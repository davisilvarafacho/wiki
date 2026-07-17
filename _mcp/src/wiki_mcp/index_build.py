"""
Constrói o índice de busca semântica da wiki.

Roda offline, sob demanda — não é parte do server MCP (que só lê o índice
já pronto). Fluxo normal: depois de um `ingest` no Claude Code (que altera
páginas da wiki), rode este script de novo pra atualizar o índice.

Uso:
    WIKI_PATH=~/wiki python -m wiki_mcp.index_build
    WIKI_PATH=~/wiki INDEX_PATH=~/.wiki-mcp-index python -m wiki_mcp.index_build

Modelo: paraphrase-multilingual-MiniLM-L12-v2 (via fastembed, ONNX, sem
torch) — bom equilíbrio para português, roda em CPU em segundos para o
tamanho atual da wiki.
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Any

import numpy as np
from fastembed import TextEmbedding

from wiki_mcp.server import _parse_frontmatter, _list_domains as _list_domains_of  # reaproveita parser e listagem

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def _default_index_path() -> Path:
    return Path(os.environ.get("INDEX_PATH", str(Path.home() / ".wiki-mcp-index")))


def _chunk_page(body: str) -> list[tuple[str, str]]:
    """Divide o corpo em chunks por seção (## heading). Retorna
    [(heading_ou_None, texto_da_secao), ...]. Se não houver ## nenhum,
    retorna o corpo inteiro como um único chunk."""
    sections = re.split(r"(?=^## )", body, flags=re.MULTILINE)
    sections = [s.strip() for s in sections if s.strip()]
    if len(sections) <= 1:
        return [(None, body.strip())]
    chunks = []
    for sec in sections:
        heading_match = re.match(r"^## (.+)$", sec, re.MULTILINE)
        heading = heading_match.group(1).strip() if heading_match else None
        chunks.append((heading, sec))
    return chunks


def build_index(wiki_root: Path, index_path: Path) -> None:
    t0 = time.time()
    print(f"Carregando modelo de embeddings ({MODEL_NAME})...")
    model = TextEmbedding(model_name=MODEL_NAME)

    records: list[dict[str, Any]] = []
    texts_to_embed: list[str] = []

    for domain in _list_domains_of():
        domain_path = wiki_root / domain
        for md_file in sorted(domain_path.rglob("*.md")):
            if md_file.name == "_index.md":
                continue
            raw = md_file.read_text(encoding="utf-8", errors="ignore")
            frontmatter, body = _parse_frontmatter(raw)
            title = str(frontmatter.get("title", md_file.stem))
            tags = frontmatter.get("tags", []) or []
            tipo = frontmatter.get("tipo")

            for heading, chunk_text in _chunk_page(body):
                # texto usado pro embedding: título + tags + heading + conteúdo
                embed_text = " | ".join(
                    filter(
                        None,
                        [title, " ".join(str(t) for t in tags), heading, chunk_text[:2000]],
                    )
                )
                texts_to_embed.append(embed_text)
                records.append(
                    {
                        "path": str(md_file.relative_to(wiki_root)),
                        "title": title,
                        "dominio": frontmatter.get("dominio", domain),
                        "tipo": tipo,
                        "tags": tags,
                        "heading": heading,
                        "snippet": chunk_text[:400],
                    }
                )

    print(f"{len(records)} chunks encontrados em {len(_list_domains_of())} domínios. Gerando embeddings...")
    vectors = np.array(list(model.embed(texts_to_embed)), dtype=np.float32)

    index_path.mkdir(parents=True, exist_ok=True)
    np.save(index_path / "embeddings.npy", vectors)
    (index_path / "metadata.json").write_text(
        json.dumps({"model": MODEL_NAME, "records": records}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Índice salvo em {index_path} ({vectors.shape[0]} vetores, dim={vectors.shape[1]}).")
    print(f"Concluído em {time.time() - t0:.1f}s.")


def main() -> None:
    wiki_root = Path(os.environ.get("WIKI_PATH", "")).expanduser().resolve()
    if not wiki_root.is_dir():
        raise SystemExit(f"WIKI_PATH inválido: '{wiki_root}'")
    build_index(wiki_root, _default_index_path())


if __name__ == "__main__":
    main()

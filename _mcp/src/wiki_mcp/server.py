"""
wiki-mcp — MCP read-only para o "second brain" pessoal do Rafacho.

Modela os tools em torno do schema descrito em CLAUDE.md/README.md do
repo `wiki` (padrão Karpathy: domínios com concepts/entities/sources/notes/
synthesis + camada _meta/), em vez de expor um filesystem genérico.

Configuração via variável de ambiente WIKI_PATH apontando para o clone
local do repo (ex: /home/rafacho/wiki).
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

import yaml
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuração e segurança de paths
# ---------------------------------------------------------------------------

WIKI_ROOT = Path(os.environ.get("WIKI_PATH", "")).expanduser().resolve()

if not WIKI_ROOT.exists() or not WIKI_ROOT.is_dir():
    raise RuntimeError(
        f"WIKI_PATH inválido ou não definido: '{WIKI_ROOT}'. "
        "Defina a variável de ambiente WIKI_PATH apontando para o clone "
        "local do repo da wiki (ex: /home/rafacho/wiki)."
    )

IGNORED_DIRS = {".git", ".obsidian"}
STANDARD_SUBDIRS = ("concepts", "entities", "sources", "notes", "synthesis")


def _safe_resolve(relative_path: str) -> Path:
    """Resolve um path relativo garantindo que ele fique dentro de WIKI_ROOT.

    Bloqueia path traversal (ex: '../../etc/passwd').
    """
    candidate = (WIKI_ROOT / relative_path).resolve()
    try:
        candidate.relative_to(WIKI_ROOT)
    except ValueError:
        raise ValueError(
            f"Path fora da wiki: '{relative_path}'. Só é possível acessar "
            f"arquivos dentro de {WIKI_ROOT}."
        )
    return candidate


def _list_domains() -> list[str]:
    domains = []
    for entry in sorted(WIKI_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in IGNORED_DIRS or entry.name in ("_meta", "raw"):
            continue
        if entry.name.startswith("."):
            continue
        # só conta como domínio se seguir o schema (tem _index.md)
        if not (entry / "_index.md").exists():
            continue
        domains.append(entry.name)
    return domains


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Separa YAML frontmatter do corpo markdown. Retorna ({}, text) se não houver."""
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    raw_yaml, body = match.group(1), match.group(2)
    try:
        meta = yaml.safe_load(raw_yaml) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, body


def _relpath(p: Path) -> str:
    return str(p.relative_to(WIKI_ROOT))


# ---------------------------------------------------------------------------
# Server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    "wiki-second-brain",
    instructions=(
        "MCP somente-leitura para a wiki pessoal (second brain) do usuário. "
        "A wiki segue o padrão Karpathy: domínios (ex: tecnico, pessoal, "
        "espiritual, estudos, empresarial) cada um com subpastas concepts/, "
        "entities/, sources/, notes/, synthesis/, mais uma camada _meta/ com "
        "index.md (catálogo global — leia primeiro em qualquer query), "
        "log.md, connections.md, glossary.md e open-questions.md. "
        "Ao responder perguntas sobre o que o usuário sabe/pensa/registrou "
        "sobre um assunto, comece por wiki_get_meta_index, depois use "
        "wiki_search e wiki_read_page para aprofundar."
    ),
)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def wiki_get_meta_index() -> str:
    """Lê _meta/index.md — o catálogo global da wiki.

    Ponto de entrada recomendado para qualquer pergunta sobre o conteúdo
    da wiki: liste aqui antes de fazer buscas mais específicas.
    """
    path = _safe_resolve("_meta/index.md")
    if not path.exists():
        return "_meta/index.md não existe ainda."
    return path.read_text(encoding="utf-8")


@mcp.tool()
def wiki_get_connections() -> str:
    """Lê _meta/connections.md — conexões cross-domain registradas
    (ex: um conceito de teologia que ressoa com um padrão de software)."""
    path = _safe_resolve("_meta/connections.md")
    if not path.exists():
        return "_meta/connections.md não existe ainda."
    return path.read_text(encoding="utf-8")


@mcp.tool()
def wiki_get_glossary() -> str:
    """Lê _meta/glossary.md — termos, convenções e abreviações usadas na wiki."""
    path = _safe_resolve("_meta/glossary.md")
    if not path.exists():
        return "_meta/glossary.md não existe ainda."
    return path.read_text(encoding="utf-8")


@mcp.tool()
def wiki_get_open_questions() -> str:
    """Lê _meta/open-questions.md — perguntas abertas que o usuário
    quer investigar no futuro."""
    path = _safe_resolve("_meta/open-questions.md")
    if not path.exists():
        return "_meta/open-questions.md não existe ainda."
    return path.read_text(encoding="utf-8")


@mcp.tool()
def wiki_recent_log(n: int = 20) -> str:
    """Retorna as últimas N entradas de _meta/log.md (log cronológico
    append-only de ingests, queries arquivadas e schema-updates).

    Args:
        n: número de entradas mais recentes a retornar (padrão 20).
    """
    path = _safe_resolve("_meta/log.md")
    if not path.exists():
        return "_meta/log.md não existe ainda."
    text = path.read_text(encoding="utf-8")
    # Entradas começam com "## [AAAA-MM-DD HH:MM] ..."
    entries = re.split(r"(?=^## \[)", text, flags=re.MULTILINE)
    entries = [e.strip() for e in entries if e.strip().startswith("## [")]
    tail = entries[-n:] if n > 0 else entries
    return "\n\n".join(tail) if tail else "Nenhuma entrada encontrada em log.md."


@mcp.tool()
def wiki_list_domains() -> list[dict[str, Any]]:
    """Lista os domínios existentes na wiki (ex: tecnico, pessoal, espiritual,
    estudos, empresarial, rafacho.dev) com uma prévia do respectivo _index.md."""
    result = []
    for domain in _list_domains():
        index_path = WIKI_ROOT / domain / "_index.md"
        preview = ""
        if index_path.exists():
            content = index_path.read_text(encoding="utf-8")
            preview = content[:400]
        result.append({"dominio": domain, "preview_index": preview})
    return result


@mcp.tool()
def wiki_list_domain(dominio: str) -> dict[str, Any]:
    """Lista a árvore de páginas de um domínio específico, organizada pelas
    subpastas padrão (concepts, entities, sources, notes, synthesis) e
    quaisquer subpastas adicionais (ex: rafacho.dev/production/*).

    Args:
        dominio: nome do domínio (ex: 'tecnico', 'pessoal', 'espiritual').
    """
    domain_path = _safe_resolve(dominio)
    if not domain_path.is_dir():
        available = ", ".join(_list_domains())
        return {
            "erro": f"Domínio '{dominio}' não encontrado.",
            "dominios_disponiveis": available,
        }

    tree: dict[str, list[str]] = {}
    for sub in sorted(domain_path.rglob("*.md")):
        if sub.name == "_index.md":
            continue
        rel = sub.relative_to(domain_path)
        bucket = rel.parts[0] if len(rel.parts) > 1 else "_raiz"
        tree.setdefault(bucket, []).append(str(rel))

    index_path = domain_path / "_index.md"
    index_content = index_path.read_text(encoding="utf-8") if index_path.exists() else ""

    return {"dominio": dominio, "index": index_content, "paginas_por_subpasta": tree}


@mcp.tool()
def wiki_read_page(path: str) -> dict[str, Any]:
    """Lê o conteúdo completo de uma página da wiki, com frontmatter
    já parseado separadamente do corpo em markdown.

    Args:
        path: caminho relativo à raiz da wiki, ex:
              'tecnico/concepts/idempotencia.md' ou
              'estudos/sources/2026-05-17-estudar-10x-melhor-emmanuel-nominato.md'.
    """
    file_path = _safe_resolve(path)
    if not file_path.exists() or not file_path.is_file():
        return {"erro": f"Página não encontrada: '{path}'"}
    text = file_path.read_text(encoding="utf-8")
    frontmatter, body = _parse_frontmatter(text)
    return {"path": path, "frontmatter": frontmatter, "conteudo": body.strip()}


@mcp.tool()
def wiki_search(
    query: str,
    dominio: str | None = None,
    tipo: str | None = None,
    max_results: int = 15,
) -> list[dict[str, Any]]:
    """Busca por um termo no título, tags e corpo das páginas da wiki.

    Busca por substring (case-insensitive) — não é busca semântica.
    Use termos específicos do conteúdo (nome de conceito, entidade, autor).

    Args:
        query: termo ou frase a buscar.
        dominio: filtra por domínio (ex: 'tecnico'). Opcional.
        tipo: filtra por tipo de página: 'concept', 'entity', 'source',
              'note', ou 'synthesis'. Opcional.
        max_results: número máximo de resultados (padrão 15).
    """
    query_lower = query.lower()
    domains = [dominio] if dominio else _list_domains()
    results = []

    for dom in domains:
        domain_path = WIKI_ROOT / dom
        if not domain_path.is_dir():
            continue
        for md_file in sorted(domain_path.rglob("*.md")):
            if md_file.name in ("_index.md",):
                continue
            text = md_file.read_text(encoding="utf-8", errors="ignore")
            frontmatter, body = _parse_frontmatter(text)

            if tipo and frontmatter.get("tipo") != tipo:
                continue

            title = str(frontmatter.get("title", md_file.stem))
            tags = frontmatter.get("tags", []) or []
            haystack = " ".join(
                [title.lower(), " ".join(str(t).lower() for t in tags), body.lower()]
            )
            if query_lower not in haystack:
                continue

            # snippet: primeira ocorrência com contexto
            idx = body.lower().find(query_lower)
            if idx == -1:
                snippet = body.strip()[:200]
            else:
                start = max(0, idx - 80)
                end = min(len(body), idx + len(query) + 80)
                snippet = ("…" if start > 0 else "") + body[start:end].replace("\n", " ") + (
                    "…" if end < len(body) else ""
                )

            results.append(
                {
                    "path": _relpath(md_file),
                    "title": title,
                    "tipo": frontmatter.get("tipo"),
                    "dominio": frontmatter.get("dominio", dom),
                    "tags": tags,
                    "snippet": snippet,
                }
            )
            if len(results) >= max_results:
                return results

    return results


_semantic_index_cache: dict[str, Any] = {}


def _load_semantic_index():
    """Carrega (lazy, uma vez por processo) o modelo de embeddings e o
    índice pré-construído por `wiki_mcp.index_build`."""
    if _semantic_index_cache:
        return _semantic_index_cache

    index_path = Path(os.environ.get("INDEX_PATH", str(Path.home() / ".wiki-mcp-index")))
    emb_path = index_path / "embeddings.npy"
    meta_path = index_path / "metadata.json"

    if not emb_path.exists() or not meta_path.exists():
        raise RuntimeError(
            f"Índice semântico não encontrado em '{index_path}'. Rode primeiro: "
            f"WIKI_PATH={WIKI_ROOT} python -m wiki_mcp.index_build"
        )

    import numpy as np
    from fastembed import TextEmbedding

    metadata = json.loads(meta_path.read_text(encoding="utf-8"))
    vectors = np.load(emb_path)
    model = TextEmbedding(model_name=metadata["model"])

    _semantic_index_cache["model"] = model
    _semantic_index_cache["vectors"] = vectors
    _semantic_index_cache["records"] = metadata["records"]
    return _semantic_index_cache


@mcp.tool()
def wiki_semantic_search(
    query: str,
    dominio: str | None = None,
    top_k: int = 8,
) -> list[dict[str, Any]]:
    """Busca semântica na wiki (por significado, não por substring exata).

    Use quando a pergunta é conceitual ou você não sabe o termo exato usado
    na wiki (ex: "o que eu já pensei sobre lidar com procrastinação" em vez
    de procurar a palavra literal "procrastinação"). Para achar um arquivo
    ou entidade por nome exato, prefira `wiki_search`.

    Requer índice pré-construído via `python -m wiki_mcp.index_build`.

    Args:
        query: pergunta ou frase em linguagem natural.
        dominio: filtra por domínio (ex: 'pessoal'). Opcional.
        top_k: quantos resultados retornar (padrão 8).
    """
    import numpy as np

    idx = _load_semantic_index()
    model, vectors, records = idx["model"], idx["vectors"], idx["records"]

    query_vec = next(model.embed([query]))
    # similaridade de cosseno (vetores do fastembed já vêm normalizados,
    # mas normalizamos de novo por segurança)
    query_norm = query_vec / (np.linalg.norm(query_vec) + 1e-9)
    vec_norms = vectors / (np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-9)
    scores = vec_norms @ query_norm

    order = np.argsort(-scores)
    results = []
    for i in order:
        rec = records[i]
        if dominio and rec.get("dominio") != dominio:
            continue
        results.append(
            {
                "path": rec["path"],
                "title": rec["title"],
                "dominio": rec.get("dominio"),
                "tipo": rec.get("tipo"),
                "secao": rec.get("heading"),
                "score": round(float(scores[i]), 4),
                "snippet": rec["snippet"],
            }
        )
        if len(results) >= top_k:
            break
    return results


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()

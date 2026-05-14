---
title: "qmd"
tipo: entity
dominio: tecnico
tags: [ferramenta, busca, markdown, bm25, vector-search, mcp]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-llm-wiki-karpathy]
---

# qmd

Motor de busca local para arquivos markdown. Combina BM25 (busca léxica) com embeddings vetoriais e re-ranking por LLM. Roda 100% on-device.

**Repositório:** https://github.com/tobi/qmd

---

## Relevância para [[llm-wiki]]

Em wikis pequenas/médias, o `index.md` é suficiente para navegação. Conforme a wiki cresce (centenas de páginas), busca estruturada se torna necessária.

O `qmd` oferece dois modos de integração com LLMs:

- **CLI** — o LLM pode executar comandos shell (`qmd search "query"`)
- **MCP server** — o LLM usa como ferramenta nativa via Model Context Protocol

---

## Características técnicas

- Busca híbrida: BM25 + vector search
- Re-ranking por LLM
- On-device (sem cloud, sem API externa)
- Indexa arquivos `.md` de uma pasta

---

## Quando usar

Não é necessário desde o início. Adicionar quando o `index.md` e navegação manual ficarem lentos ou imprecisos. Para esta wiki, a decisão de adotar o `qmd` deve ser registrada em `_meta/log.md` quando chegar o momento.

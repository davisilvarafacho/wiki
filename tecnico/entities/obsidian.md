---
title: "Obsidian"
tipo: entity
dominio: tecnico
tags: [ferramenta, markdown, note-taking, wiki, knowledge-base]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-llm-wiki-karpathy]
---

# Obsidian

Editor de markdown local orientado a conhecimento interligado. Funciona sobre uma pasta de arquivos `.md` — sem banco de dados proprietário, sem lock-in. É a ferramenta de visualização e navegação preferida para wikis no padrão [[llm-wiki]].

**Site:** https://obsidian.md

---

## Por que usar com LLM Wiki

Na metáfora de Karpathy: *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."*

- O LLM faz edições nos arquivos.
- O usuário navega os resultados em tempo real no Obsidian.
- O grafo de links é visível na **Graph View**.

---

## Funcionalidades relevantes

- **Graph View** — visualiza todos os links entre páginas. Revela hubs, órfãos, clusters.
- **Backlinks** — mostra quais páginas apontam para a atual.
- **Obsidian Web Clipper** — extensão de browser que converte artigos web para markdown. Útil para alimentar `raw/`.
- **Download de imagens** — Settings → Files and links: salvar imagens localmente em `raw/assets/`. Hotkey para baixar todos os anexos.
- **Marp** (plugin) — gera slides a partir de markdown. Útil para apresentações derivadas da wiki.
- **Dataview** (plugin) — queries sobre frontmatter YAML. Se as páginas têm `tags`, `date`, `tipo`, o Dataview gera tabelas dinâmicas.

---

## Formato de links

Obsidian usa sintaxe `[[nome-da-pagina]]` ou `[[caminho/relativo]]`. Esta wiki adota o mesmo padrão para portabilidade.

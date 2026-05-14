---
title: "LLM Wiki — Andrej Karpathy"
tipo: source
dominio: tecnico
tags: [llm, wiki, knowledge-base, rag, obsidian, gestao-do-conhecimento]
criado: 2026-05-14
atualizado: 2026-05-14
---

# LLM Wiki — Andrej Karpathy

Documento de padrão ("idea file") descrevendo como usar LLMs para construir e manter wikis pessoais persistentes. Projetado para ser compartilhado com um agente LLM como ponto de partida para instanciar o padrão.

**Fonte original:** `raw/tecnico/llm-wiki-karpathy.md`

---

## Sumário

- **Premissa:** A maioria dos sistemas (RAG, NotebookLM, uploads no ChatGPT) re-deriva conhecimento do zero a cada query. Não há acumulação.
- **Ideia central:** O LLM constrói e mantém incrementalmente uma wiki persistente — markdown interligado que fica entre o usuário e as fontes brutas. Conhecimento *compilado uma vez, mantido atual*.
- **A wiki é um artefato composto:** cross-references já estão lá, contradições já foram sinalizadas, sínteses já refletem tudo que foi lido.
- **Divisão de trabalho:** Usuário curada fontes, dirige a análise, faz boas perguntas. LLM faz todo o resto — resumir, cruzar referências, arquivar, manutenção de consistência.
- **Três camadas:**
  1. **Raw sources** — imutáveis. Fonte da verdade. LLM só lê.
  2. **Wiki** — arquivos markdown gerados/mantidos pelo LLM. LLM escreve, usuário lê.
  3. **Schema** (CLAUDE.md / AGENTS.md) — configura o LLM como mantenedor disciplinado, não chatbot genérico. Co-evolui com o uso.
- **Operações:** Ingest (processa fonte nova), Query (responde com citações), Lint (auditoria de saúde periódica).
- **Indexação:** `index.md` (orientado a conteúdo, catálogo) + `log.md` (append-only cronológico). Funciona bem até ~centenas de páginas sem RAG.
- **Respostas viram páginas:** análises, comparações, conexões descobertas via query devem ser arquivadas de volta na wiki — explorações também compõem.
- **Ferramentas úteis:** [[obsidian]] (IDE da wiki), [[qmd]] (busca local BM25/vector), Marp (slides), Dataview (queries sobre frontmatter).
- **Raiz histórica:** [[memex]] de Vannevar Bush (1945) — a visão era exatamente esta: conhecimento pessoal curado com trilhas associativas. O que Bush não resolveu foi quem faz a manutenção. O LLM resolve isso.
- **Por que funciona:** O gargalo de wikis não é a leitura ou o pensamento — é a manutenção. Humans abandonam wikis porque o custo de manutenção cresce mais rápido que o valor. LLMs não se cansam nem esquecem de atualizar cross-references.

---

## Citações relevantes

> *"The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged."*

> *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."*

> *"Good answers can be filed back into the wiki as new pages. This way your explorations compound in the knowledge base just like ingested sources do."*

> *"Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."*

> *"The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."*

---

## Takeaways

1. O padrão distingue **dois regimes**: re-derivação a cada query (RAG clássico) vs. compilação incremental persistente (LLM Wiki). Este projeto implementa o segundo.
2. O schema (CLAUDE.md) é o artefato mais crítico da infraestrutura — é o que transforma o LLM de chatbot genérico em mantenedor disciplinado.
3. **Respostas de qualidade merecem ser arquivadas.** Toda síntese valiosa que o LLM produz em resposta a uma query deve virar página na wiki.
4. O log parseable (`grep "^## \["`) é uma boa prática de engenharia aplicada a conhecimento.
5. A analogia com Memex reforça que a ideia é velha — o que mudou é a viabilidade da manutenção.

---

## Páginas criadas/atualizadas neste ingest

- [[tecnico/concepts/llm-wiki]] — conceito central
- [[tecnico/concepts/rag]] — padrão contrastante
- [[tecnico/entities/obsidian]] — ferramenta mencionada
- [[tecnico/entities/qmd]] — ferramenta de busca local
- [[tecnico/entities/memex]] — antecedente histórico

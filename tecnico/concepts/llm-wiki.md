---
title: "LLM Wiki"
tipo: concept
dominio: tecnico
tags: [llm, wiki, knowledge-base, gestao-do-conhecimento, manutencao, compounding]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [tecnico/sources/2026-05-14-llm-wiki-karpathy]
---

# LLM Wiki

Padrão arquitetural para construção e manutenção de bases de conhecimento pessoais usando LLMs. A ideia central: em vez de re-derivar conhecimento de fontes brutas a cada consulta ([[rag]]), o LLM **compila o conhecimento incrementalmente** em uma wiki persistente de arquivos markdown interligados.

---

## O problema que resolve

Sistemas baseados em [[rag]] re-derivam respostas do zero a cada query. Não há acumulação: perguntas que exigem síntese de cinco documentos forçam o modelo a localizar e conectar fragmentos toda vez. O conhecimento não cresce.

Wikis mantidas por humanos têm o problema oposto: o custo de manutenção (atualizar cross-references, sinalizar contradições, manter consistência entre dezenas de páginas) cresce mais rápido que o valor percebido. Humanos abandonam wikis.

O LLM Wiki resolve os dois problemas: acumulação persistente + manutenção de custo próximo a zero.

---

## Arquitetura

Três camadas:

**1. Raw sources (imutável)**
Documentos brutos curados pelo usuário — artigos, papers, transcrições, PDFs. O LLM lê, nunca modifica.

**2. Wiki (LLM-mantida)**
Arquivos markdown gerados e mantidos pelo LLM: páginas de entidade, páginas de conceito, sumários de fonte, notas, sínteses. O LLM escreve; o usuário lê e navega.

**3. Schema**
Documento de configuração (ex: `CLAUDE.md`, `AGENTS.md`) que instrui o LLM sobre estrutura da wiki, convenções e workflows. É o que transforma o LLM de chatbot genérico em mantenedor disciplinado. Co-evolui com o uso.

---

## Operações fundamentais

- **Ingest:** fonte nova entra, LLM processa, atualiza páginas relevantes, sinaliza contradições, registra no log. Uma fonte toca tipicamente 5–15 páginas.
- **Query:** LLM lê o índice, navega páginas relevantes, sintetiza resposta com citações. Respostas valiosas são arquivadas de volta como novas páginas.
- **Lint:** auditoria periódica — contradições, páginas órfãs, conceitos sem página, cross-references faltando.

---

## Infraestrutura de navegação

- **`index.md`** — catálogo orientado a conteúdo. LLM lê antes de qualquer query para localizar páginas. Funciona sem RAG até centenas de páginas.
- **`log.md`** — registro cronológico append-only com prefixo parseable (`## [AAAA-MM-DD] tipo | título`).

---

## Divisão de trabalho

| Usuário | LLM |
|---|---|
| Cura fontes | Resume fontes |
| Dirige análise | Atualiza cross-references |
| Faz boas perguntas | Sinaliza contradições |
| Pensa sobre o significado | Mantém consistência |

---

## Ferramentas associadas

- [[obsidian]] — IDE da wiki (graph view, navegação de links, Marp, Dataview)
- [[qmd]] — busca local BM25/vector para wikis grandes
- Git — versionamento da wiki inteira

---

## Antecedente histórico

Ver [[memex]] — visão de Vannevar Bush (1945) de um repositório pessoal curado com trilhas associativas. A diferença: Bush não tinha solução para a manutenção. O LLM resolve isso.

---

## Nota de meta-aplicação

Esta wiki implementa este padrão. O `CLAUDE.md` é o schema. Este arquivo é a prova de que o conceito funciona recursivamente — a primeira fonte ingerida é o próprio documento que descreve o padrão.

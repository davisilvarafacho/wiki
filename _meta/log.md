---
title: "Log da Wiki"
tipo: meta
---

# Log

Registro cronológico append-only de tudo que aconteceu na wiki. Cada entrada começa com `## [AAAA-MM-DD HH:MM] <tipo> | <título>`.

Tipos: `ingest`, `query`, `lint`, `schema-update`, `setup`.

Para ver as últimas N entradas:

```bash
grep "^## \[" log.md | tail -10
```

---

## [2026-05-14] setup | Wiki inicializada

- Estrutura criada com 5 domínios: tecnico, pessoal, espiritual, estudos, negocio
- Schema (`CLAUDE.md`) definido
- Camada `_meta/` inicializada (index, log, connections, glossary, open-questions)
- Padrão fractal aplicado: cada domínio com `concepts/ entities/ sources/ notes/ synthesis/`

## [2026-05-14] schema-update | Renomeação negocio → empresarial

- Pasta `negocio/` renomeada para `empresarial/` por preferência do usuário
- `raw/negocio/` renomeada para `raw/empresarial/`
- Referências atualizadas em `CLAUDE.md` e `_meta/index.md`

## [2026-05-14] schema-update | Novo domínio: rafacho.dev

- Criado domínio `rafacho.dev/` para o canal YouTube do usuário
- Estrutura padrão aplicada (concepts, entities, sources, notes, synthesis)
- **Exceção autorizada ao schema:** subpasta extra `production/` com sub-estrutura própria (ideias, roteiros, publicados, metricas, planejamento). Justificativa: o domínio tem natureza dupla (aprendizado do ofício + produção operacional). Exceção documentada em `CLAUDE.md` na seção "Exceções autorizadas ao padrão".
- `raw/rafacho.dev/` criado
- Referências adicionadas em `_meta/index.md`

## [2026-05-14 18:51] schema-update | Princípio de extensibilidade ao estilo SRP

- Adicionado princípio fundamental #5 no `CLAUDE.md`: "Extensibilidade ao estilo SRP"
- Formaliza a preferência do dono: exceções ao padrão fractal são **aditivas**, nunca substitutivas
- Justificativa registrada: preserva previsibilidade, permite migração de exceções para o padrão, mantém o schema como histórico de decisões

## [2026-05-14 18:52] ingest | LLM Wiki — Andrej Karpathy

Fonte: `raw/tecnico/llm-wiki-karpathy.md`

Páginas criadas:
- `tecnico/sources/2026-05-14-llm-wiki-karpathy.md`
- `tecnico/concepts/llm-wiki.md`
- `tecnico/concepts/rag.md`
- `tecnico/entities/obsidian.md`
- `tecnico/entities/qmd.md`
- `tecnico/entities/memex.md`

Páginas atualizadas:
- `tecnico/_index.md`
- `_meta/index.md`
- `_meta/connections.md`

Conexões registradas em `_meta/connections.md`:
- LLM Wiki como padrão transversal a todos os domínios
- Memex (Bush 1945) como antecedente histórico do LLM Wiki

## [2026-05-14 21:03] ingest | The Part of PostgreSQL We Hate the Most (Andy Pavlo)

Fonte: `raw/tecnico/2026-05-14 The Part of PostgreSQL We Hate the Most.md`

Páginas criadas:
- `tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most.md`
- `tecnico/concepts/mvcc.md`
- `tecnico/concepts/table-bloat.md`
- `tecnico/concepts/hot-update.md`
- `tecnico/concepts/autovacuum.md`
- `tecnico/entities/postgresql.md`
- `tecnico/entities/autores/andy-pavlo.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/log.md`

## [2026-05-15 17:47] ingest | How DNS Works (Dhruv Prajapati, FreeCodeCamp)

Fonte: `raw/tecnico/2026-05-15 How DNS Works A Guide to Understanding the Internet's Address Book.md`

Páginas criadas:
- `tecnico/sources/2026-05-15-how-dns-works.md`
- `tecnico/concepts/dns.md`
- `tecnico/concepts/anycast.md`
- `tecnico/concepts/glue-records.md`
- `tecnico/entities/autores/dhruv-prajapati.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/log.md`

Destaques do ingest:
- DNS como conceito central: hierarquia root → TLD → authoritative; resolução recursiva em 5 etapas
- Anycast: conceito transversal (DNS + CDNs) que merecia página própria
- Glue records: mecanismo específico e elegante para resolver dependência circular de bootstrapping
- TTL como variável crítica em migrações DNS — ponto prático importante


## [2026-05-14] ingest | What is a Tech Lead? (Josh Hornby)

Fonte: `raw/tecnico/2026-05-14 What is a Tech Lead.md`

Páginas criadas:
- `tecnico/sources/2026-05-14-what-is-a-tech-lead.md`
- `tecnico/concepts/tech-lead.md`
- `tecnico/concepts/trabalho-alavancado.md`
- `tecnico/entities/autores/josh-hornby.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/connections.md`

Conexões registradas:
- tech-lead ↔ empresarial: tensão entre entregar e desenvolver pessoas ressoa com gestão organizacional
- trabalho-alavancado ↔ pessoal: conceito de multiplicador aplica-se também a hábitos e desenvolvimento pessoal

## [2026-05-17 00:00] ingest | Nada é difícil, só é novo pra você (Pinho)

Fonte: `raw/pessoal/2026-05-17-nada-e-dificil-so-e-novo.md` — vídeo YouTube

Páginas criadas:
- `pessoal/sources/2026-05-17-nada-e-dificil-so-e-novo.md`
- `pessoal/concepts/novidade-vs-dificuldade.md`
- `pessoal/concepts/mecanismo-de-protecao-cerebral.md`
- `pessoal/concepts/dedicacao-vs-talento.md`
- `pessoal/entities/autores/pinho.md`

Páginas atualizadas:
- `pessoal/_index.md`
- `_meta/index.md`

Primeiro ingest do domínio `pessoal/`. Tese central: dificuldade percebida é quase sempre novidade disfarçada, amplificada pelo mecanismo de proteção cerebral e pelo hábito cultural de reclamação. Antídoto: dedicação consistente com interesse genuíno — que é exatamente o que o senso comum chama de talento.

---

## [2026-05-14 20:06] schema-update | Convenção de autores como entidade

- Subpasta `entities/autores/` adicionada em todos os domínios (tecnico, pessoal, espiritual, estudos, empresarial, rafacho.dev)
- Frontmatter estendido para autores: `entity_tipo`, `area`, `formacao`, `nacionalidade`, `link_principal`
- Regras de lar canônico e cross-domain definidas no `CLAUDE.md`
- No ingest, stub em `entities/autores/` criado automaticamente quando fonte tem campo `autor` sem página correspondente
- `_meta/index.md` atualizado: seção "Entidades" de cada domínio subdivida em "Autores" e "Outras"


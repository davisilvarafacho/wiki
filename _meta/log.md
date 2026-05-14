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

## [2026-05-14] schema-update | Princípio de extensibilidade ao estilo SRP

- Adicionado princípio fundamental #5 no `CLAUDE.md`: "Extensibilidade ao estilo SRP"
- Formaliza a preferência do dono: exceções ao padrão fractal são **aditivas**, nunca substitutivas
- Justificativa registrada: preserva previsibilidade, permite migração de exceções para o padrão, mantém o schema como histórico de decisões

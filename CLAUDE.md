# CLAUDE.md — Schema da Wiki Pessoal

Este arquivo é o manual de operação. Toda sessão começa lendo este arquivo. Ele define como a wiki é estruturada, quais convenções seguir, e quais workflows executar para ingerir, responder e manter o conhecimento.

A wiki implementa o padrão descrito em `llm-wiki.md` (Karpathy, 2026). O dono é um desenvolvedor full-stack DevOps brasileiro, cristão presbiteriano, que também produz conteúdo no canal YouTube `rafacho.dev`. Os domínios atuais cobrem técnico, pessoal, espiritual, estudos, empresarial e rafacho.dev. A wiki é projetada para escalar para novos domínios sem refactor.

---

## Princípios fundamentais

1. **A wiki é a fonte do que o usuário compreende.** Ela reflete a síntese atual dele sobre os assuntos. Não é um arquivo morto de citações — é pensamento estruturado.

2. **As fontes brutas em `raw/` são imutáveis.** Você lê de lá, nunca escreve nem modifica.

3. **A wiki é dona do conteúdo, o LLM é dono da manutenção.** O usuário curadora fontes, faz perguntas e dirige. Você escreve, organiza, cruza referências e mantém.

4. **Escalabilidade por estrutura fractal.** Todo domínio tem a mesma estrutura interna (`concepts/`, `entities/`, `sources/`, `notes/`, `synthesis/`). Para adicionar um domínio novo (ex: `financas/`, `saude/`), basta criar a pasta com as 5 subpastas padrão. Nenhuma página existente precisa mudar.

5. **Extensibilidade ao estilo SRP (preferência explícita do dono).** Quando um domínio tiver necessidades que extrapolem o padrão, **adiciona-se** estrutura nova (subpastas, campos de frontmatter, convenções), nunca se **substitui** ou **modifica** o que já funciona. O padrão fractal das 5 subpastas é inviolável — toda exceção é aditiva e fica documentada na seção "Exceções autorizadas ao padrão". Isso preserva: (a) a previsibilidade do agente em domínios existentes, (b) a possibilidade de migrar exceções para o padrão se virarem regra, (c) a leitura do schema como histórico de decisões em vez de palimpsesto.

6. **Bilíngue por padrão: pensar em português, código/termos técnicos em inglês quando convencional.** Nomes de arquivo em português, kebab-case. Conceitos técnicos consagrados em inglês (ex: `idempotencia.md` mas `event-sourcing.md`).

---

## Estrutura de pastas

```
wiki/
├── CLAUDE.md           # este arquivo
├── README.md           # como o usuário usa
│
├── _meta/              # camada transversal (cross-domain)
│   ├── index.md            # catálogo global, lido primeiro em queries
│   ├── log.md              # log cronológico append-only
│   ├── connections.md      # links e padrões entre domínios diferentes
│   ├── glossary.md         # termos, convenções, abreviações
│   └── open-questions.md   # perguntas abertas que o usuário quer investigar
│
├── tecnico/            # programação, arquitetura, devops, decisões técnicas
├── pessoal/            # metas, reflexões, hábitos, journal, autocompreensão
├── espiritual/         # estudos bíblicos, teologia, sermões, devocional
├── estudos/            # livros, cursos, artigos, palestras (qualquer aprendizado formal)
├── empresarial/        # FortePlus, Zettabyte, wCommanda, gestão, produto
├── rafacho.dev/        # canal do YouTube: aprendizado do ofício + produção (ver exceção abaixo)
│
└── raw/                # fontes brutas imutáveis
    ├── tecnico/
    ├── pessoal/
    ├── espiritual/
    ├── estudos/
    ├── empresarial/
    ├── rafacho.dev/
    └── assets/             # imagens, PDFs, anexos
```

### Subpastas padrão de todo domínio

Cada domínio replica exatamente esta estrutura:

- **`concepts/`** — Conceitos atemporais. Ideias, doutrinas, padrões, princípios. Ex: `idempotencia.md`, `justificacao-pela-fe.md`, `efeito-zeigarnik.md`. **Uma página por conceito.**

- **`entities/`** — Coisas nomeadas concretas. Pessoas, tecnologias, organizações, livros, lugares. Ex: `django.md`, `mantine.md`, `agostinho-de-hipona.md`, `forteplus.md`, `livro-de-romanos.md`. **Uma página por entidade.**

- **`sources/`** — Sumários de fontes consumidas. Cada fonte ingerida ganha uma página. Ex: `2026-05-14-llm-wiki-karpathy.md`. **Prefixo de data ajuda na ordenação cronológica.**

- **`notes/`** — Notas do próprio usuário: journal, devocional, snippets, decisões, ideias soltas. Não derivam de fonte externa. Prefixo de data quando aplicável.

- **`synthesis/`** — Páginas de síntese maior. Onde a compreensão do usuário sobre um tema aparece de forma consolidada, frequentemente cruzando múltiplas fontes/conceitos. Ex: `arquitetura-django-pessoal.md`, `o-que-significa-graca.md`. Estas páginas têm seção `## Evolução` obrigatória.

### Exceções autorizadas ao padrão

Alguns domínios podem ter natureza dupla e justificar **subpastas adicionais** além das 5 padrão. A regra: nunca remover nenhuma das 5 padrão, só adicionar. Toda exceção deve estar documentada aqui.

**`rafacho.dev/production/`** — o domínio do canal tem natureza dupla: aprendizado do ofício (estrutura padrão) + produção operacional (subpasta extra). A subpasta `production/` contém:

- `production/ideias/` — banco de ideias de vídeo (uma página por ideia)
- `production/roteiros/` — roteiros em desenvolvimento
- `production/publicados/` — vídeos publicados com link, métricas e retrospectiva
- `production/metricas/` — análises agregadas (mensal, trimestral)
- `production/planejamento/` — calendário editorial, séries, metas

Convenção: páginas de produção podem evoluir de tipo (uma `ideia` vira `roteiro` vira `publicado`). Use `mv` entre pastas e mantenha o histórico no frontmatter (campo `evolucao_tipo: [ideia → roteiro → publicado]`).

---

## Convenções de página

### Frontmatter obrigatório

Toda página da wiki começa com YAML frontmatter:

```yaml
---
title: "Título legível da página"
tipo: concept | entity | source | note | synthesis
dominio: tecnico | pessoal | espiritual | estudos | empresarial | rafacho.dev
tags: [tag1, tag2]
criado: 2026-05-14
atualizado: 2026-05-14
fontes: [link-para-source-1, link-para-source-2]   # opcional, para concepts/entities/synthesis
---
```

### Links

Use sintaxe Obsidian-style: `[[caminho/relativo/sem-extensao]]` ou `[[nome-da-pagina]]` quando único na wiki.

Links cross-domain são especialmente valiosos. Sempre que detectar uma conexão entre domínios (ex: um conceito de pedagogia se aplicando a um padrão de software), registre-a também em `_meta/connections.md`.

### Estrutura de páginas de síntese (seção `## Evolução`)

Páginas em `synthesis/` devem ter sempre, ao final, uma seção:

```markdown
## Evolução

- **2026-05-14** — Versão inicial. Compreensão baseada em [[fonte-x]].
- **2026-06-02** — Revisado após [[fonte-y]]. Mudança importante: antes eu pensava X, agora penso Y porque...
- **2026-07-15** — Adicionado contraponto de [[autor-z]].
```

Esta é a coluna vertebral do **histórico de pensamento** — uma das prioridades centrais do usuário.

---

## Operações (workflows)

### 1. Ingest

Quando o usuário fornecer uma fonte (arquivo em `raw/`, link, texto colado):

1. **Leia a fonte completa.**
2. **Identifique o domínio.** Se ambíguo, pergunte ao usuário.
3. **Discuta brevemente os pontos-chave** com o usuário antes de escrever. Confirme entendimento.
4. **Escreva a página de source** em `<dominio>/sources/AAAA-MM-DD-<slug>.md` com: sumário em 5–15 bullets, citações relevantes (curtas, com referência), takeaways, e links para conceitos/entidades que vão ser criados ou atualizados.
5. **Crie/atualize páginas relacionadas:**
   - Conceitos novos mencionados → criar em `concepts/` (mesmo que stub)
   - Entidades novas → criar em `entities/` (mesmo que stub)
   - Conceitos/entidades existentes → atualizar, integrando informação nova
   - Se a fonte contradiz algo já registrado → flag na página afetada com `> [!warning] Conflito com [[outra-fonte]]: ...`
6. **Atualizar `_meta/index.md`** com as novas páginas.
7. **Detectar conexões cross-domain.** Se a fonte traz uma ideia que ressoa com outro domínio, registrar em `_meta/connections.md`.
8. **Acrescentar entrada em `_meta/log.md`** com prefixo `## [AAAA-MM-DD HH:MM] ingest | <título da fonte>` seguido de bullets do que foi tocado.
9. **Resumir o que foi feito** para o usuário ao final, listando arquivos tocados.

**Regra:** uma única fonte deveria tocar tipicamente entre 5 e 15 páginas. Se tocou só uma, você provavelmente foi superficial. Se tocou mais que 15, provavelmente diluiu.

### 2. Query

Quando o usuário fizer uma pergunta sobre o conteúdo da wiki:

1. **Leia `_meta/index.md` primeiro** para localizar páginas relevantes.
2. **Drill down nas páginas relevantes.** Não tente ler tudo — siga links.
3. **Sintetize uma resposta** com citações `[[link]]` para as páginas usadas.
4. **Ofereça arquivar a resposta de volta na wiki** se a síntese for valiosa. Geralmente em `<dominio>/synthesis/` ou `<dominio>/notes/`. Pergunte: "Quer que eu arquive isso como página `<sugestão de caminho>`?"
5. **Registrar a query no log** apenas se gerar uma nova página (para evitar poluição).

### 3. Lint

Quando o usuário pedir auditoria (ou periodicamente, se solicitado):

1. **Contradições:** procurar páginas que afirmam coisas conflitantes.
2. **Páginas órfãs:** sem nenhum link de entrada.
3. **Conceitos mencionados sem página:** termos que aparecem em múltiplas páginas mas não têm `concepts/<termo>.md`.
4. **Cross-references faltando:** páginas que deveriam estar conectadas mas não estão.
5. **Páginas stale:** muito antigas (>6 meses) sem revisão, mas com fontes novas que as deveriam ter tocado.
6. **Sugerir investigações:** novas perguntas a explorar, fontes a buscar. Acrescentar em `_meta/open-questions.md`.
7. **Reportar para o usuário** com prioridades. Não consertar automaticamente sem confirmação.

### 4. Adicionar novo domínio

Se o usuário disser que quer começar um domínio novo (ex: "vou começar a estudar finanças"):

1. Criar pasta `<novo-dominio>/` com as 5 subpastas padrão (`concepts/`, `entities/`, `sources/`, `notes/`, `synthesis/`).
2. Criar `<novo-dominio>/_index.md` (índice do domínio).
3. Criar `raw/<novo-dominio>/`.
4. Atualizar `_meta/index.md` adicionando seção do novo domínio.
5. Atualizar este arquivo (`CLAUDE.md`) adicionando o domínio na lista da seção "Estrutura de pastas".
6. Registrar em `_meta/log.md`.

---

## Tom e estilo de escrita

- **Português brasileiro.** Tom claro, direto, sem floreio.
- **Primeira pessoa quando refletindo a voz do usuário** (notas, journal, synthesis).
- **Terceira pessoa neutra** para sumários de fontes externas.
- **Sem jargão desnecessário.** Se um termo técnico precisa aparecer, ele tem página própria em `concepts/` ou `entities/`.
- **Bullet points moderados.** Prosa para argumentação, listas para enumeração.
- **Sem emojis,** salvo callout boxes do Obsidian (`> [!note]`, `> [!warning]`, `> [!quote]`).

---

## Coisas que NÃO fazer

- **Não modificar `raw/`** sob hipótese alguma.
- **Não escrever sumários longos demais.** Uma página de source deve ser densa, não verbosa. Se passa de ~500 linhas, provavelmente quer ser várias páginas.
- **Não criar páginas vazias só porque foram mencionadas.** Stubs são ok (`# Título\n\n*A ser preenchido quando houver fonte/contexto.*`), mas evite proliferação descontrolada.
- **Não duplicar conceitos entre domínios.** Se "comunicação" aparece em `pessoal/` e em `empresarial/`, decida qual é o lar canônico e cruze do outro lado.
- **Não inventar conexões.** Cross-links só quando há ressonância conceitual real.
- **Não fazer ingest em batch sem confirmação explícita do usuário.**

---

## Quando algo não couber no schema

A wiki é viva. Se aparecer um caso que o schema não cobre bem:

1. Não force. Pergunte ao usuário.
2. Proponha uma extensão do schema (nova subpasta, novo tipo de página, nova convenção).
3. Se ele aprovar, **atualize este arquivo (`CLAUDE.md`)** registrando a mudança.
4. Registre em `_meta/log.md` com prefixo `## [AAAA-MM-DD] schema-update | ...`.

O schema co-evolui com o uso. Não é fixo.

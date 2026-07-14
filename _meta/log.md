---
title: "Log da Wiki"
tipo: meta
criado: 2026-05-14
atualizado: 2026-07-14
---

# Log

Registro cronológico append-only de tudo que aconteceu na wiki. Cada entrada começa com `## [AAAA-MM-DD HH:MM] <tipo> | <título>`.

Tipos: `ingest`, `query`, `lint`, `schema-update`, `setup`.

Para ver as últimas N entradas:

```bash
grep "^## \[" log.md | tail -10
```

---

## [2026-06-03] ingest | Por que o Nubank usa uma linguagem que quase ninguém conhece? (pasquadev, YouTube)

Fonte: vídeo YouTube — https://www.youtube.com/watch?v=3WDjURKrUK4
Autor: Viní Pasquantônio (pasquadev) — engenheiro brasileiro, canal pasquadev

Páginas criadas:
- `raw/tecnico/2026-06-03-nubank-clojure-event-sourcing-pasquadev.md`
- `tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev.md`
- `tecnico/concepts/programacao-funcional.md`
- `tecnico/concepts/event-sourcing.md`
- `tecnico/concepts/imutabilidade.md`
- `tecnico/concepts/side-effects.md`
- `tecnico/entities/nubank.md`
- `tecnico/entities/clojure.md`
- `tecnico/entities/datomic.md`
- `tecnico/entities/autores/vini-pasquantonio.md`

---

## [2026-06-03] ingest | O mecanismo que está quebrando seu cérebro (Dr. José Ricardo Gois, YouTube)

Fonte: `raw/pessoal/2026-06-03-o-mecanismo-que-esta-quebrando-seu-cerebro.md`
URL: https://www.youtube.com/watch?v=mfEeuu4OBao

Páginas criadas:
- `raw/pessoal/2026-06-03-o-mecanismo-que-esta-quebrando-seu-cerebro.md`
- `pessoal/sources/2026-06-03-o-mecanismo-que-esta-quebrando-seu-cerebro.md`
- `pessoal/concepts/scroll-infinito.md`
- `pessoal/concepts/dopamina.md`
- `pessoal/concepts/reforco-por-razao-variavel.md`
- `pessoal/concepts/dessensibilizacao-dopaminergica.md`

Páginas atualizadas:
- `pessoal/entities/autores/jose-ricardo-gois.md` — adicionadas novas fontes e conceitos
- `_meta/index.md`
- `_meta/log.md`

Conexões cross-domain detectadas:
- `pessoal/scroll-infinito` + `pessoal/dessensibilizacao-dopaminergica` ↔ `pessoal/manutencao-da-vida`: restaurar o sistema nervoso segue a mesma lógica de juros compostos; negligência acumula dano silencioso
- `pessoal/dopamina` + `pessoal/scroll-infinito` ↔ `estudos/carga-cognitiva`: o celular rouba atenção mesmo sem scroll ativo; o scroll intensifica o mesmo mecanismo
- `pessoal/reforco-por-razao-variavel` ↔ `pessoal/mecanismo-de-protecao-cerebral`: ambos descrevem respostas automáticas do cérebro que contornam a decisão consciente

Stub a criar: `pessoal/entities/autores/byung-chul-han.md` (filósofo "sociedade da autoexploração")

---

## [2026-06-03] ingest | O Tédio É a Saída dos Seus Problemas (Dr. José Ricardo Gois, YouTube)

Fonte: vídeo YouTube — https://youtu.be/W5yUiVWluGk
Autor: Dr. José Ricardo Gois — psicólogo e criador de conteúdo brasileiro

Páginas criadas:
- `raw/pessoal/2026-06-03-o-tedio-e-a-saida-dos-seus-problemas.md`
- `pessoal/sources/2026-06-03-o-tedio-e-a-saida-dos-seus-problemas.md`
- `pessoal/concepts/ocio.md`
- `pessoal/concepts/alexitimia.md`
- `pessoal/concepts/economia-da-atencao.md`
- `pessoal/concepts/modo-do-todo-mundo.md`
- `pessoal/entities/autores/jose-ricardo-gois.md`

Conexões cross-domain adicionadas em `_meta/connections.md`:
- ócio ↔ carga cognitiva (pessoal ↔ estudos)
- economia da atenção ↔ carga cognitiva (pessoal ↔ estudos)
- modo do todo mundo ↔ zona de conforto (pessoal interno)
- ócio ↔ devocional cristão (pessoal ↔ espiritual)

---

## [2026-06-03] ingest | I was laid off by Atlassian (Vasilios Syrakis, YouTube)

Fonte: vídeo YouTube — https://www.youtube.com/watch?v=55pTFVoclvE
Autor: Vasilios Syrakis — engenheiro de plataforma com 8 anos de Atlassian

Páginas criadas:
- `tecnico/sources/2026-05-24-laid-off-atlassian-vasilios.md`
- `tecnico/entities/autores/vasilios-syrakis.md`
- `tecnico/concepts/envoy-control-plane.md`
- `tecnico/concepts/sidecar-pattern.md`
- `tecnico/concepts/platform-engineering.md`
- `tecnico/concepts/churn-codebase.md`
- `tecnico/entities/envoy-proxy.md` (stub com contexto Atlassian)

Páginas atualizadas:
- `_meta/connections.md` — 2 novas conexões cross-domain
- `_meta/index.md`
- `_meta/log.md`

Conexões cross-domain registradas:
- `tecnico/churn-codebase` ↔ `pessoal/manutencao-da-vida`: manutenção de software e manutenção de vida como o mesmo princípio (deterioração com juros compostos)
- `tecnico/platform-engineering` ↔ `tecnico/trabalho-alavancado`: centralizar concerns no edge como exemplo concreto de leverage técnico

---

## [2026-06-03] ingest | Give God 56 Seconds.. Don't Skip This Message. (For Purpose Driven Men, YouTube)

Fonte: `raw/pessoal/2026-06-03-give-god-56-seconds.md`
URL: https://www.youtube.com/watch?v=VcVTOR7zXrM

Páginas criadas:
- `raw/pessoal/2026-06-03-give-god-56-seconds.md`
- `pessoal/sources/2026-06-03-give-god-56-seconds.md`
- `pessoal/concepts/mentalidade-de-temporada.md`
- `pessoal/entities/autores/for-purpose-driven-men.md`

Páginas atualizadas:
- `pessoal/concepts/autodisciplina.md` — link para mentalidade-de-temporada
- `pessoal/concepts/paciencia-ativa.md` — link para mentalidade-de-temporada como complemento direto
- `_meta/index.md`
- `_meta/log.md`

Conexões cross-domain registradas:
- `pessoal/mentalidade-de-temporada` ↔ `espiritual/`: padrão prova → formação → benção é central em Tiago 1:2-4 e Romanos 5:3-4

---

## [2026-05-18 10:40] ingest | VRAG: Como funciona o Visual RAG do Alibaba (Qwen 3.6 Plus)

Fonte: conversa com Qwen 3.6 Plus. Pergunta original: "Como funciona o VRAG proposto pelo Alibaba?"
Referência externa: https://github.com/Alibaba-NLP/VRAG

Páginas criadas:
- `tecnico/notes/2026-05-18-vrag-alibaba.md` — nota principal com conteúdo da conversa
- `tecnico/concepts/vrag.md` — VRAG (Visual RAG); arquitetura com VLMs, raciocínio iterativo e VRAG-RL
- `tecnico/concepts/vlm.md` — Vision-Language Model; stub
- `tecnico/concepts/vimrag.md` — VimRAG (Grafo de Memória Multimodal); stub
- `tecnico/entities/alibaba-nlp.md` — grupo de pesquisa Alibaba; autores do VRAG e série Qwen

Páginas atualizadas:
- `tecnico/concepts/rag.md` — adicionada seção "Evolução: VRAG"
- `_meta/index.md`
- `_meta/connections.md`

Conexão cross-domain registrada:
- `tecnico/vrag` ↔ `rafacho.dev/`: tema com alto potencial de conteúdo para o canal

---

## [2026-05-18 10:38] lint | Auditoria geral da wiki

- Lint executado. Wiki em estado excelente.
- Correção: adicionado campo `criado: 2026-05-14` em todos os `_index.md` de domínio e arquivos `_meta/`.
- Adicionado `atualizado: 2026-05-18` em `_meta/log.md` (estava faltando).
- Arquivos tocados: 6 `_index.md`, 5 arquivos `_meta/`.

---

## [2026-05-18] ingest | This video will find you before your next chapter (emmy, YouTube)

Fonte: `raw/pessoal/2026-05-17-este-video-vai-te-encontrar.md`
URL: https://www.youtube.com/watch?v=pfY6b87BDbY

Páginas criadas:
- `raw/pessoal/2026-05-17-este-video-vai-te-encontrar.md`
- `pessoal/sources/2026-05-17-este-video-vai-te-encontrar.md`
- `pessoal/concepts/paciencia-ativa.md`
- `pessoal/concepts/gratidao.md`

Páginas atualizadas:
- `pessoal/concepts/memento-mori.md` — adicionados links para paciencia-ativa e gratidao
- `pessoal/concepts/dedicacao-vs-talento.md` — adicionado link para paciencia-ativa
- `_meta/index.md`
- `_meta/connections.md`

Conexões cross-domain registradas:
- `pessoal/paciencia-ativa` ↔ `espiritual/` (a preencher): espera ativa como eco da espera esperançosa bíblica (Romanos 8:25, Salmo 27:14)
- `pessoal/gratidao` ↔ `espiritual/` (a preencher): gratidão com fundamento na doutrina da providência (Filipenses 4:6)

---

## [2026-05-17] ingest | Me dê 72 segundos e vou te fazer ESTUDAR 10x MELHOR (Emmanuel Nominato)

Fonte: YouTube — https://www.youtube.com/watch?v=NFWTzRiHmo0

Páginas criadas:
- `raw/estudos/2026-05-17-estudar-10x-melhor-emmanuel-nominato.md`
- `estudos/sources/2026-05-17-estudar-10x-melhor-emmanuel-nominato.md`
- `estudos/concepts/pratica-com-recuperacao.md`
- `estudos/concepts/pratica-espacada.md`
- `estudos/concepts/dificuldades-desejadas.md`
- `estudos/concepts/ilusao-do-aprendizado.md`
- `estudos/concepts/carga-cognitiva.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/connections.md`
- `estudos/_index.md`

Primeiro ingest do domínio `estudos/`. Tese central: aprendizado começa por atenção (sono + ausência de distrações) antes de qualquer técnica. A técnica mais eficaz e contraintuitiva é a prática com recuperação — fechar o material e tentar lembrar gera o atrito que consolida. Dificuldades desejadas nomeiam o paradoxo: facilitar demais impede a consolidação.

Conexões cross-domain registradas em `_meta/connections.md`:
- `dificuldades-desejadas` ↔ `pessoal/dedicacao-vs-talento`: atrito como mecanismo, não obstáculo
- `ilusao-do-aprendizado` ↔ `pessoal/novidade-vs-dificuldade`: percepções que enganam sobre o estado real
- `pratica-com-recuperacao` ↔ `pessoal/fingir-ate-se-tornar`: esforço ativo sem rede como mecanismo de crescimento
- `carga-cognitiva` ↔ `tecnico/`: context switching em desenvolvimento como o mesmo problema

---

## [2026-05-17] ingest | Nesses 51 Segundos... eu vou APAGAR seu Medo de Errar (Cultura Renegada, YouTube Short)

Fonte: `raw/pessoal/2026-05-17-apagar-medo-de-errar.md`

Páginas criadas:
- `pessoal/sources/2026-05-17-apagar-medo-de-errar.md`
- `pessoal/concepts/medo-de-errar.md`
- `pessoal/concepts/zona-de-conforto.md`
- `pessoal/entities/autores/cultura-renegada.md`

Páginas atualizadas:
- `pessoal/concepts/mecanismo-de-protecao-cerebral.md` — adicionada conexão com medo-de-errar
- `pessoal/concepts/dedicacao-vs-talento.md` — adicionada citação sobre perfeição vs. empenho
- `_meta/index.md`

---

## [2026-05-17] ingest | Não ignore a manutenção da sua vida (Pinho, YouTube)

Fonte: `raw/pessoal/2026-05-17-nao-ignore-a-manutencao-da-sua-vida.md`

Páginas criadas:
- `pessoal/sources/2026-05-17-nao-ignore-a-manutencao-da-sua-vida.md`
- `pessoal/concepts/manutencao-da-vida.md`
- `pessoal/concepts/conquista-vs-manutencao.md`
- `pessoal/entities/autores/pinho.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/connections.md`

Conexões registradas:
- `pessoal/manutencao-da-vida` ↔ `tecnico/autovacuum`: negligência com juros compostos é o mesmo problema que o PostgreSQL resolve com autovacuum
- `pessoal/conquista-vs-manutencao` ↔ `tecnico/trabalho-alavancado`: manutenção de hábitos como trabalho alavancado pessoal

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

## [2026-05-17] ingest | Discurso de formatura em Stanford — Steve Jobs (2005)

Fonte: `raw/pessoal/2005-06-12-the-pain-of-becoming-yourself-steve-jobs.md`
YouTube: https://www.youtube.com/watch?v=QYAnJ_QyCQg (canal "whoisalastair")

Páginas criadas:
- `pessoal/sources/2005-06-12-discurso-stanford-steve-jobs.md`
- `pessoal/concepts/conectar-os-pontos.md`
- `pessoal/concepts/memento-mori.md`
- `pessoal/concepts/vocacao.md`
- `pessoal/entities/autores/steve-jobs.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/connections.md`
- `_meta/log.md`

Conexões registradas em `_meta/connections.md`:
- vocação ↔ trabalho-alavancado (pessoal ↔ tecnico): amor genuíno pelo trabalho como condição para multiplicar impacto
- memento-mori ↔ discernimento espiritual (pessoal ↔ espiritual): paralelo entre clareza estóica da morte e perspectiva cristã da eternidade

---

## [2026-05-17] ingest | Harness Engineering é o próximo passo (Waldemar Neto - Dev Lab)

Fonte: YouTube — https://www.youtube.com/watch?v=dLs-Pbn8stU

Páginas criadas:
- `tecnico/sources/2026-05-17-harness-engineering-waldemar-neto.md`
- `tecnico/concepts/harness-engineering.md`
- `tecnico/concepts/feed-forward.md`
- `tecnico/concepts/multi-agent-orchestration.md`
- `tecnico/concepts/spec-driven.md` (stub)
- `tecnico/entities/autores/waldemar-neto.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/log.md`
- `_meta/connections.md`

Destaques do ingest:
- Harness como conceito unificador: o ambiente operacional ao redor do modelo é o que transforma LLM em agente confiável
- Distinção feed forward / feedback vinda da engenharia de controle — útil para avaliar qualquer framework de agentes
- As 6 falhas documentadas pela Anthropic são um checklist prático para auditar workflows com agentes
- Multi-agent orchestration com contratos explícitos é a peça que spec driven sozinho não cobre

---

## [2026-05-17] ingest | O segredo das pessoas confiantes (Luana Carolina)

Fonte: `raw/pessoal/2026-05-17-o-segredo-das-pessoas-confiantes.md`
URL: https://www.youtube.com/watch?v=0CpNy1Ph7e8

Páginas criadas:
- `pessoal/sources/2026-05-17-o-segredo-das-pessoas-confiantes.md`
- `pessoal/concepts/fingir-ate-se-tornar.md`
- `pessoal/concepts/auto-sabotagem.md`
- `pessoal/entities/autores/luana-carolina.md`

Páginas atualizadas:
- `_meta/index.md`
- `_meta/connections.md`

Conexões cross-domain registradas:
- `fingir-ate-se-tornar` ↔ `rafacho.dev`: processo de desenvolvimento de canal YouTube; stories como campo de treino
- `fingir-ate-se-tornar` ↔ `tecnico/concepts/trabalho-alavancado`: lógica de criar algo que gera retorno após o esforço inicial; o ponto de "naturalidade" como análogo ao leverage

---

## [2026-05-14 20:06] schema-update | Convenção de autores como entidade

- Subpasta `entities/autores/` adicionada em todos os domínios (tecnico, pessoal, espiritual, estudos, empresarial, rafacho.dev)
- Frontmatter estendido para autores: `entity_tipo`, `area`, `formacao`, `nacionalidade`, `link_principal`
- Regras de lar canônico e cross-domain definidas no `CLAUDE.md`
- No ingest, stub em `entities/autores/` criado automaticamente quando fonte tem campo `autor` sem página correspondente
- `_meta/index.md` atualizado: seção "Entidades" de cada domínio subdivida em "Autores" e "Outras"

---

## [2026-07-14] ingest | How Django can handle 100 millions of requests per day (Nicolae Godina)

Fonte: `raw/tecnico/2026-07-14 How Django can handle 100 millions of requests per day.md`
URL: https://medium.com/ebs-integrator/how-django-can-handle-100-millions-of-requests-per-day-c4cdbf48639e

Páginas criadas:
- `tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia.md`
- `tecnico/entities/docker.md`
- `tecnico/entities/kubernetes.md`
- `tecnico/entities/autores/nicolae-godina.md` (stub)
- `tecnico/concepts/n-plus-1-queries.md` (estava criado como stub vazio por ingest anterior; populado agora)
- `tecnico/concepts/conexoes-persistentes.md`
- `tecnico/concepts/operacoes-em-lote.md`
- `tecnico/concepts/reducao-de-transferencia-de-dados.md`

Páginas atualizadas:
- `tecnico/entities/django.md` — nova seção sobre infraestrutura e conexões persistentes; frontmatter `fontes` ampliado
- `tecnico/entities/postgresql.md` — seção sobre gestão de índices e pghero; frontmatter `fontes` ampliado
- `_meta/index.md`
- `_meta/log.md`

Destaques do ingest:
- Ênfase diferente da fonte irmã ([[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]]): infraestrutura (Docker/Kubernetes, monitoramento proativo) tratada como primeira preocupação, não complemento
- `CONN_MAX_AGE` com caso real documentado: corte de 50% na carga do banco, permitindo downgrade de instância AWS Aurora
- Meta de latência concreta: 100ms por endpoint, 20ms por query
- `tecnico/concepts/n-plus-1-queries.md` existia como arquivo vazio (stub sem conteúdo) desde um ingest anterior incompleto na mesma sessão; populado com conteúdo real a partir desta fonte


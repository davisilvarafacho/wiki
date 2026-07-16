---
title: "Índice Global"
tipo: meta
criado: 2026-05-14
atualizado: 2026-07-16
---

# Índice Global

Catálogo de todas as páginas da wiki, agrupado por domínio. Este arquivo é o ponto de partida para qualquer query — leia daqui, navegue para os domínios.

> **Manutenção:** atualizado a cada ingest. Mantenha em ordem alfabética dentro de cada categoria.

---

## Domínios

- [[tecnico/_index]] — programação, arquitetura, devops, decisões técnicas
- [[pessoal/_index]] — metas, reflexões, hábitos, journal, autocompreensão
- [[espiritual/_index]] — estudos bíblicos, teologia, sermões, devocional
- [[estudos/_index]] — livros, cursos, artigos, palestras
- [[empresarial/_index]] — FortePlus, Zettabyte, wCommanda, gestão, produto
- [[rafacho.dev/_index]] — canal do YouTube: aprendizado do ofício + produção

## Camada transversal

- [[_meta/connections]] — conexões entre domínios
- [[_meta/glossary]] — termos e convenções
- [[_meta/open-questions]] — perguntas abertas a investigar
- [[_meta/log]] — log cronológico

---

## Técnico

### Conceitos
- [[tecnico/concepts/anycast]] — técnica de roteamento onde múltiplos servidores compartilham o mesmo IP; BGP roteia para o mais próximo; base dos root DNS servers e CDNs
- [[tecnico/concepts/async-task-pattern]] — request → queue → worker → state store → polling; desacopla recebimento do pedido da execução lenta; mesmo padrão do Celery
- [[tecnico/concepts/event-sourcing]] — padrão arquitetural onde eventos imutáveis são persistidos no lugar do estado; o estado é derivado reaplicando os eventos; base do Datomic e do Nubank
- [[tecnico/concepts/imutabilidade]] — dados não mudam depois de criados; elimina bugs de estado compartilhado; fundação da programação funcional e do Event Sourcing
- [[tecnico/concepts/programacao-funcional]] — paradigma baseado em imutabilidade e ausência de side effects; decompõe sistemas complexos em funções puras e composíveis
- [[tecnico/concepts/side-effects]] — ações que uma função faz além de retornar um valor; em programação funcional são explicitados e empurrados para a periferia do sistema
- [[tecnico/concepts/autovacuum]] — processo automático de remoção de dead tuples no PostgreSQL; vulnerável a transações longas
- [[tecnico/concepts/caching]] — guardar resultado de operação cara em memória/storage rápido; memcached/redis são efêmeros; configurável por site, view ou fragmento
- [[tecnico/concepts/churn-codebase]] — alta taxa de modificações numa área do código como smell de complexidade crescente e dívida técnica iminente
- [[tecnico/concepts/conexoes-persistentes]] — reaproveitar conexões de banco entre requests via `CONN_MAX_AGE` no Django; caso real de corte de 50% na carga do banco
- [[tecnico/concepts/desnormalizacao]] — armazenar redundância proposital para evitar recálculo; troca custo de leitura por manutenção; último recurso
- [[tecnico/concepts/dns]] — Domain Name System; traduz nomes de domínio em IPs; hierarquia root → TLD → authoritative; resolução recursiva com caching por TTL
- [[tecnico/concepts/envoy-control-plane]] — servidor de gerenciamento que distribui configuração dinâmica para frotas de proxies Envoy via protocolo xDS; sem restart
- [[tecnico/concepts/feed-forward]] — mecanismo preventivo (feed forward) e corretivo (feedback/sensores) da engenharia de controle aplicado a agentes de IA
- [[tecnico/concepts/glue-records]] — registros A/AAAA incluídos fora da zona autoritativa para quebrar dependência circular quando o name server está dentro do próprio domínio
- [[tecnico/concepts/harness-engineering]] — ambiente operacional ao redor do LLM; transforma modelo poderoso em agente confiável; feed forward + sensores + memória + orquestração
- [[tecnico/concepts/hot-update]] — HOT (Heap-Only Tuple): otimização PostgreSQL que evita atualização de índices quando nova versão cabe na mesma página
- [[tecnico/concepts/llm-wiki]] — padrão de wiki pessoal mantida por LLM; conhecimento compilado incrementalmente
- [[tecnico/concepts/multi-agent-orchestration]] — agente implementador e agente validador em processos separados; neutralidade garantida por missões opostas
- [[tecnico/concepts/mvcc]] — Multi-Version Concurrency Control; múltiplas versões físicas por linha lógica para concorrência sem locks
- [[tecnico/concepts/n-plus-1-queries]] — padrão ineficiente de 1 query + N queries relacionadas; resolvido no Django com `select_related`/`prefetch_related`
- [[tecnico/concepts/operacoes-em-lote]] — agrupar inserts/updates em queries únicas (`bulk_create`/`bulk_update`) em vez de uma por objeto
- [[tecnico/concepts/particionamento-de-tabelas]] — dividir tabela grande em partes menores (ex: por período); nativo no Postgres 10+; combinar com réplicas de leitura
- [[tecnico/concepts/platform-engineering]] — disciplina de construir plataformas internas self-service que centralizam concerns transversais e multiplicam produtividade dos times de produto
- [[tecnico/concepts/rag]] — Retrieval-Augmented Generation; re-derivação de conhecimento por query
- [[tecnico/concepts/reducao-de-transferencia-de-dados]] — minimizar dados buscados do banco (`.only()`/`.defer()`) e devolvidos pela API; custo escala com volume de requests
- [[tecnico/concepts/sidecar-pattern]] — processo auxiliar colocado ao lado de um processo principal para estender comportamento sem modificar seu código; base de service mesh
- [[tecnico/concepts/spec-driven]] — metodologia de desenvolvimento com agentes onde a spec precede o código; é feed forward puro; stub
- [[tecnico/concepts/table-bloat]] — crescimento excessivo de tabelas por acúmulo de dead tuples; VACUUM regular não devolve espaço ao SO
- [[tecnico/concepts/tech-lead]] — papel de liderança técnica híbrido; direção técnica + crescimento do time + entrega
- [[tecnico/concepts/trabalho-alavancado]] — esforços que multiplicam capacidade do time muito depois de você ter seguido em frente
- [[tecnico/concepts/vimrag]] — Visual Memory RAG; evolução do VRAG com Grafo de Memória Multimodal para contextos visuais massivos; stub
- [[tecnico/concepts/vlm]] — Vision-Language Model; modelos que processam texto e imagens nativamente; base do VRAG; stub
- [[tecnico/concepts/vrag]] — VRAG (Visual RAG, Alibaba-NLP); RAG para dados visuais com VLMs, raciocínio iterativo agêntico e VRAG-RL

### Entidades

#### Autores
- [[tecnico/entities/autores/andy-pavlo]] — professor CMU, cofundador OtterTune; pesquisador de MVCC e sistemas de BD
- [[tecnico/entities/autores/dhruv-prajapati]] — autor FreeCodeCamp; artigos sobre redes e infraestrutura web
- [[tecnico/entities/autores/josh-hornby]] — engenheiro e escritor; série "Tech Lead Series" com conselhos práticos de liderança técnica
- [[tecnico/entities/autores/nicolae-godina]] — 5 anos de Django em produção; ênfase em infraestrutura (Docker/Kubernetes) e conexões persistentes
- [[tecnico/entities/autores/tarek-eissa]] — autor Medium; compilação de técnicas de performance e escalabilidade em Django
- [[tecnico/entities/autores/vasilios-syrakis]] — engenheiro de plataforma; 8 anos Atlassian; construiu infra de edge com Envoy, OSB e sidecars em Rust
- [[tecnico/entities/autores/vini-pasquantonio]] — engenheiro brasileiro (pasquadev); YouTube sobre funcional, DDD e event sourcing; experiência com Scala na Alemanha
- [[tecnico/entities/autores/waldemar-neto]] — dev brasileiro, canal Dev Lab; criador de TLC Spec Driven e framework PBQ; foco em harness engineering

#### Outras
- [[tecnico/entities/alibaba-nlp]] — grupo de pesquisa em NLP/IA do Alibaba; autores do VRAG e VimRAG; série Qwen de VLMs
- [[tecnico/entities/celery]] — fila de tarefas assíncronas para Python; usada com Django para tirar I/O de terceiros do ciclo request-response
- [[tecnico/entities/clojure]] — linguagem funcional Lisp na JVM; imutabilidade por padrão; linguagem principal do Nubank
- [[tecnico/entities/datomic]] — banco de dados imutável; Event Sourcing nativo; nunca apaga histórico; usado pelo Nubank
- [[tecnico/entities/django]] — framework web Python; stack de backend principal do usuário; performance em escala
- [[tecnico/entities/docker]] — plataforma de containerização; base para orquestração via Kubernetes
- [[tecnico/entities/envoy-proxy]] — proxy open-source L4/L7 com API de configuração dinâmica (xDS); substitui load balancers proprietários; base de service meshes
- [[tecnico/entities/kubernetes]] — orquestrador de containers; réplicas, upgrade sem downtime, métricas por pod/nó
- [[tecnico/entities/nubank]] — maior banco digital da América Latina; 100M clientes; stack: Clojure + Datomic + Event Sourcing
- [[tecnico/entities/memex]] — dispositivo hipotético de Vannevar Bush (1945); precursor conceitual da wiki pessoal
- [[tecnico/entities/obsidian]] — editor markdown local; "IDE da wiki" no padrão LLM Wiki
- [[tecnico/entities/postgresql]] — DBMS relacional open-source; o mais popular para novas aplicações; MVCC append-only é seu maior problema
- [[tecnico/entities/qmd]] — motor de busca local BM25/vector para arquivos markdown

### Sumários de fontes
- [[tecnico/sources/2026-05-14-llm-wiki-karpathy]] — Andrej Karpathy: padrão LLM Wiki (documento fundacional desta wiki)
- [[tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]] — Andy Pavlo: crítica técnica da implementação de MVCC do PostgreSQL; 4 problemas estruturais
- [[tecnico/sources/2026-05-14-what-is-a-tech-lead]] — Josh Hornby: definição do papel de tech lead; três responsabilidades e multiplier test
- [[tecnico/sources/2026-05-15-how-dns-works]] — Dhruv Prajapati: funcionamento completo do DNS, da resolução hierárquica à propagação de domínios
- [[tecnico/sources/2026-05-17-harness-engineering-waldemar-neto]] — Waldemar Neto: harness engineering como próximo passo além de spec driven; 6 falhas de agentes, feed forward vs. feedback, multi-agent orchestration
- [[tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]] — Vasilios Syrakis: 8 anos de Atlassian; OSB + Envoy control plane + sidecars em Rust; churn, manutenção e mentoria
- [[tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]] — pasquadev: análise do case do Nubank com Clojure e Datomic; programação funcional, Event Sourcing e DDD como stack para sistemas de longa vida
- [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]] — Tarek Eissa: compilação de técnicas de performance em Django — N+1 queries, gunicorn, serializers DRF, paginação, índices, caching, Celery, particionamento, CDN, desnormalização
- [[tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]] — Nicolae Godina: infraestrutura (Docker/Kubernetes), conexões persistentes (CONN_MAX_AGE), operações em lote e redução de transferência de dados no Django

### Notas
- [[tecnico/notes/2026-05-18-vrag-alibaba]] — nota derivada de conversa com Qwen 3.6 Plus; como funciona o VRAG do Alibaba (Visual RAG, raciocínio iterativo, VRAG-RL, VimRAG)

### Sínteses
*(vazio)*

---

## Pessoal

### Conceitos
- [[pessoal/concepts/alexitimia]] — dificuldade de identificar e nomear as próprias emoções; tornando-se condição quase geracional pela privação de silêncio
- [[pessoal/concepts/auto-sabotagem]] — tendência de se tornar o próprio obstáculo antes de qualquer crítica externa; o cancelamento começa por dentro
- [[pessoal/concepts/conectar-os-pontos]] — só é possível ligar experiências passadas em retrospecto; confiança no processo como condição para seguir o coração
- [[pessoal/concepts/medo-de-errar]] — errar como custo de transformação, não oposto de vencer; o verdadeiro fracasso é nunca se arriscar
- [[pessoal/concepts/conquista-vs-manutencao]] — distinção entre conquistar (ponto de partida) e manter (trabalho permanente que sustenta o que foi construído)
- [[pessoal/concepts/cortex-cingulado-anterior-dorsal]] — dACC: estrutura cerebral que regula esforço e disciplina; só cresce diante de desafios reais, nunca de prazer
- [[pessoal/concepts/dedicacao-vs-talento]] — dificuldade diminui na proporção exata da dedicação; talento é interesse aplicado por tempo suficiente
- [[pessoal/concepts/dessensibilizacao-dopaminergica]] — superestimulação crônica deregula receptores de dopamina; o mundo real perde o brilho; apatia persistente sem causa aparente
- [[pessoal/concepts/dopamina]] — neurotransmissor da antecipação (não do prazer); liberado antes da recompensa, na expectativa; base do vício em scroll
- [[pessoal/concepts/economia-da-atencao]] — modelo econômico em que atenção é produto; tédio transformado em problema de engajamento; projetado para eliminar o silêncio
- [[pessoal/concepts/efeito-bannister]] — acreditar que algo é possível como pré-condição para que se torne possível; nome a partir do recorde de Roger Bannister
- [[pessoal/concepts/fingir-ate-se-tornar]] — performar antes de ser natural como mecanismo real de desenvolvimento; o atrito e a sensação de impostor são constitutivos do processo
- [[pessoal/concepts/foco]] — habilidade neuroplástica, não talento; atenção oscila em ondas (noradrenalina); consolidação via potencial de longa duração (LTP)
- [[pessoal/concepts/gratidao]] — reconhecimento ativo do que existe agora, antes do próximo capítulo chegar; postura de percepção, não contentamento ingênuo
- [[pessoal/concepts/manutencao-da-vida]] — princípio central: tudo que é valioso exige cuidado contínuo; negligência tem juros compostos
- [[pessoal/concepts/mentalidade-de-temporada]] — temporada atual é teste, não destino; dificuldade forma para sustentar o que vem depois
- [[pessoal/concepts/mecanismo-de-protecao-cerebral]] — o cérebro trata o novo como perigo evolutivo; a "voz que manda desistir" é defesa primitiva, não intuição
- [[pessoal/concepts/habito-de-reclamacao]] — narrativa herdada de que "X é difícil" absorvida antes de tentar; amplifica o sinal do mecanismo de proteção cerebral
- [[pessoal/concepts/memento-mori]] — consciência da mortalidade como filtro do essencial; dissolve o ruído de expectativas externas e medo de perda
- [[pessoal/concepts/modo-do-todo-mundo]] — Heidegger: viver no automático do que "todo mundo" faz, sem nunca ter escolhido; tédio profundo é quando essa casca racha
- [[pessoal/concepts/novidade-vs-dificuldade]] — distinção entre dificuldade percebida (novidade + defesa cerebral) e dificuldade real; base do mindset de aprendizado
- [[pessoal/concepts/postura-de-curiosidade]] — entrar em território novo com "vamos ver no que vai dar" em vez de resistência; antídoto direto ao hábito de reclamação
- [[pessoal/concepts/ocio]] — pausa deliberada para pensar e se conhecer; na Grécia antiga (escolé) era o ponto alto da vida; hoje foi transformado em pecado
- [[pessoal/concepts/paciencia-ativa]] — paciência que não é espera passiva, mas preparação consciente e aproveitamento máximo do presente enquanto o próximo capítulo não chega
- [[pessoal/concepts/protocolo-de-foco-diario]] — protocolo prático de ~15 min em dias alternados: manhã de baixa dopamina, treino interoceptivo, eliminação de estímulos, foco sustentado, pausas estratégicas
- [[pessoal/concepts/reforco-por-razao-variavel]] — padrão de recompensa imprevisível é o mais viciante; base do design de cassinos e feeds; o cérebro não para porque não consegue prever a próxima recompensa
- [[pessoal/concepts/scroll-infinito]] — mecanismo de interface que elimina sinal de fim; combina tigela sem fundo com reforço variável; desperdiça 1 milhão de vidas/dia segundo seu criador
- [[pessoal/concepts/sistemas-vs-metas]] — vencedores e perdedores compartilham a meta; a diferença é o sistema de treino diário que protege o comportamento
- [[pessoal/concepts/tecnica-do-nao-zero]] — disciplina se constrói nos dias ruins; se não tem energia faça fácil, se não tem tempo faça curto, mas não deixe de fazer
- [[pessoal/concepts/vocacao]] — encontro entre o que se faz e o que se ama; o que sustenta nos momentos de colapso externo
- [[pessoal/concepts/autodisciplina]] — libertação, não privação; autocomando independente de motivação; a vida sem disciplina é servidão às próprias compulsões
- [[pessoal/concepts/pensamento-retrospectivo]] — planejar de trás para frente a partir do objetivo; baseado em evidência própria, não em intenção
- [[pessoal/concepts/rituais-de-iniciacao]] — sequência pré-definida que leva até o ponto de partida da tarefa; planejar como começar, não como fazer tudo
- [[pessoal/concepts/zona-de-conforto]] — mantém preso em versão menor de si mesmo; nunca transformou ninguém; sair exige agir antes de estar pronto

### Entidades

#### Autores
- [[pessoal/entities/autores/byung-chul-han]] — filósofo sul-coreano/alemão; "sociedade da autoexploração"; citado (não ingerido diretamente), stub
- [[pessoal/entities/autores/cultura-renegada]] — canal brasileiro de YouTube Shorts; conteúdo motivacional sobre mindset, medo de errar e zona de conforto
- [[pessoal/entities/autores/for-purpose-driven-men]] — canal YouTube; conteúdo motivacional cristão para homens; foco em propósito e perseverança
- [[pessoal/entities/autores/gabriel-tortela]] — psicólogo clínico, PhD em neurociência (USP); disciplina como músculo neural (dACC), procrastinação
- [[pessoal/entities/autores/jose-ricardo-gois]] — Dr. José Ricardo Gois; psicologia e filosofia aplicada; autoconhecimento, ócio, alexitimia e economia da atenção
- [[pessoal/entities/autores/luana-carolina]] — criadora de conteúdo brasileira; desenvolvimento pessoal, comunicação e presença digital
- [[pessoal/entities/autores/pinho]] — criador de conteúdo brasileiro; desenvolvimento pessoal, minimalismo, hábitos e finanças pessoais
- [[pessoal/entities/autores/natalia-persico]] — criadora de conteúdo; foco em autodisciplina, hábitos e desenvolvimento pessoal
- [[pessoal/entities/autores/reservatorio-de-dopamina]] — canal brasileiro de neurociência popular; foco, dopamina e atenção
- [[pessoal/entities/autores/steve-jobs]] — cofundador Apple, NeXT e Pixar; referência em vocação, design e visão de vida

#### Outras
*(vazio)*

### Sumários de fontes
- [[pessoal/sources/2005-06-12-discurso-stanford-steve-jobs]] — Steve Jobs: três histórias sobre conectar pontos, amor e perda, e a morte como ferramenta (Stanford, 2005)
- [[pessoal/sources/2026-05-17-apagar-medo-de-errar]] — Cultura Renegada: errar como custo de transformação; zona de conforto como prisão; coragem do primeiro passo
- [[pessoal/sources/2026-05-17-nada-e-dificil-so-e-novo]] — Pinho: "Nada é difícil, só é novo pra você"; mecanismo cerebral de defesa, hábito de reclamação e dedicação como transformadora
- [[pessoal/sources/2026-05-17-este-video-vai-te-encontrar]] — emmy: paciência ativa; fazer o máximo do presente enquanto aguarda o próximo capítulo; gratidão e sonho com intenção
- [[pessoal/sources/2026-05-17-nao-ignore-a-manutencao-da-sua-vida]] — Pinho: manutenção como princípio de vida; conquista é só o começo; negligência tem juros
- [[pessoal/sources/2026-06-03-give-god-56-seconds]] — For Purpose Driven Men: temporada atual como teste formativo; grit e disciplina se constroem na adversidade
- [[pessoal/sources/2026-06-03-o-tedio-e-a-saida-dos-seus-problemas]] — Dr. José Ricardo Gois: ócio deliberado como porta do autoconhecimento; alexitimia, economia da atenção e modo do todo mundo
- [[pessoal/sources/2026-06-03-o-mecanismo-que-esta-quebrando-seu-cerebro]] — Dr. José Ricardo Gois: scroll infinito, dopamina de antecipação, reforço variável e dessensibilização dopaminérgica
- [[pessoal/sources/2026-05-17-o-segredo-das-pessoas-confiantes]] — Luana Carolina: o custo de fazer algo antes de ser bom; fingir até se tornar; auto-sabotagem interna
- [[pessoal/sources/2026-05-26-domine-a-autodisciplina-7-habitos]] — Natalia Persico: autodisciplina como autocomando; 7 hábitos práticos incluindo rituais de iniciação e pensamento retrospectivo
- [[pessoal/sources/2026-07-14-foco-imparavel-reservatorio-dopamina]] — Reservatório de Dopamina: foco como habilidade neuroplástica; paradoxo renascentista, oscilação atencional (noradrenalina), LTP, efeito Bannister e protocolo prático de treino
- [[pessoal/sources/2026-07-16-melhor-tecnica-disciplina-neurocientista]] — Gabriel Tortela: disciplina como músculo (dACC); técnica "1, 2, 3, já", técnica do não-zero, sistemas vs. metas

### Notas
*(vazio)*

### Sínteses
*(vazio)*

---

## Espiritual

### Conceitos
*(vazio)*

### Entidades

#### Autores
*(vazio)*

#### Outras
*(vazio)*

### Sumários de fontes
*(vazio)*

### Notas
*(vazio)*

### Sínteses
*(vazio)*

---

## Estudos

### Conceitos
- [[estudos/concepts/carga-cognitiva]] — recurso mental limitado; ladrões silenciosos: música com letra, celular visível, sono ruim
- [[estudos/concepts/dificuldades-desejadas]] — paradoxo central do aprendizado: o esforço que parece atrapalhar é o que consolida
- [[estudos/concepts/ilusao-do-aprendizado]] — releitura gera familiaridade, não retenção; reconhecimento não é recuperação
- [[estudos/concepts/pratica-com-recuperacao]] — feche o material e tente lembrar; flashcards, questões, ensinar alguém; técnica mais eficaz
- [[estudos/concepts/pratica-espacada]] — revisitar de tempos em tempos; esquecimento é fisiológico; intervalos crescentes fortalecem retenção

### Entidades

#### Autores
- [[estudos/entities/autores/emmanuel-nominato]] — criador de conteúdo; foco em técnicas de estudo com base científica

#### Outras
*(vazio)*

### Sumários de fontes
- [[estudos/sources/2026-05-17-estudar-10x-melhor-emmanuel-nominato]] — Emmanuel Nominato: base do aprendizado (atenção, sono, distrações) + técnicas com base científica

### Notas
*(vazio)*

### Sínteses
*(vazio)*

---

## Empresarial

### Conceitos
*(vazio)*

### Entidades

#### Autores
*(vazio)*

#### Outras
*(vazio)*

### Sumários de fontes
*(vazio)*

### Notas
*(vazio)*

### Sínteses
*(vazio)*

---

## rafacho.dev

### Conceitos
*(vazio)*

### Entidades

#### Autores
*(vazio)*

#### Outras
*(vazio)*

### Sumários de fontes
*(vazio)*

### Notas
*(vazio)*

### Sínteses
*(vazio)*

### Produção

#### Ideias
*(vazio)*

#### Roteiros
*(vazio)*

#### Publicados
*(vazio)*

#### Métricas
*(vazio)*

#### Planejamento
*(vazio)*

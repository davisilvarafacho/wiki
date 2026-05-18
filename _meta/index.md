---
title: "Índice Global"
tipo: meta
criado: 2026-05-14
atualizado: 2026-05-14
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
- [[tecnico/concepts/autovacuum]] — processo automático de remoção de dead tuples no PostgreSQL; vulnerável a transações longas
- [[tecnico/concepts/dns]] — Domain Name System; traduz nomes de domínio em IPs; hierarquia root → TLD → authoritative; resolução recursiva com caching por TTL
- [[tecnico/concepts/feed-forward]] — mecanismo preventivo (feed forward) e corretivo (feedback/sensores) da engenharia de controle aplicado a agentes de IA
- [[tecnico/concepts/glue-records]] — registros A/AAAA incluídos fora da zona autoritativa para quebrar dependência circular quando o name server está dentro do próprio domínio
- [[tecnico/concepts/harness-engineering]] — ambiente operacional ao redor do LLM; transforma modelo poderoso em agente confiável; feed forward + sensores + memória + orquestração
- [[tecnico/concepts/hot-update]] — HOT (Heap-Only Tuple): otimização PostgreSQL que evita atualização de índices quando nova versão cabe na mesma página
- [[tecnico/concepts/llm-wiki]] — padrão de wiki pessoal mantida por LLM; conhecimento compilado incrementalmente
- [[tecnico/concepts/multi-agent-orchestration]] — agente implementador e agente validador em processos separados; neutralidade garantida por missões opostas
- [[tecnico/concepts/mvcc]] — Multi-Version Concurrency Control; múltiplas versões físicas por linha lógica para concorrência sem locks
- [[tecnico/concepts/rag]] — Retrieval-Augmented Generation; re-derivação de conhecimento por query
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
- [[tecnico/entities/autores/waldemar-neto]] — dev brasileiro, canal Dev Lab; criador de TLC Spec Driven e framework PBQ; foco em harness engineering

#### Outras
- [[tecnico/entities/alibaba-nlp]] — grupo de pesquisa em NLP/IA do Alibaba; autores do VRAG e VimRAG; série Qwen de VLMs
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

### Notas
- [[tecnico/notes/2026-05-18-vrag-alibaba]] — nota derivada de conversa com Qwen 3.6 Plus; como funciona o VRAG do Alibaba (Visual RAG, raciocínio iterativo, VRAG-RL, VimRAG)

### Sínteses
*(vazio)*

---

## Pessoal

### Conceitos
- [[pessoal/concepts/auto-sabotagem]] — tendência de se tornar o próprio obstáculo antes de qualquer crítica externa; o cancelamento começa por dentro
- [[pessoal/concepts/conectar-os-pontos]] — só é possível ligar experiências passadas em retrospecto; confiança no processo como condição para seguir o coração
- [[pessoal/concepts/medo-de-errar]] — errar como custo de transformação, não oposto de vencer; o verdadeiro fracasso é nunca se arriscar
- [[pessoal/concepts/conquista-vs-manutencao]] — distinção entre conquistar (ponto de partida) e manter (trabalho permanente que sustenta o que foi construído)
- [[pessoal/concepts/dedicacao-vs-talento]] — dificuldade diminui na proporção exata da dedicação; talento é interesse aplicado por tempo suficiente
- [[pessoal/concepts/fingir-ate-se-tornar]] — performar antes de ser natural como mecanismo real de desenvolvimento; o atrito e a sensação de impostor são constitutivos do processo
- [[pessoal/concepts/gratidao]] — reconhecimento ativo do que existe agora, antes do próximo capítulo chegar; postura de percepção, não contentamento ingênuo
- [[pessoal/concepts/manutencao-da-vida]] — princípio central: tudo que é valioso exige cuidado contínuo; negligência tem juros compostos
- [[pessoal/concepts/mecanismo-de-protecao-cerebral]] — o cérebro trata o novo como perigo evolutivo; a "voz que manda desistir" é defesa primitiva, não intuição
- [[pessoal/concepts/memento-mori]] — consciência da mortalidade como filtro do essencial; dissolve o ruído de expectativas externas e medo de perda
- [[pessoal/concepts/novidade-vs-dificuldade]] — distinção entre dificuldade percebida (novidade + defesa cerebral) e dificuldade real; base do mindset de aprendizado
- [[pessoal/concepts/paciencia-ativa]] — paciência que não é espera passiva, mas preparação consciente e aproveitamento máximo do presente enquanto o próximo capítulo não chega
- [[pessoal/concepts/vocacao]] — encontro entre o que se faz e o que se ama; o que sustenta nos momentos de colapso externo
- [[pessoal/concepts/zona-de-conforto]] — mantém preso em versão menor de si mesmo; nunca transformou ninguém; sair exige agir antes de estar pronto

### Entidades

#### Autores
- [[pessoal/entities/autores/cultura-renegada]] — canal brasileiro de YouTube Shorts; conteúdo motivacional sobre mindset, medo de errar e zona de conforto
- [[pessoal/entities/autores/luana-carolina]] — criadora de conteúdo brasileira; desenvolvimento pessoal, comunicação e presença digital
- [[pessoal/entities/autores/pinho]] — criador de conteúdo brasileiro; desenvolvimento pessoal, minimalismo, hábitos e finanças pessoais
- [[pessoal/entities/autores/steve-jobs]] — cofundador Apple, NeXT e Pixar; referência em vocação, design e visão de vida

#### Outras
*(vazio)*

### Sumários de fontes
- [[pessoal/sources/2005-06-12-discurso-stanford-steve-jobs]] — Steve Jobs: três histórias sobre conectar pontos, amor e perda, e a morte como ferramenta (Stanford, 2005)
- [[pessoal/sources/2026-05-17-apagar-medo-de-errar]] — Cultura Renegada: errar como custo de transformação; zona de conforto como prisão; coragem do primeiro passo
- [[pessoal/sources/2026-05-17-nada-e-dificil-so-e-novo]] — Pinho: "Nada é difícil, só é novo pra você"; mecanismo cerebral de defesa, hábito de reclamação e dedicação como transformadora
- [[pessoal/sources/2026-05-17-este-video-vai-te-encontrar]] — emmy: paciência ativa; fazer o máximo do presente enquanto aguarda o próximo capítulo; gratidão e sonho com intenção
- [[pessoal/sources/2026-05-17-nao-ignore-a-manutencao-da-sua-vida]] — Pinho: manutenção como princípio de vida; conquista é só o começo; negligência tem juros
- [[pessoal/sources/2026-05-17-o-segredo-das-pessoas-confiantes]] — Luana Carolina: o custo de fazer algo antes de ser bom; fingir até se tornar; auto-sabotagem interna

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
*(vazio)*

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

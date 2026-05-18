---
title: "Índice Global"
tipo: meta
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
- [[tecnico/concepts/glue-records]] — registros A/AAAA incluídos fora da zona autoritativa para quebrar dependência circular quando o name server está dentro do próprio domínio
- [[tecnico/concepts/hot-update]] — HOT (Heap-Only Tuple): otimização PostgreSQL que evita atualização de índices quando nova versão cabe na mesma página
- [[tecnico/concepts/llm-wiki]] — padrão de wiki pessoal mantida por LLM; conhecimento compilado incrementalmente
- [[tecnico/concepts/mvcc]] — Multi-Version Concurrency Control; múltiplas versões físicas por linha lógica para concorrência sem locks
- [[tecnico/concepts/rag]] — Retrieval-Augmented Generation; re-derivação de conhecimento por query
- [[tecnico/concepts/table-bloat]] — crescimento excessivo de tabelas por acúmulo de dead tuples; VACUUM regular não devolve espaço ao SO
- [[tecnico/concepts/tech-lead]] — papel de liderança técnica híbrido; direção técnica + crescimento do time + entrega
- [[tecnico/concepts/trabalho-alavancado]] — esforços que multiplicam capacidade do time muito depois de você ter seguido em frente

### Entidades

#### Autores
- [[tecnico/entities/autores/andy-pavlo]] — professor CMU, cofundador OtterTune; pesquisador de MVCC e sistemas de BD
- [[tecnico/entities/autores/dhruv-prajapati]] — autor FreeCodeCamp; artigos sobre redes e infraestrutura web
- [[tecnico/entities/autores/josh-hornby]] — engenheiro e escritor; série "Tech Lead Series" com conselhos práticos de liderança técnica

#### Outras
- [[tecnico/entities/memex]] — dispositivo hipotético de Vannevar Bush (1945); precursor conceitual da wiki pessoal
- [[tecnico/entities/obsidian]] — editor markdown local; "IDE da wiki" no padrão LLM Wiki
- [[tecnico/entities/postgresql]] — DBMS relacional open-source; o mais popular para novas aplicações; MVCC append-only é seu maior problema
- [[tecnico/entities/qmd]] — motor de busca local BM25/vector para arquivos markdown

### Sumários de fontes
- [[tecnico/sources/2026-05-14-llm-wiki-karpathy]] — Andrej Karpathy: padrão LLM Wiki (documento fundacional desta wiki)
- [[tecnico/sources/2026-05-14-postgresql-mvcc-the-part-we-hate-the-most]] — Andy Pavlo: crítica técnica da implementação de MVCC do PostgreSQL; 4 problemas estruturais
- [[tecnico/sources/2026-05-14-what-is-a-tech-lead]] — Josh Hornby: definição do papel de tech lead; três responsabilidades e multiplier test
- [[tecnico/sources/2026-05-15-how-dns-works]] — Dhruv Prajapati: funcionamento completo do DNS, da resolução hierárquica à propagação de domínios

### Notas
*(vazio)*

### Sínteses
*(vazio)*

---

## Pessoal

### Conceitos
- [[pessoal/concepts/dedicacao-vs-talento]] — dificuldade diminui na proporção exata da dedicação; talento é interesse aplicado por tempo suficiente
- [[pessoal/concepts/mecanismo-de-protecao-cerebral]] — o cérebro trata o novo como perigo evolutivo; a "voz que manda desistir" é defesa primitiva, não intuição
- [[pessoal/concepts/novidade-vs-dificuldade]] — distinção entre dificuldade percebida (novidade + defesa cerebral) e dificuldade real; base do mindset de aprendizado

### Entidades

#### Autores
- [[pessoal/entities/autores/pinho]] — criador de conteúdo brasileiro; desenvolvimento pessoal, minimalismo, organização de vida

#### Outras
*(vazio)*

### Sumários de fontes
- [[pessoal/sources/2026-05-17-nada-e-dificil-so-e-novo]] — Pinho: "Nada é difícil, só é novo pra você"; mecanismo cerebral de defesa, hábito de reclamação e dedicação como transformadora

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

---
title: "How Django can handle 100 millions of requests per day"
tipo: source
dominio: tecnico
url: "https://medium.com/ebs-integrator/how-django-can-handle-100-millions-of-requests-per-day-c4cdbf48639e"
autor: "Nicolae Godina"
publicado: 2020-07-21
capturado: 2026-07-14
tipo_fonte: blog-post
tags: [django, performance, escalabilidade, orm, infraestrutura, postgresql, kubernetes]
criado: 2026-07-14
atualizado: 2026-07-14
---

# How Django can handle 100 millions of requests per day

Recomendações de Nicolae Godina, com cinco anos de experiência em Django em produção, sobre como sustentar alto volume de requests. Foco mais equilibrado entre infraestrutura e código do que a compilação de Tarek Eissa (ver [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]]) — trata infraestrutura como primeira preocupação, não última.

## Sumário

- **Infraestrutura vem primeiro**: microserviços (atenção ao volume de dados trafegado entre eles — sincronização frequente aumenta custo), [[tecnico/entities/docker|Docker]] para empacotar e [[tecnico/entities/kubernetes|Kubernetes]] para orquestrar e controlar réplicas
- **Infraestrutura para manutenção**: deve permitir upgrade/downgrade de recursos sem downtime, e monitorar métricas específicas — requests por microserviço/endpoint, CPU por pod e por nó do cluster, tráfego de entrada/saída, CPU e uso de storage no banco — para manutenção proativa em vez de troubleshooting reativo
- **O banco é o culpado mais provável**: a velocidade de resposta de um endpoint normalmente é limitada pela query, não pelo código Python
- **Escolha de banco**: preferência do autor por [[tecnico/entities/postgresql|PostgreSQL]] por robustez e integridade de dados; priorizar storage rápido e CPU/IOPS na camada de dados
- **Índices**: criar todos os necessários, mas remover redundantes — cada índice acelera SELECT e penaliza INSERT/UPDATE; o Django ORM pode gerar índices que se repetem, exigindo checagem manual
- **Meta de latência**: endpoints devem responder em até 100ms, o que implica queries individuais em até 20ms
- **Debug logs do ORM**: ativar `django.db.backends` em `LOGGING` (nível DEBUG) para ver tempo de execução de cada query durante desenvolvimento
- **pghero**: dashboard de performance para PostgreSQL — identifica slow queries e índices duplicados
- **[[tecnico/concepts/conexoes-persistentes|Conexões persistentes]]**: Django fecha a conexão com o banco ao final de cada request por padrão; usar `CONN_MAX_AGE` evita reconectar a cada request. Caso relatado pelo autor: subir de 0 para 300s reduziu a carga do banco pela metade, permitindo downgrade de uma instância AWS Aurora `db.r5.8xlarge` para `db.r5.4xlarge`
- **Desativar apps e middlewares não usados**: `Sessions` e `Messages`, por exemplo, são desnecessários numa API REST pura — cada middleware a menos é um passo a menos por request
- **[[tecnico/concepts/operacoes-em-lote|Operações em lote]]**: usar bulk insert/update do ORM em vez de operações individuais; especificar `batch_size` ao inserir mais de 5000 objetos
- **`select_related`**: pré-carrega entidades relacionadas via JOIN, evitando N+1 queries (ver [[tecnico/concepts/n-plus-1-queries]]) — depende do tamanho das tabelas envolvidas, já que o ORM gera a query de JOIN
- **[[tecnico/concepts/reducao-de-transferencia-de-dados|Redução de transferência de dados]]**: `.only()`/`.defer()` no ORM para limitar colunas buscadas do banco; no lado da API, excluir campos não usados pelo cliente — exemplo do autor: resposta de 1KB × 1 milhão de chamadas/dia = 30GB/mês trafegados

## Citações relevantes

> "Whatever speed you gain via code execution you'll most probably lose at the database end."

> "After adjusting this parameter [CONN_MAX_AGE] from 0 to 300 seconds, I reduced the DB load in half."

> "Any extra milliseconds multiplied by millions of requests can lead to excessive consumption of resources. If the application is optimized or properly built, increasing hardware resources does not save the day."

## Takeaways

- Diferença de ênfase em relação à outra fonte sobre Django: este autor trata **infraestrutura e observabilidade** (Docker, Kubernetes, métricas de pod/nó, monitoramento proativo) como o primeiro pilar, não um complemento tardio — a outra fonte foca quase inteiramente em código/ORM
- `CONN_MAX_AGE` é apresentado com um caso real de impacto (queda de 50% na carga do banco, permitindo downgrade de hardware) — evidência concreta de que conexões persistentes têm ROI alto e barato de implementar
- A meta de latência (100ms por endpoint, 20ms por query) é um número prático e citável, raro em artigos desse tipo
- "Don't blame the piano — blame the pianist": o argumento central é que Django/Python raramente é o gargalo real; a disciplina de quem escreve o código e desenha a infraestrutura é que determina se a aplicação escala

## Páginas relacionadas

- [[tecnico/entities/django]] — atualizada com infraestrutura e conexões persistentes
- [[tecnico/entities/docker]] — entidade criada
- [[tecnico/entities/kubernetes]] — entidade criada
- [[tecnico/entities/postgresql]] — atualizada (pghero, gestão de índices)
- [[tecnico/entities/autores/nicolae-godina]] — autor criado (stub)
- [[tecnico/concepts/n-plus-1-queries]] — populado (estava stub vazio)
- [[tecnico/concepts/conexoes-persistentes]] — conceito criado
- [[tecnico/concepts/operacoes-em-lote]] — conceito criado
- [[tecnico/concepts/reducao-de-transferencia-de-dados]] — conceito criado
- [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]] — fonte irmã sobre o mesmo tema, ênfase diferente

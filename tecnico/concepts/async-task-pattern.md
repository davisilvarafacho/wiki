---
title: "Async Task Pattern"
tipo: concept
dominio: tecnico
tags: [arquitetura, filas, workers, async, backend]
fontes: [tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]
criado: 2026-05-24
atualizado: 2026-07-14
---

# Async Task Pattern

Padrão arquitetural para desacoplar o recebimento de um pedido da sua execução, quando a execução é lenta demais para caber no ciclo de vida de uma request HTTP síncrona.

## O fluxo

**request → queue → worker → state store → polling**

1. O servidor web recebe a request e, em vez de executar o trabalho, apenas a enfileira.
2. Um worker separado consome a fila e executa o trabalho de fato (potencialmente demorado: provisionamento de infraestrutura, chamadas a APIs de terceiros, processamento pesado).
3. O worker escreve o resultado num state store.
4. O cliente consulta o estado periodicamente (polling) até o trabalho ser concluído.

## Exemplo real

No Open Service Broker da Atlassian (ver [[tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]]), o padrão foi implementado com **SQS** como fila, um worker dedicado para executar tarefas de provisionamento (criar DNS records, distribuições CloudFront, configurar serviços AWS), e **DynamoDB** como state store — o web server lê o resultado ali durante o polling do cliente.

## Por que usar

- Evita que a request HTTP fique bloqueada esperando um trabalho longo terminar (timeout, conexão pendurada).
- Isola falhas: se o worker cair, a fila retém o pedido para retry.
- Permite escalar produtores (web servers) e consumidores (workers) independentemente.

## Ver também

- [[tecnico/entities/celery]] — implementação do mesmo padrão no ecossistema Django/Python (fila + workers assíncronos)
- [[tecnico/concepts/envoy-control-plane]] — outro padrão do mesmo ingest, também baseado em desacoplar mudança de estado da propagação

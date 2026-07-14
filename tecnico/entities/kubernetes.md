---
title: "Kubernetes"
tipo: entity
dominio: tecnico
tags: [containers, orquestracao, devops, infraestrutura]
fontes: [tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Kubernetes

*A ser preenchido quando houver fonte dedicada.*

Orquestrador de containers — controla número de réplicas, distribui carga, reinicia pods com falha e permite upgrade/downgrade de recursos sem downtime. Passo seguinte a [[tecnico/entities/docker|Docker]] numa infraestrutura pensada para escalar: containerização sozinha não resolve orquestração de múltiplas réplicas em produção.

## Uso citado

Em contexto de alta carga (ex: aplicações [[tecnico/entities/django|Django]] servindo dezenas de milhões de requests/dia), métricas por pod e por nó do cluster (CPU, tráfego) são citadas como essenciais para monitoramento proativo, não apenas troubleshooting reativo.

## Ver também

- [[tecnico/entities/docker]]
- [[tecnico/entities/django]]
- [[tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]]

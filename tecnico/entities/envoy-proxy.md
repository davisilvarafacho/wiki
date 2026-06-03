---
title: "Envoy Proxy"
tipo: entity
dominio: tecnico
tags: [proxy, networking, platform-engineering, open-source, cncf]
criado: 2026-06-03
atualizado: 2026-06-03
---

# Envoy Proxy

*A ser preenchido quando houver fonte/contexto dedicado.*

Proxy open-source L4/L7 desenvolvido originalmente pela Lyft, doado à CNCF. Similar ao Nginx em funcionalidade básica, mas com diferencial central: **API de configuração dinâmica (xDS)** que permite reconfigurar clusters, rotas, listeners e certificados em runtime sem restart.

## Características principais

- **xDS API**: protocolo de discovery (gRPC streaming) para receber configuração dinâmica do [[tecnico/concepts/envoy-control-plane]]
- **Recursos configuráveis**: listeners, routes, clusters (upstreams), endpoints
- **Filtros de rede extensíveis**: HTTP Connection Manager, ext_authz, ext_proc, rate limiting, access log
- **Observabilidade nativa**: métricas Prometheus, tracing (Zipkin/Jaeger/OTLP)

## Uso na Atlassian

Utilizado como proxy central de edge da Atlassian para substituir enterprise load balancers com custo de licença. ~2.000 instâncias em ~13 regiões AWS, provisionadas via CloudFormation usando AMI construída com Packer + SaltStack. Configuradas dinamicamente pelo control plane "Sovereign" — ver [[tecnico/concepts/envoy-control-plane]].

## Ver também

- [[tecnico/concepts/envoy-control-plane]]
- [[tecnico/concepts/sidecar-pattern]]
- [[tecnico/concepts/platform-engineering]]
- [[tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]]

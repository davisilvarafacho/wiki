---
title: "Envoy Control Plane (xDS)"
tipo: concept
dominio: tecnico
tags: [envoy, proxy, control-plane, xds, platform-engineering, configuracao-dinamica]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]
---

# Envoy Control Plane (xDS)

Padrão de gerenciamento dinâmico de configuração para frotas de proxies [[tecnico/entities/envoy-proxy]]. Em vez de arquivos de config estáticos que exigem restart, o controle plane serve a configuração via API (protocolo xDS — *discovery service*) e os proxies a consomem em tempo real. Mudanças de estado fluem do plano de controle para a frota sem downtime.

## O problema que resolve

Um proxy convencional tem configuração estática: para mudar algo (nova rota, novo cluster, novo certificado), é preciso atualizar o arquivo e reiniciar o processo. Em uma frota de milhares de proxies servindo tráfego real, isso é impraticável. O control plane elimina esse ciclo.

## Componentes

```
[Fontes de contexto]        [Control Plane]         [Proxies]
  banco de dados    ──────►  templates +  ──xDS──►   Envoy #1
  S3 / configs             contexto dinâmico         Envoy #2
  broker/OSB                                         Envoy #N
```

- **Fontes de contexto**: qualquer lugar com estado relevante — banco de dados do broker, buckets S3, resultados de provisionamento
- **Templates**: definem a estrutura dos recursos Envoy (clusters, routes, listeners); contêm lógica que combina template + contexto para produzir configuração válida
- **xDS API**: protocolo de discovery que o Envoy usa para solicitar recursos ao control plane; existem variantes: CDS (clusters), RDS (routes), LDS (listeners), EDS (endpoints)
- **Proxies**: consomem a config do control plane via streaming gRPC; atualizam-se em runtime sem restart

## Implementação na Atlassian — "Sovereign"

[[tecnico/entities/autores/vasilios-syrakis]] construiu e open-sourcou um control plane chamado **Sovereign** (disponível no Bitbucket). Implementado como FastAPI, recebia:
- Templates de recursos Envoy (clusters, routes, listeners) em formato de arquivo
- Contexto dinâmico do banco do OSB e de outros sources (S3)

Quando o contexto mudava (ex: novo serviço provisionado via [[tecnico/concepts/platform-engineering]]), o Sovereign renderizava novos recursos e os entregava aos proxies via xDS. Resultado: um dev enviava uma requisição de provisionamento ao broker, e em instantes a configuração chegava nos proxies sem nenhuma intervenção manual.

## Relação com o padrão de platform engineering

O control plane é o "cérebro" da frota de proxies em um setup de [[tecnico/concepts/platform-engineering]]: ele traduz intenção (o que o dev quer) em configuração concreta (o que o proxy faz). Esse nível de indireção é o que permite self-service — o dev declara o que quer, a plataforma implementa.

## Ver também

- [[tecnico/entities/envoy-proxy]]
- [[tecnico/concepts/platform-engineering]]
- [[tecnico/concepts/sidecar-pattern]]

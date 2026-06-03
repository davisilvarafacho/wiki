---
title: "Sidecar Pattern"
tipo: concept
dominio: tecnico
tags: [arquitetura, proxy, microservices, platform-engineering, envoy, rust]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]
---

# Sidecar Pattern

Padrão arquitetural onde um processo auxiliar (o *sidecar*) roda colocado ao lado de um processo principal no mesmo host/pod, estendendo seu comportamento sem modificar seu código. A comunicação entre os dois geralmente ocorre via rede local (localhost) ou socket.

O nome vem da analogia com o sidecar de motocicleta: o sidecar não dirige, mas acompanha e adiciona capacidade sem ser o veículo principal.

## Casos de uso típicos

- **Autenticação/Autorização**: o sidecar valida tokens antes de repassar a requisição ao processo principal
- **Rate limiting**: o sidecar conta e throttle requisições antes que cheguem ao destino
- **Observabilidade**: coleta de métricas, logs e traces sem instrumentar o código principal
- **TLS termination**: o sidecar gerencia certificados e descriptografa antes de repassar
- **Service mesh**: o padrão é a base do Istio, Linkerd e similares — cada serviço tem um proxy Envoy como sidecar

## Vantagens

- **Separação de concerns**: lógica ortogonal (segurança, observabilidade) fica fora do código de negócio
- **Poliglota**: sidecar pode ser escrito em qualquer linguagem, independente do serviço principal
- **Reuso**: o mesmo sidecar serve múltiplos serviços sem duplicação
- **Atualização independente**: sidecar pode ser versionado e atualizado sem tocar no serviço principal

## Desvantagens

- **Latência adicional**: hop extra em cada requisição
- **Complexidade operacional**: mais processos para monitorar, configurar e debugar
- **Consumo de recursos**: cada instância do serviço carrega também o sidecar

## Implementação na Atlassian

Na plataforma de edge da Atlassian, os proxies [[tecnico/entities/envoy-proxy]] rodam com sidecars para concerns que o proxy não implementa nativamente:

- **Autenticação**: sidecar em **Rust**, escrito por [[tecnico/entities/autores/vasilios-syrakis]] — Envoy delega a decisão de autenticação via *external processing* ou *external authorization* para este processo local
- **Autorização**: sidecar desenvolvido por outro time
- **Rate limiting**: sidecar desenvolvido por outro time

Os sidecars eram instalados na AMI via Packer + SaltStack durante o processo de build da imagem, e recebiam configuração dinâmica via wire local — mantendo o princípio de [[tecnico/concepts/envoy-control-plane]] de configuração sem restart.

A adição de novos sidecars é aditiva: não modifica o proxy principal nem os backends — exatamente o que o padrão propõe.

## Envoy e sidecars

Envoy oferece dois mecanismos de integração com sidecars:

- **ext_authz (external authorization)**: Envoy chama o sidecar para aprovar/negar cada requisição
- **ext_proc (external processing)**: sidecar pode inspecionar e modificar headers/body da requisição e resposta

Ambos tornam o proxy extensível sem precisar recompilar ou modificar o Envoy.

## Ver também

- [[tecnico/entities/envoy-proxy]]
- [[tecnico/concepts/envoy-control-plane]]
- [[tecnico/concepts/platform-engineering]]

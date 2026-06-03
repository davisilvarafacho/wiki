---
title: "Platform Engineering"
tipo: concept
dominio: tecnico
tags: [plataforma, self-service, devops, infraestrutura, centralização, produtividade]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]
---

# Platform Engineering

Disciplina de engenharia focada em construir e operar plataformas internas que aumentam a produtividade dos times de produto, eliminando fricção operacional e centralizando concerns transversais. A plataforma provê self-service: os desenvolvedores declaram o que precisam (via config, API ou arquivo versionado) e a plataforma entrega — sem precisar abrir chamado para um time de infra.

## O problema que resolve

Sem uma plataforma centralizada, cada time de produto precisa implementar por conta própria: autenticação, rate limiting, DoS protection, observabilidade, TLS, load balancing. Isso é redundância em escala:

- Mil times → mil implementações potencialmente inconsistentes de segurança
- Features de produto atrasam porque precisam reimplementar infraestrutura
- Quando uma vulnerabilidade aparece, precisa ser corrigida em mil lugares

A plataforma resolve isso uma vez. Depois, todos herdam automaticamente.

## Princípio da centralização no edge

Um dos padrões mais poderosos de platform engineering é interceptar concerns *antes* que as requisições cheguem aos backends:

```
[Cliente] → [Edge/Proxy] → [Backend A]
                       → [Backend B]
                       → [Backend C]
```

O edge (proxy central) aplica:
- Autenticação e autorização
- Rate limiting
- DoS protection
- Access logs
- TLS termination
- Roteamento avançado

Os backends ficam livres para focar em lógica de negócio. Quanto mais tarde um concern é tratado (quanto mais perto do backend), mais caro e redundante fica.

## Self-service como princípio

Self-service significa que o consumidor da plataforma não precisa interagir com o time de plataforma para provisionar recursos. O fluxo típico:

1. Dev commita um arquivo de config no repositório (ou chama uma API)
2. A plataforma lê essa declaração de intenção
3. Provisiona/configura automaticamente os recursos necessários
4. Dev recebe confirmação — sem abrir ticket, sem esperar aprovação manual

Na Atlassian, o Open Service Broker implementava esse fluxo para load balancing: dev enviava um pedido via API, o worker provisionava DNS, CloudFront, config Envoy; o [[tecnico/concepts/envoy-control-plane]] detectava o novo estado e propagava para a frota de proxies.

## Exemplo concreto: plataforma de edge da Atlassian

[[tecnico/entities/autores/vasilios-syrakis]] descreveu a plataforma que construiu:

- ~2.000 proxies Envoy em ~13 regiões AWS, provisionados por CloudFormation + AMI customizada
- Open Service Broker (FastAPI + SQS + DynamoDB) para receber pedidos de provisionamento
- Envoy Control Plane ("Sovereign") para distribuir config dinâmica para a frota
- Sidecars para autenticação (Rust), autorização e rate limiting — via [[tecnico/concepts/sidecar-pattern]]
- Produtos como Jira, Confluence, Bitbucket e Status Page atrás desse edge

O time de plataforma implementou autenticação, DoS protection e rate limiting uma única vez. Todos os produtos herdaram automaticamente.

## Relação com [[tecnico/concepts/trabalho-alavancado]]

Platform engineering é a definição operacional de trabalho alavancado aplicado à infraestrutura: você constrói algo uma vez e isso multiplica a capacidade de dezenas (ou centenas) de outros times. O custo é concentrado no time de plataforma; o benefício é distribuído por toda a engenharia.

## Ver também

- [[tecnico/concepts/envoy-control-plane]]
- [[tecnico/concepts/sidecar-pattern]]
- [[tecnico/entities/envoy-proxy]]
- [[tecnico/concepts/trabalho-alavancado]]

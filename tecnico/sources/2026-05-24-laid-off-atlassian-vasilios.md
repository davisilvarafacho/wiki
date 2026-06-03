---
title: "I was laid off by Atlassian"
tipo: source
dominio: tecnico
url: https://www.youtube.com/watch?v=55pTFVoclvE
autor: "Vasilios Syrakis"
publicado: 2026-05-24
capturado: 2026-06-03
tipo_fonte: youtube
tags: [platform-engineering, envoy, load-balancing, aws, devops, atlassian, sidecar, rust, fastapi]
---

# I was laid off by Atlassian

Vasilios Syrakis reflete sobre 8 anos trabalhando na Atlassian após ser demitido. O vídeo cobre a arquitetura da plataforma de load balancing self-service que ele construiu, os sistemas de infraestrutura AWS envolvidos, e reflexões não-técnicas sobre manutenção de software, mentoria e diplomacia.

Fonte: [[tecnico/entities/autores/vasilios-syrakis]]

---

## Sumário

### Entrevista e contratação
- Processo em 3 etapas: HackerRank (acertou tudo), entrevista técnica com whitepaper da Cloudflare sobre custom domains + perguntas de microservices, exercício de troubleshooting de incidente real (denial of service), entrevista de valores
- Contratado com a promessa de construir um **Open Service Broker** para load balancing self-service interno

### Arquitetura do OSB (Open Service Broker) — primeiros meses
- **FastAPI** como camada HTTP da API (passou por Connexion → Flask → FastAPI)
- **SQS** para desacoplar recebimento do pedido da execução: o web server recebe, joga na fila, retorna polling; o worker executa
- **DynamoDB** como state store: worker escreve resultado, web server lê no polling
- Tarefas de provisionamento típicas: criar DNS records, criar distribuição CloudFront, configurar serviços AWS via API
- Padrão clássico de [[tecnico/concepts/async-task-pattern]]: request → queue → worker → state store → polling

### Envoy como substituto dos load balancers proprietários
- Decisão de um arquiteto: substituir enterprise load balancers (com custo de licença) por [[tecnico/entities/envoy-proxy]] — proxy open-source, cloud-native, similar ao Nginx mas com API de configuração dinâmica (xDS)
- Motivação: self-service (devs não precisam abrir chamado para configurar load balancing)

### Envoy control plane — "Sovereign" (open-sourced no Bitbucket)
- FastAPI que carrega **templates** (tipos de recursos Envoy: clusters, routes, listeners) e **contexto** (dados dinâmicos vindos do broker/DynamoDB e de outros sources como S3)
- Renderiza configuração Envoy combinando template + contexto, expõe via xDS para os proxies consumirem em runtime — sem restart
- Contexto muda → templates rerenderizam → proxies recebem nova config automaticamente
- Ver [[tecnico/concepts/envoy-control-plane]] para o padrão completo

### Infraestrutura AWS (CloudFormation + Packer + SaltStack)
- **CloudFormation**: IaC para provisionar ~2.000 proxies Envoy em ~13 regiões; recursos típicos: VPC, subnet, internet gateway, security group, key pair, IAM role, ASG, NLB, Route 53, ACM
- **Packer** (HashiCorp): orquestra criação da AMI — sobe EC2 temporário, aplica SaltStack, faz snapshot → AMI
- **SaltStack**: configuration management declarativo (similar a Puppet/Ansible/Chef); instala e configura: Envoy, logging agent, security hardening, network tuning, sidecars, observability agent
- AMI referenciada pelo CloudFormation; ASG usa AMI para provisionar EC2s que sobem com tudo pré-configurado

### Migrações e features centralizadas (anos 3–6)
- Migração de todos os microservices Atlassian para o novo edge (a plataforma forçou: serviços não podiam mais se expor publicamente pelo load balancer antigo)
- Produtos migrados incluem: Jira, Confluence, Bitbucket, Status Page e outros
- Centralização de concerns no edge — antes de chegar nos backends:
  - **DoS protection**: provida por CloudFront (spearheaded por colega)
  - **Access logs**: configurados via filtros de rede do Envoy (HCM), dinâmicos por template
  - **Autenticação**: sidecar em Rust, escrito por Vasilios — [[tecnico/concepts/sidecar-pattern]]
  - **Autorização**: sidecar de outro time
  - **Rate limiting**: sidecar de outro time
- Sidecars instalados via AMI provisioning; recebem config dinâmica via wire local

### Reflexões não-técnicas
- **Manutenção de software**: "Building something is easy. Changing it and making sure you can still change it over time is difficult." Churn em certas áreas do código é smell — ver [[tecnico/concepts/churn-codebase]]
- **Mentoria**: difícil encontrar o equilíbrio entre dar a resposta e deixar o mentorado travar; intern que acompanhou recebeu rating máximo — o crédito é distribuído entre vários SMEs e o próprio esforço do intern
- **Diplomacia e conflito**: exposição a muitos tipos de managers e colegas; conflito de personalidade é inevitável; crescimento veio de tomar responsabilidade por gerenciar a diferença ativamente

---

## Citações relevantes

> "Building something is easy. Changing it and making sure you can still change it over time is difficult — because as you change things, it slowly becomes harder to change."

> "It'll be interesting with all these vibe-coded apps and AI-assisted apps to see how we handle that when we have people that are not really familiar with what they've created and the maintenance burdens appear."

> "Churn in the codebase... it's sort of a smell. It's an indication that that part of the service or project is going to keep increasing in size or complexity and something there needs to happen."

---

## Takeaways

- O padrão OSB (Open Service Broker) é uma abstração limpa para self-service de infraestrutura; qualquer plataforma interna que precise provisionar recursos pode se beneficiar
- Envoy + control plane xDS = infra de proxy programável que reage a mudanças de estado sem downtime
- O modelo sidecar permite adicionar concerns ortogonais (auth, rate limit) sem tocar no proxy principal nem nos backends
- Centralizar concerns no edge (autenticação, DoS, logs) é multiplicador de valor: mil times de backend entregam features sem reimplementar segurança
- Churn previsível em certas áreas do código é sinal de que aquele módulo precisa de atenção arquitetural antes de virar dívida
- Manutenção de software é o trabalho que nunca termina — ver conexão com [[pessoal/concepts/manutencao-da-vida]]

---

## Páginas relacionadas criadas/atualizadas

- [[tecnico/entities/autores/vasilios-syrakis]] — autor (novo)
- [[tecnico/entities/envoy-proxy]] — entidade (stub novo)
- [[tecnico/concepts/envoy-control-plane]] — conceito (novo)
- [[tecnico/concepts/sidecar-pattern]] — conceito (novo)
- [[tecnico/concepts/platform-engineering]] — conceito (novo)
- [[tecnico/concepts/churn-codebase]] — conceito (novo)

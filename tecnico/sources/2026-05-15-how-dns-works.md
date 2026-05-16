---
title: "How DNS Works: A Guide to Understanding the Internet's Address Book"
tipo: source
dominio: tecnico
url: https://www.freecodecamp.org/news/how-dns-works-the-internets-address-book/?ref=dailydev
autor: "Dhruv Prajapati"
publicado: 2025-05-14
capturado: 2026-05-15
tipo_fonte: blog-post
tags: [dns, redes, resolucao-de-nomes, infraestrutura]
criado: 2026-05-15
atualizado: 2026-05-15
---

# How DNS Works: A Guide to Understanding the Internet's Address Book

Artigo introdutório-intermediário do FreeCodeCamp cobrindo o funcionamento completo do DNS — desde como um dispositivo encontra seu primeiro servidor DNS até o processo de compra, configuração e propagação de um novo domínio.

## Sumário

- O DNS traduz nomes de domínio (ex: `example.com`) para IPs (ex: `192.0.2.1`), operando como o "GPS da internet"
- Dispositivos obtêm o endereço de um servidor DNS via: (a) configuração hardcoded de fábrica, (b) DHCP/ISP na conexão de rede, ou (c) configuração manual do usuário
- O processo de resolução percorre **5 camadas em sequência**: IP direto → cache da aplicação → cache do SO + `/etc/hosts` → Recursive Resolver → hierarquia DNS (root → TLD → authoritative)
- O **Recursive Resolver** (ex: BIND, Unbound) é o motor central: faz toda a caminhada hierárquica em nome do cliente
- Hierarquia DNS: **Root Servers** (13 clusters anycast, ~1.936 instâncias físicas em mai/2025) → **TLD Servers** (ex: `.com` gerenciado pela VeriSign) → **Authoritative Name Servers**
- **Glue records**: registros A/AAAA incluídos na resposta de referência NS quando o name server está dentro do próprio domínio — evita dependência circular de bootstrapping
- **Caching** opera em múltiplos níveis (app, SO, recursive resolver); **TTL** controla a expiração; **negative cache** evita re-consultas de domínios inexistentes
- **Root hints file**: lista hardcoded de IPs dos root servers, presente em todo resolver, evita bootstrap circular
- **Priming queries**: ao inicializar, o resolver consulta a hierarquia para atualizar os IPs dos root servers
- Zone files (texto) foram substituídas por bancos de dados em memória (hash tables, tries) para suportar o volume moderno de queries
- Anycast é universal nos root servers; TLD e authoritative adotam parcialmente por questões de custo
- **Registradores de domínio** (GoDaddy, Hostinger) são intermediários entre o dono e o registry do TLD; glue records são registrados no TLD registry quando o name server está dentro do domínio
- **Propagação DNS** após mudanças: pode levar 24–48h por causa do caching distribuído global

## Citações relevantes

> "DNS resolution works by sending a query through a chain of DNS servers, each one helping to pinpoint the exact address."

> "There are 13 root server clusters, named a.root-servers.net to m.root-servers.net, operated by 12 organizations [...] As of May 10, 2025, 1,936 anycast instances ensure high availability and scalability."

> "Glue records are critical when the requested name servers' domains are within the queried domain [...] preventing circular dependency by supplying the IP without resolving the domain."

## Takeaways

- DNS é **hierárquico e distribuído por design** — sem SPOF quando bem configurado com anycast
- O **TTL** é a peça central do comportamento de cache; migrações DNS devem considerar o TTL atual e baixá-lo com antecedência
- Distinguir **recursive resolver** (faz a caminhada) de **authoritative server** (tem a resposta definitiva) é fundamental para debugging de problemas de DNS
- A dependência circular (ns1.example.com para example.com) é um problema real de bootstrapping, resolvido elegantemente pelos glue records
- `dig +trace <dominio>` é a ferramenta de debugging que mostra toda a caminhada hierárquica

## Páginas relacionadas

- [[tecnico/concepts/dns]] — conceito criado
- [[tecnico/concepts/anycast]] — conceito criado
- [[tecnico/concepts/glue-records]] — conceito criado
- [[tecnico/entities/autores/dhruv-prajapati]] — autor criado (stub)

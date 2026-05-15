---
title: "DNS (Domain Name System)"
tipo: concept
dominio: tecnico
tags: [dns, redes, infraestrutura, resolucao-de-nomes]
criado: 2026-05-15
atualizado: 2026-05-15
fontes: [tecnico/sources/2026-05-15-how-dns-works]
---

# DNS (Domain Name System)

Sistema distribuído e hierárquico que traduz nomes de domínio legíveis por humanos (como `example.com`) em endereços IP (`192.0.2.1`) usados pelos computadores para comunicação em rede. Fundado em 1983; base da usabilidade da internet.

## Como um dispositivo encontra o primeiro servidor DNS

Todo dispositivo precisa saber o IP de ao menos um servidor DNS. Isso é resolvido por três mecanismos em ordem de precedência:

1. **Hardcoded de fábrica** — routers e dispositivos vêm pré-configurados com IPs de DNS público (ex: `8.8.8.8` Google, `1.1.1.1` Cloudflare)
2. **DHCP** — ao conectar a uma rede, o roteador distribui IPs de DNS via DHCP (geralmente os do ISP, ex: `75.75.75.75` Comcast)
3. **Configuração manual** — usuários avançados podem definir qualquer DNS: OpenDNS (`208.67.222.222`), Quad9 (`9.9.9.9`), etc.

## O processo de resolução (5 etapas)

Quando uma aplicação precisa resolver `example.com`:

**1. IP válido direto** — verifica via regex se o destino já é um IP. Se sim, dispensa DNS completamente.

**2. Cache da aplicação** — browsers (Chrome, Firefox) mantêm cache DNS próprio. Se o mapeamento estiver lá, resolve localmente.

**3. Cache do SO + hosts file** — o cliente DNS do SO verifica:
   - Cache local (Windows: `dnscache`; macOS: `mDNSResponder`; Linux: NSS)
   - Arquivo `/etc/hosts` (mapeamentos manuais, ex: `127.0.0.1 localhost`)

**4. Recursive Resolver** — se nada acima resolver, o SO encaminha a query ao servidor DNS configurado. Esse servidor roda um **Recursive Resolver** (ex: BIND, Unbound) que conduz a caminhada completa pela hierarquia DNS.

**5. Resolução recursiva** — o resolver percorre três níveis:
   - **Root servers** → retorna referência ao TLD server correto (ex: `.com`)
   - **TLD server** → retorna referência ao authoritative name server do domínio
   - **Authoritative name server** → retorna o registro final (A, AAAA, CNAME, MX...)

## Hierarquia de servidores

```
Root Servers (13 clusters, anycast global)
    └── TLD Servers (ex: .com → VeriSign, .br → Registro.br)
            └── Authoritative Name Servers (ex: ns1.example.com)
```

### Root Servers

- 13 clusters nomeados de `a.root-servers.net` a `m.root-servers.net`, operados por 12 organizações (VeriSign opera dois)
- Usam [[anycast]] routing — em mai/2025 havia 1.936 instâncias físicas distribuídas globalmente
- O número 13 tem origem histórica: limitação do UDP (512 bytes/resposta cabia 13 registros NS); com anycast, a capacidade física escala livremente mantendo os 13 IPs lógicos
- **Root hints file**: lista hardcoded de IPs dos root servers presente em todo resolver, evita bootstrap circular
- **Priming queries**: ao inicializar, o resolver atualiza os IPs dos root servers consultando a própria hierarquia (RFC 8109)
- **Root zone file**: banco de dados de todos os TLDs e seus name servers, mantido pela IANA/ICANN

### TLD Servers

- Gerenciados por registries (ex: VeriSign para `.com`, IANA para `.gov`)
- Mantêm zone files com todos os domínios registrados sob o TLD e seus authoritative name servers
- Ao receber uma query, retornam referência NS + [[glue-records]] quando aplicável

### Authoritative Name Servers

- Têm a resposta definitiva para um domínio específico
- Respondem com registros DNS: **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias), **MX** (e-mail)
- Configurados via registrador de domínio (GoDaddy, Hostinger, Cloudflare) ou auto-hospedados

## Caching e TTL

O DNS usa cache agressivamente em todos os níveis para escalar:

| Nível | Onde |
|---|---|
| Aplicação | Cache interno do browser/app |
| SO | `dnscache` / `mDNSResponder` / NSS |
| Recursive Resolver | Cache de respostas root/TLD/authoritative |

- **TTL (Time to Live)**: campo em cada registro DNS que define por quantos segundos ele pode ser cacheado. Valores comuns: 300 (5min), 3600 (1h), 86400 (24h)
- **Negative cache**: armazena respostas de domínios inexistentes para evitar re-consultas repetidas
- **Forwarded query cache**: cache de queries encaminhadas a outros resolvers

> [!note] Implicação prática: ao migrar um domínio para outro IP, verifique o TTL atual antes. Se estiver em 86400, a propagação pode levar 24h. Boa prática: baixar o TTL para 300 alguns dias antes da migração.

## Glue Records

Quando o authoritative name server de um domínio está dentro do próprio domínio (ex: `ns1.example.com` para `example.com`), há uma dependência circular. A solução são os [[glue-records]]: o TLD server inclui o IP do name server junto com a referência NS, quebrando o ciclo.

## Registro e propagação de domínios

Ao comprar um domínio via registrador:

1. Registrador notifica o registry do TLD → domínio adicionado ao zone file do TLD
2. Usuário configura name servers no painel do registrador
3. Zone file do authoritative server é populado com registros (A, CNAME, MX...)
4. **Propagação DNS**: mudanças levam 24–48h para propagar globalmente devido ao caching distribuído

## Debugging

```bash
dig +trace example.com      # mostra toda a caminhada hierárquica
dig @8.8.8.8 example.com    # consulta diretamente o DNS do Google
nslookup example.com        # alternativa multiplataforma
```

## Evolução técnica

Zone files em texto puro (padrão original do RFC 1035) foram substituídas por bancos de dados em memória (hash tables, tries) para suportar o volume de queries moderno — especialmente em TLDs como `.com`. A abstração de "zone file" persiste conceitualmente mesmo sem ser a implementação física.

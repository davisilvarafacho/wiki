---
title: "Anycast"
tipo: concept
dominio: tecnico
tags: [redes, roteamento, infraestrutura, dns, cdn]
criado: 2026-05-15
atualizado: 2026-05-15
fontes: [tecnico/sources/2026-05-15-how-dns-works]
---

# Anycast

Técnica de roteamento de rede em que múltiplos servidores geograficamente distribuídos compartilham o **mesmo endereço IP**. Quando um cliente envia uma requisição para esse IP, a infraestrutura de roteamento (tipicamente BGP) encaminha o pacote para a instância mais próxima ou menos carregada.

## Contraste com outros esquemas de endereçamento

| Esquema     | Destino                                               |
|-------------|-------------------------------------------------------|
| Unicast     | Um IP → um destino específico                         |
| Broadcast   | Um IP → todos os hosts da rede local                  |
| Multicast   | Um IP → um grupo de hosts inscritos                   |
| **Anycast** | **Um IP → o nó mais próximo de um conjunto de nós**   |

## Benefícios

- **Baixa latência**: usuário é atendido pela instância geograficamente mais próxima
- **Alta disponibilidade**: se uma instância falha, o tráfego é roteado automaticamente para a próxima
- **Distribuição de carga natural**: múltiplas instâncias absorvem tráfego global sem configuração explícita no cliente
- **Transparência**: do ponto de vista do cliente, é um único servidor normal

## Como funciona (BGP)

Anycast depende do BGP (Border Gateway Protocol). Cada instância do serviço anuncia a mesma rota BGP para o mesmo prefixo IP. Os roteadores da internet, ao receberem múltiplos anúncios para o mesmo IP, encaminham o tráfego para a instância com menor "distância" BGP — que geralmente corresponde à mais próxima geograficamente.

## Uso no DNS

Os **13 clusters de root servers** do [[dns]] usam anycast universalmente. Isso resolveu o problema histórico de escala: o DNS foi originalmente projetado com 13 root servers por limitação do UDP (512 bytes/resposta cabia 13 registros NS). Com anycast, os 13 IPs lógicos passaram a corresponder a centenas/milhares de instâncias físicas.

- Em mai/2025: 1.936 instâncias anycast dos root servers globalmente
- TLD servers e authoritative servers adotam anycast parcialmente; servidores menores podem operar com unicast por custo/operacional

## Uso em CDNs e DNS público

CDNs como Cloudflare, Fastly e Akamai usam anycast extensivamente. Exemplos:

- `1.1.1.1` (Cloudflare DNS) — IP anycast respondido por centenas de PoPs globais
- `8.8.8.8` (Google DNS) — mesmo padrão
- Cloudflare CDN — todo o tráfego de clientes passa por anycast antes de atingir o servidor de origem

## Limitação

Anycast não garante consistência de sessão: uma sessão TCP pode ser transferida entre instâncias se o roteamento BGP mudar durante a conexão. Por isso anycast é mais adequado para protocolos stateless (UDP/DNS) ou serviços que tolerem reconexão. Para TCP de longa duração, é necessário combinação com sticky routing ou uso criterioso.

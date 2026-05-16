---
title: "Glue Records"
tipo: concept
dominio: tecnico
tags: [dns, redes, infraestrutura]
criado: 2026-05-15
atualizado: 2026-05-15
fontes: [tecnico/sources/2026-05-15-how-dns-works]
---

# Glue Records

Registros DNS (do tipo A ou AAAA) fornecidos **fora da zona autoritativa** de um domínio, incluídos na resposta de referência de um servidor pai (root ou TLD server), com o objetivo de quebrar uma dependência circular de resolução.

## O problema: dependência circular

Considere o domínio `example.com` com o seguinte authoritative name server configurado: `ns1.example.com`.

Para resolver `example.com`, o recursive resolver precisa saber o IP de `ns1.example.com`. Mas para isso, precisaria consultar o authoritative server de `example.com` — que é justamente `ns1.example.com`. **Dependência circular**.

## A solução: glue records

O TLD server (ex: `.com`), ao responder uma query sobre `example.com` com os registros NS, inclui também os registros **A/AAAA** dos name servers como glue records — mesmo que esses registros sejam tecnicamente responsabilidade da zona de `example.com`. Assim o resolver obtém o IP de `ns1.example.com` sem precisar resolver `example.com` primeiro.

```
Pergunta ao TLD: "Quem é o authoritative server de example.com?"

Resposta TLD:
  NS: ns1.example.com         ← referência
  A:  ns1.example.com → 1.2.3.4  ← glue record (quebra o ciclo)
```

## Quando são necessários

Glue records são **obrigatórios** quando o nome do name server está dentro do próprio domínio sendo delegado:

- `ns1.example.com` para `example.com` → **glue obrigatório**
- `ns1.otherdomain.com` para `example.com` → **glue desnecessário** (pode-se resolver `otherdomain.com` independentemente)

Para TLD servers, glue records são sempre incluídos nas respostas — os TLD name servers (ex: `a.gtld-servers.net`) têm seus IPs fornecidos como glue pelos root servers.

## Onde ficam armazenados

Glue records são registrados no **registry do TLD** junto com a delegação do domínio. Ao configurar name servers dentro do próprio domínio via registrador, o registrador solicita os IPs correspondentes e os submete ao TLD registry. Essa é uma das etapas ao comprar e configurar um novo domínio (ver [[dns#Registro e propagação de domínios]]).

## Referência

Definidos na RFC 1035 — documento fundacional do [[dns]].

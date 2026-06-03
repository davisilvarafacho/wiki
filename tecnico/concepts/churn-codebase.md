---
title: "Churn de Codebase"
tipo: concept
dominio: tecnico
tags: [manutenção, arquitetura, dívida-técnica, qualidade, software]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]
---

# Churn de Codebase

*Code churn* é a frequência com que determinadas partes de um codebase são modificadas ao longo do tempo. Alta taxa de churn em uma área específica é um *smell* — um indicador de que aquele módulo tende a crescer em complexidade e vai acumular dívida técnica se não receber atenção arquitetural.

> "Once you notice that there is some churn, it's sort of a smell. It is an indication that that part of the service or project is going to keep increasing in size or complexity and something there needs to happen." — [[tecnico/entities/autores/vasilios-syrakis]]

## Por que churn concentrado é um problema

Cada mudança em código adiciona chance de acoplamento acidental. Módulos que mudam com frequência tendem a:

- Acumular responsabilidades que não eram suas originalmente
- Ser modificados por muitos autores diferentes com visões diferentes
- Tornar-se pontos de medo (*fear zones*): ninguém quer mexer por medo de quebrar
- Crescer em tamanho sem que haja uma refatoração correspondente

Com o tempo, o custo marginal de cada mudança cresce: mudar uma coisa quebra outra. O trabalho de "detangling" (desembaraçar acoplamentos) se torna necessário e caro.

## Churn como dado, não como intuição

A análise de churn pode ser feita objetivamente com ferramentas de análise de histórico git:

- Contar o número de commits por arquivo em um período
- Identificar os arquivos com maior número de autores distintos
- Cruzar churn alto com tamanho do arquivo (alta complexidade + alto churn = risco máximo)

Ferramentas como `git log --follow`, `code-maat` (Adam Tornhill) ou extensões de IDE mostram esses padrões.

## O que fazer quando detectar churn

1. **Identificar por quê** o módulo muda tanto: requisitos que chegam sempre ali? API mal definida? Falta de abstração?
2. **Separar responsabilidades**: se o módulo concentra lógica de diferentes domínios, extrair
3. **Adicionar testes**: módulos com churn alto sem cobertura de testes são dívida dupla
4. **Documentar invariantes**: o que *não* deve mudar naquele módulo? Tornar explícito ajuda novos contribuidores

## Relação com manutenção de software

Churn é um dos sinais que aparecem cedo na vida de sistemas que mais tarde se tornam impossíveis de manter. A observação de [[tecnico/entities/autores/vasilios-syrakis]] é precisa: "Building something is easy. Changing it and making sure you can still change it over time is difficult."

O churn previsível é a manifestação técnica do princípio de [[pessoal/concepts/manutencao-da-vida]]: o que não é cuidado deteriora progressivamente, e a deterioração tem juros compostos.

## Churn em projetos assistidos por IA

Vasilios levantou uma preocupação válida sobre o futuro de projetos "vibe-coded" ou gerados com assistência de IA por pessoas que não entendem profundamente o que foi criado: os problemas de manutenção não aparecem no dia 1, aparecem meses depois, quando o churn se acumula e ninguém entende mais as interdependências do sistema.

## Ver também

- [[pessoal/concepts/manutencao-da-vida]]
- [[tecnico/concepts/tech-lead]]
- [[tecnico/sources/2026-05-24-laid-off-atlassian-vasilios]]

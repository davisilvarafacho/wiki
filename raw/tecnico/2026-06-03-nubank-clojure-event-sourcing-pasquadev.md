---
title: "Por que o Nubank usa uma linguagem que quase ninguém conhece?"
tipo: source
dominio: tecnico
url: https://www.youtube.com/watch?v=3WDjURKrUK4
autor: "Viní Pasquantônio (pasquadev)"
publicado: 2026-06-03
capturado: 2026-06-03
tipo_fonte: youtube-video
tags: [clojure, nubank, programacao-funcional, event-sourcing, datomic, ddd, jvm]
---

# Por que o Nubank usa uma linguagem que quase ninguém conhece?

Canal: pasquadev
URL: https://www.youtube.com/watch?v=3WDjURKrUK4

Vídeo de reação e análise ao vídeo original do Nubank: "Why one of the largest digital banks chose Clojure and Datomic?"

## Transcrição / pontos principais

- Nubank usa Clojure como linguagem principal, inclusive para scripts e infraestrutura
- CTO do Nubank leu o paper "Out of the Tar Pit" e tirou o insight central: mutable state e side effects são a fonte de toda complexidade acidental em sistemas grandes
- Nubank precisava ser grande (banco de varejo em escala) ou morrer tentando — modelo de negócio não funciona em escala pequena
- Imutabilidade elimina a categoria de bugs de estado compartilhado: aqueles que só acontecem com "alinhamentos cósmicos" e são quase impossíveis de reproduzir
- Side effects devem ser explícitos e empurrados para as periferias do domínio (arquitetura hexagonal / cebola)
- Datomic: banco de dados imutável — não significa que nada muda, mas que você nunca perde o histórico de estados anteriores. Para um banco financeiro com requisitos de auditoria e regulatórios, isso é um superpoder
- O que o CTO descreve sobre o Datomic é Event Sourcing: persistir eventos (fatos imutáveis), não o estado atual; reaplica os eventos para calcular o estado presente
- Conta bancária como exemplo clássico: o saldo não é o que persiste — as transações são o que persiste
- CQRS mencionado como padrão complementar ao event sourcing
- "Codebase em Java/Ruby envelhece como leite; com funcional + DDD + eventing, envelhece como vinho"
- Clojure na JVM permite acesso ao ecossistema maduro de bibliotecas Java sem precisar reinventar a roda — o que seria um desvio da missão central (construir o banco, não construir bibliotecas)
- Apresentador trabalhou na Alemanha num sistema de apostas esportivas em Scala — mesmo paradigma funcional; variável mutável já era code smell; time já sabia que tinha jeito mais elegante de resolver

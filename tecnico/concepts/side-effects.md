---
title: "Side Effects (Efeitos Colaterais)"
tipo: concept
dominio: tecnico
tags: [side-effects, funcional, pureza, arquitetura-hexagonal]
criado: 2026-06-03
atualizado: 2026-06-03
fontes: [tecnico/sources/2026-06-03-nubank-clojure-event-sourcing-pasquadev]
---

# Side Effects (Efeitos Colaterais)

Qualquer coisa que uma função faz além de receber um input e retornar um output. Side effects incluem: escrever no banco de dados, enviar e-mail, chamar uma API externa, modificar uma variável global, imprimir no console, ler o relógio.

## O problema

Uma função chamada `calcularPreco` deveria calcular o preço. Se ela também envia um e-mail de confirmação e atualiza o banco de dados, esses comportamentos ocultos são side effects. O chamador não sabe que eles existem a menos que leia o código interno da função.

Isso cria:
- **Surpresas em produção** — a função faz mais do que o nome sugere
- **Dificuldade de teste** — para testar `calcularPreco` você precisa mockar banco e servidor de e-mail
- **Acoplamento oculto** — a função depende de infraestrutura que não está na sua assinatura
- **Não determinismo** — chamar a mesma função duas vezes pode produzir efeitos diferentes dependendo do estado externo

## A solução funcional: tornar side effects explícitos e periféricos

Programação funcional não elimina side effects — sistemas reais precisam escrever no banco, enviar e-mail, chamar APIs. O que muda é a visibilidade e o posicionamento:

1. **Explicitação** — a assinatura da função ou o sistema de tipos deixa claro que há um side effect. Em Kotlin, `suspend` e os contextos do coroutine system cumprem esse papel. Em Haskell, a mônada `IO` faz isso no nível do tipo.
2. **Periferização** — side effects ficam nas bordas do sistema (camada de infraestrutura, adaptadores), nunca no domínio central. O núcleo do sistema é puro; a interação com o mundo externo fica isolada na periferia.

Essa segunda propriedade é a arquitetura hexagonal / cebola: o domínio no centro, adaptadores ao redor. Qualquer coisa que "cheira" a infraestrutura (banco, fila, e-mail) fica na camada mais externa.

## Relacionado

- [[tecnico/concepts/programacao-funcional]]
- [[tecnico/concepts/imutabilidade]]

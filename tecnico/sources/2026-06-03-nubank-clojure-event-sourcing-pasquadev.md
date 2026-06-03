---
title: "Por que o Nubank usa uma linguagem que quase ninguém conhece? (pasquadev)"
tipo: source
dominio: tecnico
url: https://www.youtube.com/watch?v=3WDjURKrUK4
autor: "Viní Pasquantônio (pasquadev)"
publicado: 2026-06-03
capturado: 2026-06-03
tipo_fonte: youtube-video
tags: [clojure, nubank, programacao-funcional, event-sourcing, datomic, ddd, jvm]
criado: 2026-06-03
atualizado: 2026-06-03
---

# Por que o Nubank usa uma linguagem que quase ninguém conhece?

Vídeo de reação e análise ao vídeo original do Nubank: "Why one of the largest digital banks chose Clojure and Datomic?". O apresentador, Viní Pasquantônio (pasquadev), usa o case como ponto de partida para explicar programação funcional, event sourcing e DDD a partir de um exemplo real de escala.

---

## Sumário

- **Clojure como linguagem principal do Nubank** — usado em produção, scripts e infraestrutura; roda na JVM, herdando o ecossistema maduro de libs Java sem precisar reinventá-las
- **"Out of the Tar Pit" como fundação intelectual** — o CTO leu o paper e extraiu o insight central: mutable state e side effects são a fonte de toda a complexidade acidental em sistemas grandes; essa leitura motivou as escolhas técnicas
- **Imutabilidade elimina uma categoria inteira de bugs** — bugs de estado compartilhado só aparecem com "alinhamentos cósmicos" de condições; são impossíveis de reproduzir, testar e corrigir; programação funcional torna esse tipo de bug estruturalmente impossível
- **Side effects devem ser explícitos e periféricos** — uma função chamada `calcularPreco` não deveria enviar e-mail nem atualizar banco; em programação funcional, side effects ficam declarados, visíveis e empurrados para a borda do sistema (arquitetura cebola / hexagonal)
- **Datomic como banco imutável** — não significa que nada muda, mas que os estados anteriores nunca são perdidos; o histórico é parte do modelo de dados, não um log separado; perfeito para requisitos de auditoria e regulatórios de um banco financeiro
- **Datomic implementa Event Sourcing no nível do banco** — o que persiste são eventos (fatos imutáveis no passado), não o estado atual; o estado é reconstruído reaplicando os eventos
- **Conta bancária como exemplo clássico de Event Sourcing** — o saldo não é persistido; o que persiste são todas as transações; o saldo é calculado na leitura reaplicando o histórico
- **Vantagens do Event Sourcing** — reprodução 100% de qualquer bug (basta salvar os eventos e dar play); testes para 100% dos bugs; estado em tempo real; informação histórica nativa
- **Desafios do Event Sourcing** — curva de aprendizado alta; event log cresce muito (estratégia de snapshots/checkpoints é necessária); raramente visto no mercado
- **CQRS como complemento natural** — mencionado como padrão do lado da leitura; separação entre escrever eventos e ler estado
- **"Código envelhece como leite ou como vinho"** — Java/Ruby: o codebase deteriora com o tempo, acumula legado, exige o especialista de 20 anos; funcional + DDD + eventing: o código ganha robustez com o tempo porque o domínio está bem modelado e os estados são imutáveis
- **Escala corrobora o paradigma** — o apresentador trabalhou com Scala (funcional) num sistema de apostas esportivas na Alemanha; variável mutável já era code smell imediato no time; migraram de Java justamente por bugs de estado

---

## Citações

> "Mutable state e side effects são a fonte de toda a complexidade acidental em sistemas grandes."
> — CTO do Nubank, parafraseando "Out of the Tar Pit"

> "Codebase em Java/Ruby envelhece como leite. Com funcional + DDD + eventing, envelhece como vinho."
> — engenheiro do Nubank no vídeo original

> "Hoje código está barato. Código ruim é extremamente caro."
> — Viní Pasquantônio

---

## Takeaways

- Programação funcional não é apenas estética de código — é uma postura que elimina categorias inteiras de bugs por design
- Event Sourcing é a aplicação da imutabilidade ao banco de dados; o Datomic é a implementação mais radical dessa ideia
- Sistemas que precisam de auditabilidade, debugging confiável e evolução sustentada de longo prazo têm razões estruturais para preferir funcional + event sourcing
- A escolha da JVM para Clojure mostra pragmatismo: o objetivo era construir o banco, não construir linguagens e bibliotecas
- Funcional + DDD + eventing é um stack raro no mercado — mas quando dominado, muda como você lê código, entende sistemas e concebe soluções

---

## Páginas relacionadas

- [[tecnico/concepts/programacao-funcional]]
- [[tecnico/concepts/event-sourcing]]
- [[tecnico/concepts/imutabilidade]]
- [[tecnico/concepts/side-effects]]
- [[tecnico/entities/nubank]]
- [[tecnico/entities/clojure]]
- [[tecnico/entities/datomic]]
- [[tecnico/entities/autores/vini-pasquantonio]]

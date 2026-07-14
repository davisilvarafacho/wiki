---
title: "Operações em lote (bulk operations)"
tipo: concept
dominio: tecnico
tags: [orm, performance, banco-de-dados, django]
fontes: [tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Operações em lote (bulk operations)

Em vez de executar uma query de INSERT ou UPDATE por objeto, agrupar múltiplos objetos em uma única query (ou um número reduzido delas). Reduz o número de round-trips ao banco, que costuma ser o custo dominante em operações de escrita em massa.

## No Django ORM

`bulk_create()` e `bulk_update()` executam inserções/atualizações de múltiplos objetos em queries agrupadas, em vez de uma query por `.save()`:

```python
Produto.objects.bulk_create(lista_de_produtos, batch_size=1000)
```

- Para lotes acima de ~5000 objetos, especificar `batch_size` explicitamente — o tamanho ideal depende do tamanho de cada objeto (número de colunas, tamanho dos dados).
- Lotes grandes demais aumentam consumo de memória em Python; lotes pequenos demais perdem o ganho de reduzir round-trips. É um equilíbrio a calibrar por caso.

## Por que importa

Junto com a eliminação de [[tecnico/concepts/n-plus-1-queries|N+1 queries]], é uma das otimizações de maior retorno por esforço de implementação: poucas linhas de mudança, redução direta no número de queries executadas contra o banco.

## Ver também

- [[tecnico/entities/django]]
- [[tecnico/entities/postgresql]]
- [[tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]]

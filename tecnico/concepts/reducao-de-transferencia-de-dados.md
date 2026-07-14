---
title: "Redução de transferência de dados"
tipo: concept
dominio: tecnico
tags: [performance, orm, api, django]
fontes: [tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Redução de transferência de dados

Princípio de performance aplicável em duas camadas distintas de uma aplicação web: buscar do banco só o que será usado, e devolver ao cliente só o que ele consome. Em ambos os casos, o custo (tempo de resposta, banda, dinheiro) escala linearmente com o volume de dados desnecessários multiplicado pelo número de requests.

## Camada banco → aplicação

O Django ORM busca todas as colunas de um modelo por padrão. Quando só algumas são necessárias:

- **`.only(*campos)`** — busca apenas os campos especificados.
- **`.defer(*campos)`** — busca todos os campos exceto os especificados (útil quando poucos campos são caros, ex: um `TextField` grande).

```python
Usuario.objects.only("nome", "email")
```

## Camada aplicação → cliente

Serializers de API (ex: Django Rest Framework) devem expor apenas os campos que o cliente efetivamente consome. JSON não é um formato compacto — cada campo extra é custo repetido em toda resposta.

## Por que importa em escala

Exemplo citado: uma resposta de 1KB chamada 1 milhão de vezes por dia já representa ~30GB de tráfego por mês. Excluir um campo não usado tem impacto multiplicado pelo volume de requests, não pelo tamanho absoluto do dado.

## Ver também

- [[tecnico/entities/django]]
- [[tecnico/concepts/n-plus-1-queries]] — princípio complementar: primeiro reduzir o número de queries, depois o que cada uma transporta
- [[tecnico/sources/2026-07-14-django-100-milhoes-de-requests-por-dia]]

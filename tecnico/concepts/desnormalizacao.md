---
title: "Desnormalização"
tipo: concept
dominio: tecnico
tags: [performance, banco-de-dados, modelagem]
fontes: [tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Desnormalização

Armazenar redundância proposital no banco — um valor derivado ou duplicado — para evitar recalcular ou rejuntar dados a cada leitura. Troca custo de leitura por custo de manutenção (o dado redundante precisa ser mantido sincronizado).

## Exemplo

Contar quantos produtos têm a frase "para crianças" na descrição via `COUNT` a cada request fica caro conforme a tabela cresce (10 mil, 100 mil, 1 milhão de linhas). Desnormalizar significa guardar essa contagem já pronta, atualizando-a periodicamente ou a cada inserção/remoção:

```python
# Sem desnormalização — recalcula toda vez
count = my_model.objects.filter(description__icontains="para crianças").count()

# Desnormalizado — leitura direta
count = my_count.objects.get(description="para crianças")
total_count = count.total
```

## Quando usar

**Último recurso.** Só depois de esgotar índices, caching, redução de queries e outras otimizações — porque introduz dados não acoplados que podem divergir da fonte de verdade se a sincronização falhar.

## Ver também

- [[tecnico/entities/django]]
- [[tecnico/concepts/caching]] — outra forma de evitar recálculo, mas sem duplicar o dado permanentemente no schema
- [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]]

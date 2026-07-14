---
title: "Caching"
tipo: concept
dominio: tecnico
tags: [performance, memoria, redis, memcached]
fontes: [tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Caching

Guardar o resultado de uma operação cara (query, cálculo, chamada externa) em memória ou storage rápido, para devolver a mesma resposta sem repetir o custo — desde que o dado ainda seja válido.

## Quando usar

Faz sentido quando a resposta é cara de gerar e não muda a cada request — modelos que raramente mudam, agregações, resultados de queries pesadas. Sem caching, cada request recalcula ou reconsulta do zero.

## Backends comuns

- **Memcached / Redis** — em memória, rápido, mas **efêmero**: o cache inteiro some se o processo reiniciar ou a máquina desligar
- **Database cache** — persiste em tabela do próprio banco
- **File system cache** — persiste em disco

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

## Granularidade

Configurável em vários níveis, do site inteiro a uma view (`@cache_page`) ou a um fragmento pequeno de dado:

```python
@cache_page(60 * 15)
def my_view(request):
    return render(request, 'myapp/template.html', {
        'time_consuming_data': get_time_consuming_data()
    })
```

## Ver também

- [[tecnico/entities/django]]
- [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]]

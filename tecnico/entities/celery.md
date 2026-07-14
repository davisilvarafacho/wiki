---
title: "Celery"
tipo: entity
dominio: tecnico
tags: [python, fila-assincrona, django, background-jobs]
fontes: [tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]
criado: 2026-07-14
atualizado: 2026-07-14
---

# Celery

*A ser preenchido quando houver fonte dedicada.*

Fila de tarefas assíncronas mais popular do ecossistema Python. Usado tipicamente junto de [[tecnico/entities/django]] para tirar do ciclo request-response qualquer trabalho cujo tempo de resposta não é controlado pela própria aplicação (envio de email, chamadas a APIs de terceiros, processamento pesado).

## Uso típico

```python
from celery import shared_task

@shared_task
def send_order_confirmation(order_pk):
    email_data = generate_data_for_email(order_pk)
    send_customized_mail(**email_data)
```

O request retorna imediatamente; a tarefa é processada depois por um worker separado, lendo de uma fila (Redis ou RabbitMQ como broker mais comuns).

## Ver também

- [[tecnico/entities/django]]
- [[tecnico/sources/2026-07-14-como-escalar-django-para-1-milhao-de-usuarios]]

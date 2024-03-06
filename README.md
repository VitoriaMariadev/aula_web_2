# Iniciar um projeto Django

django-admin startproject nomedoprojeto

# Iniciar um app no Django

python manage.py startapp nomedoaplicativo

# Rodar um projeto Django

python manage.py runserver

# Como indicar o caminho da url de um app

Vai no arquivo 'urls.py' que já vem junto com o projeto Django

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nome_do_app/', include("nome_do_app.urls"))
]

```

# Como pegar parâmetros na Url

Tem que ir no app e criar um arquivo chamado 'urls.py' e escrever o código:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:parametro>/", views.nome_da_funcao, name="nome_da_funcao"), # Como passar um parametro pela URL
]
```

No arquivo 'views.py' do app:

```python
from django.shortcuts import render

def index(request): # Esse aqui é só pra não dá erro
    ...

def nome_da_funcao(request, parametro):
    ...
```

# Como colocar o HTML e o CSS

Dentro do app criar a pasta 'templates' e dentro dela criar a pasta com o nome do app e o arquivo 'index.html'

## templates/nome_do_app/index.html

Para colocar o CSS tem que criar a pasta 'static' e dentro dela criar uma pasta com o nome do app e depois o arquivo 'styles.css'

## static/nome_do_app/styles.css

Para linkar o CSS no HTML

```html
{% load static %} <!-- precisa dessa linha para funcionar -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WEB 2</title>
    <link rel="stylesheet" href="{% static 'nome_do_app/styles.css' %}"> <!-- Essa linha de código é a que linka o CSS -->

</head>
```
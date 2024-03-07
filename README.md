# Iniciar um projeto Django

django-admin startproject nomedoprojeto

# Iniciar um app no Django

python manage.py startapp nomedoaplicativo

Sempre que criar um app tem que esrever o nome dele no arquivo 'settings.py'

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
    path("<int:parametro>/", views.nome_da_funcao, name="nome_da_funcao"), # Como passar um parametro pela URL
    # path("<str:parametro>/", views.nome_da_funcao, name="nome_da_funcao"), Use com 'str' caso o valor seja uma string
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

### templates/nome_do_app/index.html

Para colocar o CSS tem que criar a pasta 'static' e dentro dela criar uma pasta com o nome do app e depois o arquivo 'styles.css'

### static/nome_do_app/styles.css

Para linkar o CSS no HTML

```html
{% load static %}
<!-- precisa dessa linha para funcionar -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>WEB 2</title>
    <link rel="stylesheet" href="{% static 'nome_do_app/styles.css' %}" />
    <!-- Essa linha de código é a que linka o CSS -->
  </head>
</html>
```

Se tiver algum erro olhe o aquivo CSS está no plural 'styles.css'

# Como 'manda' o arquivo HTML pela URL

No arquivo 'views.py' do app:

```python
from django.shortcuts import render
from django.http import HttpResponse # Tem que importar

# Create your views here.

def nome_do_app(resquest):

    nome = 'Maria'

    return render(resquest, "nome_do_app/index.html", {
        'nome': nome, # Não pode esquecer da virgula
        'idade': 17,
    })

```

# Como receber variáveis pelo HTML

No arquivo 'views.py':

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def nome_do_app(request):

    nome = 'Maria'

    # Manda as variáveis por aqui
    return render(request, "nome_do_app/index.html", {
        'nome': nome, # Tem que tá entre '' e com dois pontos no final
        'numero': 173434,
    })
```

No arquivo 'index.html' pra mostrar a variável tem que tá entre chaves duplas {{variavel}}:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>WEB 2</title>
    <link rel="stylesheet" href="{% static 'nome_do_app/styles.css' %}" />
  </head>

  <body>
    <h1>Agenda telefonica</h1>

    <ul>
      <li>{{nome}} - {{numero}}</li>
    </ul>
  </body>
</html>
```

# Como usar o FOR:

No arquivo 'views.py':

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contatos(request, id):
    nome = 'Maria'
    numero = '1234'

    nomes = ['Maria', 'Lucas', 'Mateus']

    return render(request, "agenda/index.html", {
        'nome': nome, # Tem que tá entre aspas e com dois pontos no final
        'numero': numero,
        'nomes': nomes
    })
```

No arquivo 'index.html':

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="{% static 'agenda/styles.css' %}" />
    <title>Document</title>
  </head>
  <body>
    <h1>Agenda telefonica</h1>

    <ul>
      <li>{{nome}} - {{numero}}</li>
    </ul>

    <h1>Nomes</h1>

    <ul>
      {% for pessoas in nomes %}
      <!-- Tem que abrir e fechar com 'endfor' -->

      <li>{{pessoas}}</li>

      {% endfor %}
    </ul>
  </body>
</html>
```

# Como usar o IF e ELSE

No arquivo 'views.py':

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contatos(request, id):
    nome = 'Maria'
    numero = '1234'

    nomes = ['Maria', 'Lucas', 'Mateus']

    lista_de_contatos = {1: {'nome': 'Maria', 'numero': 1234,
                        2: {'nome': 'João', 'numero': 23423}
                        }}

    if id in lista_de_contatos:

        return render(request, "agenda/index.html", {
            'nome': lista_de_contatos[id]['nome'], # Tem que tá entre aspas e com dois pontos no final
            'numero': lista_de_contatos[id]['numero'],
            'nomes': nomes,
            'contato': True
        })

    else:
        return render(request, "agenda/index.html", {
            'contato': False
        })
```

No arquivo 'index.html':

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'agenda/styles.css' %}"> 
    <title>Document</title>
</head>
<body>

    <h1>Agenda telefonica</h1>
    
    {% if contato %}
    <ul>
        <li>{{nome}} - {{numero}}</li> 
    </ul>

    {% else %}

    <h2>Não existe contatos cadastrados</h2>

    {% endif %}

    <h1>Nomes</h1>

    <ul>
        {% for pessoas in nomes %}

        <li>{{pessoas}}</li>

        {% endfor %}
    </ul>

</body>
</html>
```

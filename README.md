# Iniciar um projeto Django

django-admin startproject nomedoprojeto

# Iniciar um app no Django

python manage.py startapp nomedoaplicativo

# Rodar um projeto Django

python manage.py runserver

# Como pegar parâmetros na Url

Tem que ir no app e criar um arquivo chamado 'urls.py' e escrever o código:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:id>/", views.contatos, name="contatos"), # Como passar um parametro pela URL
]
```


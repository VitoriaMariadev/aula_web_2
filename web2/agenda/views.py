from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contatos(request, id):

    nomes = ['Maria', 'Lucas', 'Mateus']

    lista_de_contatos = {1: {'nome': 'Maria', 'numero': 1234}, 
                        2: {'nome': 'João', 'numero': 23423}}
    
    if id in lista_de_contatos:

        return render(request, "agenda/index.html", {
            'nome': lista_de_contatos[id]['nome'], # Tem que tá entre aspas e com dois pontos no final
            'numero': lista_de_contatos[id]['numero'],
            'nomes': nomes,
            'contato': True
        })

    else:
        return render(request, "agenda/index.html", {
            'nomes': nomes,
            'contato': False 
        })
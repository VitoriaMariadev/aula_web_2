from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(resquest):

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    data = data_e_hora_em_texto[:10]
    horas = data_e_hora_em_texto[10:16]
    dia = data_e_hora_em_texto[:2]
    mes = data_e_hora_em_texto[3:5]
    ano = data_e_hora_em_texto[6:10]
    hora = data_e_hora_em_texto[10:13]
    mes = int(mes)
    hora = int(hora)

    estacao = ''
    horario = ''

    if 3 <= mes <= 6:
        estacao = 'outono'
    elif 7 <= mes <= 9:
        estacao = 'inverno'
    elif    10 <= mes <= 12:
        estacao = 'primavera'
    else:
        estacao = 'verao'

    if 0 <= hora < 6:
        horario = 'madrugada'
    elif 6 <= hora < 12:
        horario = 'meio-dia'
    elif 12 <= hora < 18:
        horario = 'tarde'
    else:
        horario = 'noite'

    estacao, horario = tempo_definido()

    return render(resquest, "newyear/index.html", {
        'estacao': estacao,
        'horario': horario,
        'data': data,
        'horas': horas,
    })

def tempo_definido():
    horario = 'tarde'
    estacao = 'primavera'
    return estacao,horario

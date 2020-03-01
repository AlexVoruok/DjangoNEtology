from os import listdir
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime, time


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    current_time = datetime.now().isoformat(sep='T', timespec='minutes')
    msg = f'Текущее  время: <p> {current_time}'

    return HttpResponse(msg)


def workdir_view(request):

    list_dir = listdir()
    mes = ('<br>').join(list_dir)

    return HttpResponse(mes)

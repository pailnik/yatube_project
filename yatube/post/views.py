from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'post/index.html'
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, template, context)


def group_list(request):
    template = 'post/group_list.html'
    return render(request, template)


def group_detail(requests, pk):
    return HttpResponse(f'Пост номер {pk}')

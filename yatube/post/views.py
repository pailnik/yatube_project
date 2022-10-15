from django.http import HttpResponse


def index(requests):
    return HttpResponse('Главная странциа')


def group_list(requests):
    return HttpResponse('Список постов')


def group_detail(requests, pk):
    return HttpResponse(f'Пост номер {pk}')
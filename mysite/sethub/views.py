from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Sethub

nav = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Контакты', 'url': 'contact'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Логин', 'url': 'login'},
    {'name': 'Добавить пост', 'url': 'add'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request):
    posts = Sethub.objects.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'nav': nav,
        'posts': posts,
    }

    return render(request, 'sethub/index.html', context=data)


def about(request):
    return render(request, 'sethub/about.html', { 'title': 'О нас', 'nav': nav })


def contact(request):
    return render(request, 'sethub/contact.html', { 'title': 'Контакты', 'nav': nav })


def login(request):
    return render(request, 'sethub/login.html', { 'title': 'Логин', 'nav': nav })


def add_post(request):
    return render(request, 'sethub/add.html', { 'title': 'Добавить пост', 'nav': nav })


def show_post(request, post_slug):
    post = get_object_or_404(Sethub, slug=post_slug)
    data = {
        'title': post.title,
        'nav': nav,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'sethub/post.html', data)


def show_category(request, category_id):
    return index(request)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
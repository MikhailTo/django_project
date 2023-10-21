from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    #t = render_to_string('sethub/index.html')
    #return HttpResponse(t)
    return render(request, 'sethub/index.html')


def about(request):
    return render(request, 'sethub/about.html')


def catalog(request, cat_id):
    return HttpResponse(f"<h1>Каталог {cat_id}</h1>")


def catalog_by_slug(request, cat_slug):
    if request.GET:
        for key, value in zip(request.GET.keys(), request.GET.values()):
            print(key, '=', value, end='|')
    return HttpResponse(f"<h1>Каталог {cat_slug}</h1>")


def archive(request, year):
    if year not in range(1990, 2023):
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам: {year}</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
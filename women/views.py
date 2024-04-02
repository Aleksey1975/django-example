from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def index(request):
    return render(request, 'women/index.html')


def categories(request, cat_id):
    return render(request, 'women/cats.html')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'Категория по слагу:  {cat_slug}')


def archives(request, year):
    if int(year) > 3999:
        uri = reverse('cat_slug', args=('disco',))
        return redirect(uri)
    if int(year) > 2999:
        return redirect('cat_slug', 'music')
    if int(year) > 2024:
        # return redirect('home', permanent=True)
        return redirect(index)

    return HttpResponse(f'Архив по годам  {year}')


def converter(request, year):
    if year > 55555:
        raise Http404()
    return HttpResponse(f'Converter {year}')

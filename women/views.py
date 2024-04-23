from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.defaultfilters import slugify
from .models import *
from .forms import *


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def about(request):
    context = {'title': 'О сайте',
               'menu': menu,
               'menu_selected': 'О сайте',
               }
    return render(request, 'women/about.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def categories(request, cat_id):
    return render(request, 'women/cats.html')


# def categories_by_slug(request, cat_slug):
#     cats = Category.objects.filter(women2__is_published=True).distinct()
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Women2.objects.filter(is_published=True, cat=category)
#
#     data = {
#         'menu': menu,
#         'posts': posts,
#         'cats': cats,
#         'cat_slug': cat_slug,
#         'title': cat_slug,
#         'cat_selected': cat_slug,
#         'category': category,
#
#     }
#
#     return render(request, 'women/index.html', data)


def show_category(request, post_slug):
    category = get_object_or_404(Category, slug=post_slug)
    tags = Tag.objects.filter(tags__is_published=True).distinct()
    women = Women2.objects.filter(cat__slug=post_slug, is_published=True).select_related('cat')
    categories = Category.objects.filter(posts__is_published=True).distinct()
    if not women:
        raise Http404()

    context = {
        'cat_selected': post_slug,
        'title': category.name,
        'women': women,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'women/index.html', context=context)


def show_post(request, post_slug):
    tags = Tag.objects.filter(tags__is_published=True).distinct()
    categories = Category.objects.filter(posts__is_published=True).distinct()
    post = get_object_or_404(Women2, slug=post_slug)
    post_tags = post.tag.all()

    context = {
        'post': post,
        'title': post.title,
        'categories': categories,
        'tags': tags,
        'post_tags': post_tags,
    }
    return render(request, 'women/post.html', context)


def show_tag(request, tag_slug):
    categories = Category.objects.filter(posts__is_published=True).distinct()
    tag = get_object_or_404(Tag, slug=tag_slug)
    women = Women2.objects.filter(tag__slug=tag_slug, is_published=True)
    tags = Tag.objects.filter(tags__is_published=True).distinct()

    if not women:
        raise Http404()

    context = {
        'categories': categories,
        'title': tag.name,
        'women': women,
        'tags': tags,
        'tag_selected': tag_slug,

    }
    return render(request, 'women/index.html', context=context)




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


def index(request):
    categories = Category.objects.filter(posts__is_published=True).distinct()
    women = Women2.objects.filter(is_published=True).select_related('cat')
    tags = Tag.objects.filter(tags__is_published=True).distinct()

    context = {
        'cat_selected': 0,
        'title': 'женщины',
        'women': women,
        'categories': categories,
        'selected': 1,
        'tags': tags,

    }
    return render(request, 'women/index.html', context=context)

#
# def show_post(request, post_slug):
#     cats = Category.objects.all()
#     post = get_object_or_404(Women2, slug=post_slug)
#
#     data = {
#         'menu': menu,
#         'post': post,
#         'title': post.title,
#         'cats': cats,
#
#     }

#    return render(request, 'women/post.html', data)


def addpage(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women2.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста!')
    else:
        form = AddPost()

    categories = Category.objects.filter(posts__is_published=True).distinct()
    women = Women2.objects.filter(is_published=True).select_related('cat')
    tags = Tag.objects.filter(tags__is_published=True).distinct()

    context = {
        'form': form,
        'cat_selected': 0,
        'title': 'Добавление статьи',
        'menu_selected': "Добавить статью",
        'women': women,
        'categories': categories,
        'selected': 1,
        'tags': tags,

    }
    return render(request, 'women/add_page.html', context=context)



def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

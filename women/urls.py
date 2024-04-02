from django.urls import path, re_path, register_converter
from women.views import *
from . import converters

register_converter(converters.FiveDigitYearConverter, 'year5')


urlpatterns = [
    # path('', index, name='home'),
    path('<year5:year>/', converter),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archives),
    path('cats/<int:cat_id>/', categories),
    path('cats/<slug:cat_slug>/', categories_by_slug, name='cat_slug'),

    path('', index, name='home'),  # http://127.0.0.1:8000
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),

]

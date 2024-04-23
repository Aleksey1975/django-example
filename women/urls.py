from django.urls import path, re_path, register_converter
from women.views import *
from . import converters
from django.conf import settings
from django.conf.urls.static import static


register_converter(converters.FiveDigitYearConverter, 'year5')


urlpatterns = [
    # path('', index, name='home'),
    path('<year5:year>/', converter),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archives),
    path('cats/<int:cat_id>/', categories, name='cats'),
    path('category/<slug:post_slug>/', show_category, name='category'),
    path('tag/<slug:tag_slug>/', show_tag, name='tag'),

    path('', index, name='home'),  # http://127.0.0.1:8000
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),

]



# handler404 = PageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf.urls import handler404
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap
from . import views

sitemaps = {
    'static': StaticSitemap
}

urlpatterns = [
    path('', views.index, name='index'),
    path('home-decor', views.home_decor, name='home-decor-gallery'),
    path('kitchen-decor', views.kitchen_decor, name='kitchen-decor-gallery'),
    path('shatters-gallery', views.shatters_gallery, name='shatters-gallery'),
    path('form', views.form, name='form'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('404', views.error_404, name='404'),
    path('get-form/<str:name>/<int:phone>/<str:email>', views.get_form, name='form-url'),
    path('register-telegram/<str:user_name>/<int:user_id>', views.registration_telegram)
]

# handler404 = views.error_404

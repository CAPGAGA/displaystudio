from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home-decor', views.home_decor, name='home-decor-gallery'),
    path('kitchen-decor', views.kitchen_decor, name='kitchen-decor-gallery'),
    path('shatters-gallery', views.shatters_gallery, name='shatters-gallery'),
    path('form', views.form, name='form'),
    path('404', views.error_404, name='404'),
    path('get-form', views.get_form, name='form-url'),
]

# handler404 = views.error_404

from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home-decor', views.home_decor, name='home-decor-gallery'),
    path('kitchen-decor', views.kitchen_decor, name='kitchen-decor-gallery'),
    path('shatters-gallery', views.shatters_gallery, name='shatters-gallery'),
    path('form', views.form, name='form'),
    path('get-form', views.get_form, name='form-url'),
]


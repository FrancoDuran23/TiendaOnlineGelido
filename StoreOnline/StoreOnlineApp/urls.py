from django.urls import path
from StoreOnlineApp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('servicios',views.servicios,name="servicios"),
    path('productos',views.productos,name="productos"),
    path('sabores',views.sabores,name="sabores"),
    path('blog',views.blog,name="blog"),
]

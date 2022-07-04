
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('my_page/', views.my_page, name='my_page'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('company/', views.company, name='company'),
    path('design/', views.design, name='design'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
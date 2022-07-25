from random import betavariate
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/post/', views.post, name='post'),
    path('categories/', views.category, name='category'),
    path('category/', views.category_pages, name='category_page'),
    # about us page
    path('about/', views.about, name='about')
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact_api),
    path('contact-list/', views.contactList),
    path('contact-detail/<str:pk>/', views.contactDetail),
    path('contact-create/', views.contactCreate),
    # contact taklif
    path('contact-taklif/', views.contactTaklifAPI),
    # contact shikoyat
    path('contact-shikoyat/', views.contactShikoyatAPI),
    path('contact-search/', views.contactSearch),
    path('contact-order/', views.contactOrder),
    path('contact-update/<str:pk>/', views.contactUpdate),
    path('contact-delete/<str:pk>/', views.contactDelete),
    # path('pagina/', views.some),
    path('post-lists/', views.postAPI_lists),
    path('post-detail/<str:pk>/', views.postDetail),
    path('post-create/', views.postCreate),
    path('post-update/<str:pk>/', views.postUpdate),
    path('post-delete/<str:pk>/', views.postDelete),
    path('user-lists/', views.UserLists)
]

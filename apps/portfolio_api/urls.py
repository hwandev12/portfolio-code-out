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
    path('contact-update/', views.contactUpdate),
    path('contact-delete/<str:pk>/', views.contactDelete),
]

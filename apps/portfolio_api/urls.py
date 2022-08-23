from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.contact_api),
    path('contact-list/', views.contactList),
    path('contact-detail/<str:pk>/', views.contactDetail),
    path('contact-create/', views.contactCreate),
    path('contact-update/', views.contactUpdate),
    path('contact-delete/<str:pk>/', views.contactDelete),
]

from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
	path("", views.dashboard, name='dashboard_home'),
	path("create-user/", views.create_user, name='create_user')
]
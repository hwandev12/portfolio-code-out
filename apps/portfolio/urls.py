from django.urls import path, include
from . import views
from apps.authentication.views import signup, login, profile
from django.contrib.auth.views import LogoutView

app_name = 'blog'

# import rest_frameworks facts
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'contact', views.ContactList)




urlpatterns = [
    path('api-contact/', views.contact_api),
    # path('<int:pk>/api-contacts/', views.contact_detail),
    path('api-auth/', include('rest_framework.urls',  namespace='rest_framework')),
    path('', views.home, name='home'),
    path('<int:pk>/post/', views.post, name='post'),
    path('categories/', views.category, name='category'),
    path('category/', views.category_pages, name='category_page'),
    # about us page
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("profile/", profile, name='profile')
]

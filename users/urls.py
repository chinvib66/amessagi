from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('dashboard/', views.dashboard,name = 'dashboard'),
    path('login/', auth_views.login,{'template_name':'registration/login.html'} ,name='login'),
    path('logout/', auth_views.logout, name='logout'),
]
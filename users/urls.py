from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('dashboard/', views.dashboard,name = 'dashboard'),
    path('login/', views.loginU,name='login'),
    path('logout/', views.logoutU, name='logout'),
]
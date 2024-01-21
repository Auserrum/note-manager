from django.urls import path, include
from web import views
from django.urls import path
from django.contrib.auth import views as auth_views
from authorize import views as auth
from . import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', auth.register, name='register'),

    path('add/', views.add, name="add"),
    path('completed/<int:id>/', views.completed, name="completed"),
]

from django.contrib.auth.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.register, name='users_register'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.home,name = "blog_list"),
    path('post/<int:post_id>/',views.blog_detail,name='post_detail'),
     path('login/', auth_views.LoginView.as_view(), name='login'),  # صفحه ورود
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # صفحه خروج
    path('dashboard/', views.dashboard, name='dashboard'),  # صفحه داشبورد پس از ورود
]
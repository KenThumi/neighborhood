from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('addprof/<int:id>',views.addprof, name='addprof'),
    path('profile/', views.profile, name='profile'),
    path('police', views.getPoliceDept, name='police'),
    path('health', views.getHealthDept, name='health')

]
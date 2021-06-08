from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('addprof',views.addprof, name='addprof'),
    path('profile/', views.profile, name='profile'),
    path('police', views.getPoliceDept, name='police'),
    path('health', views.getHealthDept, name='health'),
    path('depts', views.getDepts, name='depts'),
    path('postform',views.createPost, name='postform'),
    path('updatelocation', views.updateLocation, name='updatelocation'),
    path('search', views.search, name='search'),
    path('neighbours', views.getNeighbours, name='neighbours')

]
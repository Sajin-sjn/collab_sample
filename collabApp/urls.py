from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.public_login,name='public_login'),
    path('signup',views.signup,name='signup'),
    path('user_home',views.user_home,name='user_home'),
    path('admin_home',views.admin_home,name='admin_home'),
]
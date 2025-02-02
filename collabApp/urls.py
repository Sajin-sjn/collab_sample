from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.public_login,name='public_login'),
    path('signup',views.signup,name='signup'),
    path('admin_home',views.admin_home,name='admin_home'),
]
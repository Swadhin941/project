from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login.html',views.login,name='login'),
    path("Register.html",views.register,name='register'),
    path("post.html",views.post,name='post'),
    path('regsub',views.regsub, name='regsub'),
    path('log',views.log, name='log'),
    path('cp',views.cp,name='cp'),
    path('search',views.search, name='search'),
    path('Home/logout',views.logout, name='logout'),
]
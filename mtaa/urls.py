from django.urls import path,re_path
from . import views


urlpatterns = [
    path('home/',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    path('profile/',views.get_profile,name='profile'),
    path('mtaa/',views.neighbourhood,name='mtaa'),
    path('searched/',views.search,name='search'),
    path('update/',views.news,name='news'),
    path('logout/',views.logout,name='logout')    
]

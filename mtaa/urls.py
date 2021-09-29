from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('profile/',views.get_profile,name='profile')
]

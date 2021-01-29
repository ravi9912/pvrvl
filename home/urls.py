from django.urls import path
from django.conf.urls import url
from .views import *#homepage,login,logout,mainmenu,otp_verification
app_name='home'

urlpatterns = [
    path('homepage/',homepage,name='homepage'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('mainmenu/',mainmenu,name='mainmenu'),
    path('login/home/otp_verification/',otp_verification,name='otp_verification'),
    path('create_new_user/',create_new_user,name='create_new_user'),
    #path('calculator/',calculator,name='calculator'),
    path('masterlogin/',masterlogin,name='masterlogin'),
    
]
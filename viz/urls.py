from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name='viz-home'),
    path('',views.respNI,name='viz-respNI'),
    path('signUp/',views.showSignUp,name='viz-showSignUp'),
    path('signIn/',views.showSignIn,name='viz-showSignIn'),
]

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home,name='viz-home'),
    path('',views.respNI,name='viz-respNI'),
    path('signUp/',views.showSignUp,name='viz-showSignUp'),
    path('signIn/',auth_views.LoginView.as_view(template_name='HTML/signIn.html'),name='viz-showSignIn'),
    path('signOut/',auth_views.LogoutView.as_view(template_name='HTML/signOut.html'),name='viz-showSignOut'),
    path('profile/',views.profile,name='viz-profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
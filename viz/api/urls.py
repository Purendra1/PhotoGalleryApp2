from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

urlpatterns = [
    path('albums/',AlbumListAPIView.as_view(),name='viz-api-albumList'),
    path('albums/public/',PublicAlbumListAPIView.as_view(),name='viz-api-publicAlbumList'),
    path('photos/public/',PublicPhotoListAPIView.as_view(),name='viz-api-publicPhotoList'),
    path('photos/',PhotoListAPIView.as_view(),name='viz-api-photoList'),
    path('albums/<pk>/',AlbumDetailAPIView.as_view(),name='viz-api-albumDetails'),
    path('photos/<pk>/',PhotoDetailAPIView.as_view(),name='viz-api-photoDetails'),
    path('albums/<pk>/update/',AlbumUpdateAPIView.as_view(),name='viz-api-updateAlbum'),
    path('albums/<pk>/delete/',AlbumDeleteAPIView.as_view(),name='viz-api-deleteAlbum'),
    path('photos/<pk>/update/',PhotoUpdateAPIView.as_view(),name='viz-api-updatePhoto'),
    path('photos/<pk>/delete/',PhotoDeleteAPIView.as_view(),name='viz-api-deletePhoto'),
    path('album/create/',AlbumCreateAPIView.as_view(),name='viz-api-createAlbum'),
    path('albums/<pk>/addPhoto/',PhotoCreateAPIView.as_view(),name='viz-api-createPhoto'),
    path('signUp/',UserCreateAPIView.as_view(),name='viz-api-SignUp'),
    path('signIn/',UserLoginAPIView.as_view(),name='viz-api-SignIn'),
    path('signOut/',UserLogoutAPIView.as_view(),name='viz-api-SignOut'),
    path('profile/',ProfileAPIView.as_view(),name='viz-api-profile'),
    path('home/',LoginHomeView.as_view(),name='viz-api-home'),
    path('userCreated/',UserCreatedView.as_view(),name='viz-api-resp'),
    path('changePassword/',changePassword,name='viz-api-passwordChange'),
    path('getCSRFToken/',GetCSRFTokenAPIView.as_view(),name='viz-api-getCSRFToken'),
    path('getAuthToken/', obtain_auth_token, name='viz-api-getAuthToken'), 

]

'''
urlpatterns = [
    path('',views.home,name='viz-home'),
    path('',views.respNI,name='viz-respNI'),
    path('signUp/',views.showSignUp,name='viz-showSignUp'),
    path('albums/',views.AlbumListView.as_view(),name='viz-albums'),
    path('albums/<pk>/',views.AlbumDetailView.as_view(),name='viz-showAlbum'),
    path('albums/<pk>/update/',views.AlbumUpdateView.as_view(),name='viz-updateAlbum'),
    path('albums/<pk>/delete/',views.AlbumDeleteView.as_view(),name='viz-deleteAlbum'),
    path('album/create/',views.AlbumCreateView,name='viz-createAlbum'),
    path('photo/create/',views.PhotoCreateView.as_view(),name='viz-createPhoto'),
    path('photos/<pk>/',views.PhotoDetailView.as_view(),name='viz-showPhoto'),
    path('signIn/',auth_views.LoginView.as_view(template_name='HTML/signIn.html'),name='viz-showSignIn'),
    path('signOut/',auth_views.LogoutView.as_view(template_name='HTML/signOut.html'),name='viz-showSignOut'),
    path('profile/',views.profile,name='viz-profile'),
    path('photos/<pk>/update/',views.PhotoUpdateView.as_view(),name='viz-updatePhoto'),
    path('photos/<pk>/delete/',views.PhotoDeleteView.as_view(),name='viz-deletePhoto'),
    path('changePassword/',views.changePassword,name='viz-passwordChange')

]
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
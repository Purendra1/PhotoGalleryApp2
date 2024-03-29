from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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
    path('album/<pk>/photo/create/',views.PhotoCreateViewInAlbum.as_view(),name='viz-createPhotoInAlbum'),
    path('photos/<pk>/',views.PhotoDetailView.as_view(),name='viz-showPhoto'),
    path('signIn/',auth_views.LoginView.as_view(template_name='HTML/signIn.html'),name='viz-showSignIn'),
    path('signOut/',auth_views.LogoutView.as_view(template_name='HTML/signOut.html'),name='viz-showSignOut'),
    path('profile/',views.profile,name='viz-profile'),
    path('photos/<pk>/update/',views.PhotoUpdateView.as_view(),name='viz-updatePhoto'),
    path('photos/<pk>/delete/',views.PhotoDeleteView.as_view(),name='viz-deletePhoto'),
    path('changePassword/',views.changePassword,name='viz-passwordChange')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
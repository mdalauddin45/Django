from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.AlbumAddView.as_view(), name='album'),
    path('edit/<int:pk>',views.EditAlbumView.as_view(), name='edit_album'),
    path('delete/<int:pk>',views.DeleteAlbumView.as_view(), name='delete_album'),
]
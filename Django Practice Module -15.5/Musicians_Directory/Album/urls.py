from django.urls import path
from .import views
urlpatterns = [
    path('',views.album, name='album'),
    path('edit/<int:id>',views.edit_album, name='edit_album'),
    path('delete/<int:id>',views.delete_album, name='delete_album'),
]

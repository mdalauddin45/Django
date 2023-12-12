from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home' ),
    path('category/<slug:category_slug>/', views.home,name='category_wise_post' ),
    path('accounts/',include('author.urls')),
    path('post/',include('post.urls')),
    path('catigory/',include('categories.urls')),
]

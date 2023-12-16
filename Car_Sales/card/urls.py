from django.urls import path
from .import views

urlpatterns = [
    path('details/<int:id>',views.DetailsPostView.as_view(), name='details_post'),
    path('purchase/<int:id>/', views.purchase, name='purchase_car'),
]
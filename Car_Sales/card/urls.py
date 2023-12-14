from django.urls import path,include
from .import views

urlpatterns = [
    path('details/<int:id>',views.DetailsPostView.as_view(), name='details_post'),
    path('purchase/<int:id>/', views.PurchaseCarView.as_view(), name='purchase_car'),
]
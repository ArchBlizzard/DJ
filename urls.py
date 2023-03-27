from django.urls import path
from .views import order_list, order_detail, OrderCreate, OrderUpdate, OrderDelete, favorite_toggle

urlpatterns = [
    path('', order_list, name='order_list'),
    path('<int:pk>/', order_detail, name='order_detail'),
    path('add/', OrderCreate.as_view(), name='order_add'),
    path('<int:pk>/edit/', OrderUpdate.as_view(), name='order_edit'),
    path('<int:pk>/delete/', OrderDelete.as_view(), name='order_delete'),
    path('<int:pk>/favorite_toggle/', favorite_toggle, name='favorite_toggle'),
]

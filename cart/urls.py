from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:cart_item_id>/<int:new_quantity>/', views.update_cart_item, name='update_cart_item'),
    path('remove/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
]

from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('history/', views.order_history, name='order_history'),
    path('return/<int:order_id>/', views.return_request, name='return_request'),
]

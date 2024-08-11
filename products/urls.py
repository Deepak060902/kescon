from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('search/', views.search_products, name='search_products'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/add-review/', views.add_review, name='add_review'),

]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
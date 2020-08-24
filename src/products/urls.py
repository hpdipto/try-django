from django.urls import path
from .views import render_initial_data, dynamic_lookup_view, product_create_view, product_detail_view, product_delete_view, product_list_view


app_name = 'products'
urlpatterns = [
    path('initial/', render_initial_data, name='product initial data'),
    path('create/', product_create_view, name='product create view'),
    # path('', product_detail_view, name='product-detail'),
    path('<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list'),
]
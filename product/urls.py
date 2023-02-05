from django.urls import path

from product.views import create_product, list_products, ProductDeleteView, ProductUpdateView




urlpatterns = [
    path('create-product/', create_product),
    path('list-products/', list_products),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

]








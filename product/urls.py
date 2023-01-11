from django.urls import path

from product.views import create_product, list_products


urlpatterns = [
    path('create-product/', create_product),
    path('list-products/', list_products),

]




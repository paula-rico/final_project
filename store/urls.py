from django.urls import path

from store.views import create_store, list_stores


urlpatterns = [
    path('create-store/', create_store),
    path('list-stores/', list_stores),

]
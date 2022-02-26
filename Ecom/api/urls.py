from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('products/', include("api.product.urls")),
    path('category/', include("api.category.urls")),
]

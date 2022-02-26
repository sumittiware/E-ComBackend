from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductsView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view())
]

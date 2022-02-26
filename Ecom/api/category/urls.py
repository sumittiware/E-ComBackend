from django.contrib import admin
from django.urls import path
from .views import CategoryListView, CategoryAdminView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<int:pk>/', CategoryAdminView.as_view()),
]

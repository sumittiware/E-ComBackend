from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer
# Create your views here.


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_class = (
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser,
    )
    serializer_class = CategorySerializer
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from .pagination import ProductPaginatonClass
from .permissions import IsAdminOrReadOnly


class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPaginatonClass


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all().order_by('id')
    # check what is the issue with this permission part
    permissions = (IsAdminOrReadOnly, )
    serializer_class = ProductDetailSerializer

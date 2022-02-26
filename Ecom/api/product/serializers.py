from rest_framework import serializers
from .models import Product
from ..category.serializers import CategorySerializer


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   allow_null=True,
                                   required=False)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock',
            'is_active',
            'image',
            'category',
            'metadata',
            'created_at',
            'updated_at',
        )


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,
                                   allow_empty_file=False,
                                   allow_null=True,
                                   required=False)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'image',
            'category',
        )

from django.db import models
from tinymce import models as tmc
from ..category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = tmc.HTMLField()
    price = models.FloatField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    metadata = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        'name',
        'price',
        'stock',
    ]

    def __str__(self):
        return self.name
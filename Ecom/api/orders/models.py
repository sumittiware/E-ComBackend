from django.db import models
from ..user.models import CustomUser
# Create your models here.


class Orders(models.Model):
    items = models.JSONField()
    price = models.FloatField(null=False, default=0.0)
    payment_id = models.CharField(max_length=150, default=0)
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment_id

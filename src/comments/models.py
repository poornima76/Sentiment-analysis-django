from django.db import models
from products.models import Product
from profiles.models import Profile
# Create your models here.

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    prediction = models.IntegerField(name='prediction') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"product: {self.product.name},profile: {self.profile.user},comment: {self.text} "

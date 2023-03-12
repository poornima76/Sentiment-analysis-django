from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    synopsis = models.CharField(max_length=1000)
    tags = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    # auto_now=True

    def __str__(self):
        return f"{self.name}-{self.synopsis}-{self.tags}-{self.release_date.strftime('%d/%m/%Y')}"
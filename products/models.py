from django.db import models

# Create your models here.
class Category(models.Model):
    """Product categories model fields"""

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model fields"""

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    shoe_size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

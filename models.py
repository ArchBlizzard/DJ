from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])

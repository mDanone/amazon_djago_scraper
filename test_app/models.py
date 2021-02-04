from django.db import models


class Merchant(models.Model):
    business_name = models.CharField(max_length=64)
    merchant_id = models.CharField(max_length=16, unique=True)
    rating = models.FloatField(blank=True, null=True)
    review_count = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    node_id = models.IntegerField(null=True, blank=True)
    merchant_url = models.CharField(max_length=256, default='url', null=True, blank=True)

    def __str__(self):
        return self.business_name


class Product(models.Model):
    date_scrapped = models.DateField(null=True, blank=True)
    product_name = models.CharField(max_length=256, default='seller')
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, default=None)
    price = models.FloatField(null=True, blank=True)
    num_of_reviews = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    num_of_elements = models.IntegerField(null=True, blank=True)

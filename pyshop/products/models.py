from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)   # Standard length for urls

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.name

class Offer(models.Model):

    code = models.CharField(max_length=20)
    description = models.TextField()
    discount = models.FloatField()

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.code

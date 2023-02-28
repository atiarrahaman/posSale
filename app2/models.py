from django.db import models

# Create your models here.



class Product(models.Model):
    item_name=models.CharField(max_length=250)
    price=models.PositiveBigIntegerField()
    slug=models.CharField(max_length=250)
    status=models.BooleanField()
    def __str__(self):
        return self.item_name

class Suplyer(models.Model):
    sypplyer_name = models.CharField(max_length=250)

    def __str__(self):
        return self.sypplyer_name
    


class ProductInput(models.Model):
    item_name=models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.PositiveIntegerField()
    sypplyer_name=models.ForeignKey(Suplyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.sypplyer_name.sypplyer_name


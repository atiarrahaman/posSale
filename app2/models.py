from django.db import models

# Create your models here.



class Product(models.Model):
    item_name=models.CharField(max_length=250,)
    price=models.PositiveBigIntegerField()
    qty=models.IntegerField(default=0)
    slug=models.CharField(max_length=250)
    status=models.BooleanField()

   
    
    def __str__(self):
        return self.item_name

    
    
   
    

class Suplyer(models.Model):
    sypplyer_name = models.CharField(max_length=250)

    def __str__(self):
        return self.sypplyer_name
    


class ProductInput(models.Model):
    item_name=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='productInputs')
    qty=models.PositiveIntegerField()
    price=models.PositiveIntegerField(default=0)
    sypplyer_name=models.ForeignKey(Suplyer, on_delete=models.CASCADE,related_name='suppylers')
   
    def __str__(self):
        return self.sypplyer_name.sypplyer_name
    @property
    def Gross_amount(self):
       return self.price*self.qty
    @property
    def vatamount(self):
       temp=(self.price*self.qty)
       vat=(temp*15/100)
       return vat
    @property
    def totalAmount(self):
       temp=(self.price*self.qty)
       vat=(temp*15/100)
       amount=(temp+vat)
       return amount

    
    
    


class ProductInputCart(models.Model):
    item=models.ForeignKey('ProductInput', on_delete=models.CASCADE)


class Client(models.Model):
    client_name=models.CharField(max_length=250,default='company name')
    tax_number=models.IntegerField(default=0)


class PosSale(models.Model):
    item=models.ForeignKey('Product', on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)

    @property
    def possale_total(self):
     return self.qty * self.item.price
    
    @property
    def vatcost(self):
     temp=( self.qty * self.item.price)
     vat=(temp*15/100)
     return vat
    
    @property
    def Total_amount(self):
     temp=( self.qty * self.item.price)
     vat=(temp*15/100)
     totalamount=(temp+vat)
     return totalamount
    
    


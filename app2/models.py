from django.db import models
from django.utils import timezone
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
    item=models.ForeignKey('Product', on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)


class Client(models.Model):
    client_name=models.CharField(max_length=250,default='company')
    tax_number=models.IntegerField(default=300950786200003)


class PosSale(models.Model):
    item=models.ForeignKey('Product', on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    Discount_price=models.FloatField(default=0)
    date=models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.date = timezone.now()
        return super(PosSale, self).save(*args, **kwargs)



     
    @property
    def gross_price(self):
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
     totalamount=(temp+vat - self.Discount_price)
     return totalamount
    


class CheckOut(models.Model):
    possale=models.ForeignKey(PosSale, on_delete=models.CASCADE,blank=True ,null=True)
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_date= models.DateTimeField(auto_now_add=True)
    qty=models.PositiveIntegerField(default=1)
    date=models.DateTimeField(blank=True, null=True)
    

    @property
    def Total_amount(self):
     temp=( self.qty * self.item.price)
     vat=(temp*15/100)
     totalamount=(temp+vat)
     return totalamount
    



class AddExpenseMony(models.Model):
    Money=models.PositiveIntegerField()
    reason=models.CharField(max_length=200)
    date=models.DateTimeField()
    def __str__(self):
        return self.Money
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.date = timezone.now()
        return super(AddExpenseMony, self).save(*args, **kwargs)

class AddTrasctions(models.Model):
    money=models.PositiveIntegerField()
    reason=models.CharField(max_length=200)
    date=models.DateTimeField()
   
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.date = timezone.now()
        return super(AddTrasctions, self).save(*args, **kwargs)

   
class BuyProduct(models.Model):
    money=models.PositiveIntegerField()
    supplyer=models.ForeignKey(Suplyer, on_delete=models.CASCADE)
    date=models.DateTimeField()
    def __str__(self):
        return self.supplyer.sypplyer_name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.date = timezone.now()
        return super(BuyProduct, self).save(*args, **kwargs)



class AddCash(models.Model):
    add_money=models.PositiveIntegerField()
    Reason=models.CharField(max_length=200)
    date=models.DateTimeField()
   
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.date = timezone.now()
        return super(AddCash, self).save(*args, **kwargs)

   
from django import forms
from .models import *

class ProductAddForm(forms.ModelForm):
    class Meta:
        model= Product
        fields ='__all__'
        widgets={
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty':forms.NumberInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            
        }


class ProductInputForm(forms.ModelForm):
    
    class Meta:
        model=ProductInput
        fields='__all__'
        widgets={
            'item_name': forms.Select(attrs={'class': 'form-control'}),
            'qty':forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sypplyer_name':forms.Select(attrs={'class': 'form-control'}),
        }


class PosSaleForm(forms.ModelForm):
    class Meta:
        model=PosSale
        fields='__all__'
      
        exclude=['Discount_price','date']
        widgets={
            # 'item': forms.Select(attrs={'class': 'form-control'}),
            # 'qty':forms.NumberInput(attrs={'class': 'form-control'}),
            
        }

    
class AddCompanyNameForm(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'
        
        widgets={
             'client_name': forms.TimeInput(attrs={'class': 'form-control'}),
             'tax_number':forms.NumberInput(attrs={'class': 'form-control'}),
            
        }


    
class AddExpenseMonyForm(forms.ModelForm):
    class Meta:
        model=AddExpenseMony
        fields=['Money','reason']
        
        
        widgets={
             'Money': forms.NumberInput(attrs={'class': 'form-control'}),
             'reason':forms.Textarea(attrs={'class': 'form-control'}),
            
        }

class AddTrasctionsForm(forms.ModelForm):
    class Meta:
        model=AddTrasctions
        fields=['money','reason']
        widgets={
             'money': forms.NumberInput(attrs={'class': 'form-control'}),
             'reason':forms.Textarea(attrs={'class': 'form-control'}),
            
        }

class BuyProductForm(forms.ModelForm):
    class Meta:
        model=BuyProduct
        fields=['money','supplyer']
        widgets={
             'money': forms.NumberInput(attrs={'class': 'form-control'}),
             'supplyer':forms.Select(attrs={'class': 'form-control'}),
            
        }



class AddCashForm(forms.ModelForm):
    class Meta:
        model=AddCash
        fields=['add_money','Reason']
        widgets={
             'add_money': forms.NumberInput(attrs={'class': 'form-control'}),
             'Reason':forms.Textarea(attrs={'class': 'form-control'}),
            
        }
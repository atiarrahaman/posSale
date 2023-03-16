from django import forms
from .models import Product , ProductInput ,PosSale,Client

class ProductAddForm(forms.ModelForm):
    class Meta:
        model= Product
        fields ='__all__'


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
        exclude=['Discount_price']
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
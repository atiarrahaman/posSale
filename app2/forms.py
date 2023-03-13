from django import forms
from .models import Product , ProductInput ,PosSale

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
        widgets={
            'item': forms.Select(attrs={'class': 'form-control'}),
            'qty':forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
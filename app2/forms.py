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


class PosSaleForm(forms.ModelForm):
    class Meta:
        model=PosSale
        fields='__all__'
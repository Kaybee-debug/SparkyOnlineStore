from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model =Product
        # fields = "__all__"
        fields = (
            'item',
            'description',
            'price',
            'image',
            
        )
      
        # widgets ={
        #     "item": forms.TextInput(attrs={'class':'form-control'}),
        #     "description": forms.TextInput(attrs={'class':'form-control'}),
        #     "price": forms.TextInput(attrs={'class':'form-control'}),
        # }
       
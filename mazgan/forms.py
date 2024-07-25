from django import forms
from parler.forms import TranslatableModelForm
from .models import Bid

class BidForm(TranslatableModelForm):
    class Meta:
        model = Bid
        fields = '__all__'
        widgets = {
             'email': forms.EmailInput(attrs={
                     'class': "form-control",
                     'placeholder': 'optional'
             }),
             'phone': forms.TextInput(attrs={
                 'class': "form-control",
                 'placeholder': 'optional'
             }),
             'text': forms.Textarea(attrs={
                'class': "form-control",
                 'rows': '3'
             }),
         }
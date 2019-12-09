from django import forms
from .models import billing

class BillingForm(forms.ModelForm):
    class Meta:
        model = billing
        fields = ['compania', 'adultos', 'ninos', 'alojamiento', 
                  'text', 'email', 'titulo']
        widgets = {
           'compania': forms.Select(attrs={'class':'form-control'}),
           'alojamiento': forms.Select(attrs={'class':'form-control'}),
           'text': forms.Textarea(attrs={'class':'form-control','rows':10}),
           'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
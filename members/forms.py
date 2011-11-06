from django import forms

class AdhesionForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)

from django import forms

class StoreForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    region = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()


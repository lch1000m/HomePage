
from django import forms

class MyForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)

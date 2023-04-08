from django import forms

class CarSearchForm(forms.Form):
    license_plate = forms.CharField(max_length=10)
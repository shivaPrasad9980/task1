from django import forms 
from . models import SalesData

class SalesForm(forms.ModelForm):
    class Meta:
        model = SalesData
        fields = "__all__"
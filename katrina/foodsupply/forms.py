from django import forms
from django.forms import ModelForm
from .models import household

class householdForm(ModelForm):
    class Meta:
        model = household
        fields = "__all__"

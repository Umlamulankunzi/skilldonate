from django.db import transaction
from django import forms
from app_auth.models import Charity




class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    city = forms.CharField(widget=forms.TextInput())
    country = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Charity
        fields = ('name', 'description', 'city', 'country')

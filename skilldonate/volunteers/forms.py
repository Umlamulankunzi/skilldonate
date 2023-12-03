from django import forms
from app_auth.models import Volunteer



class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(label="Last name",widget=forms.TextInput(), required=False)
    phone = forms.CharField(label="Phone", widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    country = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Volunteer
        fields = ('name', 'last_name', 'phone', 'city', 'country')

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import Charity, Volunteer, User
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    # email = forms.EmailField(widget=forms.EmailInput())
    # password = forms.CharField(widget=forms.PasswordInput())
    pass

class VolunteerSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    country = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_volunteer = True
        if commit:
            user.save()
        volunteer = Volunteer.objects.create(
            user=user,
            name=self.cleaned_data.get('name'),
            last_name=self.cleaned_data.get('last_name'),
            phone=self.cleaned_data.get('phone'),
            city=self.cleaned_data.get('city'),
            country=self.cleaned_data.get('country'),
            )
        return user


class CharitySignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    city = forms.CharField(widget=forms.TextInput())
    country = forms.CharField(widget=forms.TextInput())


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_charity = True
        if commit:
            user.save()
        charity = Charity.objects.create(
            user=user, name=self.cleaned_data.get('name'),
            description=self.cleaned_data.get('description'),
            city=self.cleaned_data.get('city'),
            country=self.cleaned_data.get('country'),
            )
        return user





# class QuestionForm(forms.ModelForm):
#     question = forms.CharField(widget=forms.Textarea())

#     class Meta:
#         model = Question
#         fields = ('question',)

# class AnswerForm(forms.ModelForm):
#     answer = forms.CharField(widget=forms.Textarea())

#     class Meta:
#         model = Answer
#         fields = ('answer',)

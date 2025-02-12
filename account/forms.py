from django import forms
from account.models import User

class RegistrationForm(forms.ModelForm):
    c_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "w-full my-3 rounded-md"}), label="Confirm Password")
    class Meta:
        model = User
        fields = ["name", "email", "country", "age","password"]
        widgets = {"country": forms.Select(attrs={"class" : "w-full my-3 rounded-md"})}
from django import forms
from account.models import User

# Signup Form 
class RegistrationForm(forms.ModelForm):
    c_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "w-full my-3 rounded-md"}), label="Confirm Password")
    class Meta:
        model = User
        fields = ["name", "email", "country", "age","password"]
        widgets = {"country": forms.Select(attrs={"class" : "w-full my-3 rounded-md"}),"password": forms.PasswordInput(attrs={"class" : "w-full my-3 rounded-md"})}
    
    def clean(self):
        cleaned_data =  super().clean()
        password, c_password = [cleaned_data.get("password"),cleaned_data.get("c_password")]
        if(password!=c_password):
            self.add_error("c_password","Password and confirm password doesn't match")

# Login Form 
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255,widget=forms.EmailInput(attrs={"class":"w-full my-3 rounded-md"}))
    password = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={"class":"w-full my-3 rounded-md"}))
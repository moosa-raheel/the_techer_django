from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from account.utils import send_email
from django.contrib import messages
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user_name = form.cleaned_data.get("name")
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            send_email(email,user_name)
            messages.success(request,"Check your email for verify and activate your account")
            redirect("register")
    else:
        form = RegistrationForm()
    return render(request,"account/register.html",{"form" : form})
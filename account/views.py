from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from account.utils import send_email
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from django.urls import reverse
from account.models import User
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
            uuid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_url = reverse("verify_user",kwargs={"uuid":uuid,"token":token})
            activation_link = f"{settings.SITE_DOMAIN}{activation_url}"
            send_email(email,user_name,activation_link)
            messages.success(request,"Check your email for verify and activate your account")
            redirect("register")
    else:
        form = RegistrationForm()
    return render(request,"account/register.html",{"form" : form})

def verify_user(request,uuid,token):
    pk = force_str(urlsafe_base64_decode(uuid))
    user = User.objects.get(pk=pk)
    if default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
    return HttpResponseRedirect("/")
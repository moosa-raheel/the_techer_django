from django.shortcuts import render
from account.forms import RegistrationForm
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
    else:
        form = RegistrationForm()
    return render(request,"account/register.html",{"form" : form})
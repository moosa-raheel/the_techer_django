from django.urls import path
from account import views

urlpatterns = [
    path("register/",views.register,name="register"),
    path("verify/<str:uuid>/<str:token>",views.verify_user, name="verify_user")
]

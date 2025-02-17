from django.urls import path
from account import views

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("verify/<str:uuid>/<str:token>",views.verify_user, name="verify_user")
]

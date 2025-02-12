from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("",include("base.urls")),
    path("account/",include("account.urls")),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]

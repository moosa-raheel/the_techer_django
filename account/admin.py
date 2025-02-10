from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ['id','name','email','age','is_active']
    ordering = ['id','age']
    list_filter = ['is_active','is_superuser','is_staff']
    filter_horizontal = []
    readonly_fields = ["created_at","updated_at"]
    fieldsets = (
        ('User Credentials', {"fields":['email','password']}),
        ('Personal Information', {"fields": ['name','country','age']}),
        ('Permissions',{"fields": ['is_superuser','is_staff','is_active']}),
        ('Important Dates',{"fields": ['created_at','updated_at','last_login']})
    )
    search_fields = ['name','email']
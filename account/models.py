from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

COUNTRY_CHOICES = (
    ('pakistan','Pakistan'),
    ('india','India'),
    ('america','America'),
    ('china','China'),
    ('japan','Japan'),
    ('others','Others')
)

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError("user must have an email address")
        user = self.model(email=self.normalize_email(email=email),**kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have is_staff True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser True")
        user = self.create_user(email,password,**extra_fields)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, unique=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES)
    age = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    def has_perm(self,perms):
        return self.is_superuser
    
    def has_module_perms(self,app_label,obj=None):
        return self.is_superuser
from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER = (
    ("female", "Female"),
    ("male", "Male")
)

class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    username  = models.CharField(max_length=200)
    email     = models.EmailField(unique=True)
    phone     = models.CharField(max_length=200)
    gender    = models.CharField(max_length=100,choices=GENDER)
    otp       = models.CharField(max_length=100,blank=True,null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
    

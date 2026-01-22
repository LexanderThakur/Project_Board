from django.db import models

# Create your models here.


class User(models.Model):
    user_email=models.EmailField(unique=True)
    user_password=models.CharField(max_length=255)



    
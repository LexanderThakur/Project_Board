from django.db import models

from accounts.models import User
# Create your models here.

class Projects(models.Model):

    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=False)

    name=models.CharField(max_length=255,null=False,unique=True)
    description=models.CharField(max_length=500)
    created_at= models.DateField(auto_now_add=True,null=False)


class Tasks(models.Model):

    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    compeleted=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)

    
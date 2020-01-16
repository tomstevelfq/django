from django.db import models

class Mes(models.Model):
    mid=models.AutoField(primary_key=True)
    url=models.CharField(max_length=128)

class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    passwd=models.CharField(max_length=128)

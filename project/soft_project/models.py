from django.db import models

# Create your models here.

class keys(models.Model):
    key=models.CharField(max_length=100)
    id1=models.IntegerField(primary_key=True)

class files(models.Model):
    file=models.CharField(max_length=100)
    id1 = models.ForeignKey(keys,on_delete=models.CASCADE)
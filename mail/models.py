from django.db import models

class User(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=10,default="")
    mo_num=models.BigIntegerField()
    email=models.TextField(max_length=40)
    pas=models.TextField(max_length=20)

    def __str__(self):
        return self.name


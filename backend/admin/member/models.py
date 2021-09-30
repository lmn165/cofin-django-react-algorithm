from django.db import models

# Create your models here.
from dataclasses import dataclass


class MemberVo(models.Model):
    username = models.TextField(primary_key=True)
    pwd = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()
    birth = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.username}'


    # class Meta:
    #     manage = True
    #     db_table = 'users'

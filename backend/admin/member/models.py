from django.db import models


class Member(models.Model):
    use_in_migrations = True
    username = models.CharField(primary_key=True, max_length=10)
    pwd = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()
    birth = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.username}'
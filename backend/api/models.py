from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    tg_id = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.tg_id


class Event(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserTemp:
    name = ''
    surname = ''
    number = ''
    context = []

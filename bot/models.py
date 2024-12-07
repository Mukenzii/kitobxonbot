from django.db import models
from django.contrib.auth.models import User

class Bot_users(models.Model):
    telegram_id = models.IntegerField()
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    phone_number = models.IntegerField(unique=True)
    is_blocked = models.BooleanField()
    is_superuser = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Bot_pages(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField()
    file = models.FileField()
    is_blocked = models.BooleanField()
    sort = models.IntegerField()
    created_by = models.DateTimeField(auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



class Bot_langs(models.Model):
    title = models.CharField(max_length=30, unique=True)
    is_blocked = models.BooleanField()
    created_by = models.DateTimeField(auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)




class Bot_settings(models.Model):
    title = models.CharField(max_length=80, unique=True)
    body = models.TextField()
    created_by = models.DateTimeField(auto_created=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)







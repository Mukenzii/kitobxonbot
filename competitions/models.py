from django.db import models
from django.contrib.auth.models import User

class Competitions_list(models.Model):
    title = models.CharField(max_length=140, unique=True)
    body = models.TextField()
    image = models.ImageField()
    file = models.FileField()
    url = models.URLField()
    lang_id = models.IntegerField()
    start_on_date = models.DateTimeField()
    start_at_time = models.DateTimeField()
    end_on_date = models.DateTimeField()
    end_at_time = models.DateTimeField()
    is_blocked = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_created=True )
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)



class Competitions_shares(models.Model):
    competition_id = models.IntegerField()
    channel_group_id = models.IntegerField(unique=True)
    shared_on = models.DateTimeField(auto_now_add=True)
    shared_by = models.ForeignKey(User,on_delete=models.CASCADE)







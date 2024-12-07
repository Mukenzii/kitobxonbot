from django.db import models
from django.contrib.auth.models import User


class Quiz_levels(models.Model):
    competition_id = models.IntegerField()
    title = models.CharField(max_length=120, unique=True)
    body = models.TextField()
    image = models.ImageField()
    file = models.FileField()
    url = models.URLField()
    lang_id = models.IntegerField(unique=True)
    start_on_date = models.DateTimeField()
    start_at_time = models.DateTimeField()
    end_on_date = models.DateTimeField()
    end_at_time = models.DateTimeField()
    is_blocked = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Quiz_level_exams(models.Model):
    quiz_level_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=120, unique=True)
    lang_id = models.IntegerField(unique=True)
    level_exam_weight = models.FloatField()
    number_of_questions = models.IntegerField()
    time_to_solve_exam = models.TimeField()
    is_blocked = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)




class Quiz_exam_questions(models.Model):
    quiz_exam_id = models.IntegerField()
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    image = models.ImageField()
    file = models.FileField()
    url = models.URLField()
    lang_id = models.IntegerField(unique=True)
    is_blocked = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)





















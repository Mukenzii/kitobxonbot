# Generated by Django 5.1.3 on 2024-12-05 18:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=140, unique=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
                ('url', models.URLField()),
                ('lang_id', models.IntegerField()),
                ('start_on_date', models.DateTimeField()),
                ('start_at_time', models.DateTimeField()),
                ('end_on_date', models.DateTimeField()),
                ('end_at_time', models.DateTimeField()),
                ('is_blocked', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Competitions_shares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_id', models.IntegerField()),
                ('channel_group_id', models.IntegerField(unique=True)),
                ('shared_on', models.DateTimeField(auto_now_add=True)),
                ('shared_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

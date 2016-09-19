# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 19:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PossibleAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='text of the answer')),
                ('is_true', models.BooleanField(default=False, help_text='correct answer')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='text of the question')),
                ('number', models.PositiveSmallIntegerField(help_text='serial number of task')),
                ('question_type', models.CharField(choices=[('aud', 'Audio'), ('vid', 'Video'), ('txt', 'Text')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test', to='quizapi.Subject')),
                ('tasks', models.ManyToManyField(related_name='tests', to='quizapi.Task')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_answer', models.DateTimeField(auto_now=True)),
                ('answers', models.ManyToManyField(related_name='user_answers', to='quizapi.PossibleAnswer')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='quizapi.Task')),
                ('test', models.ManyToManyField(related_name='user_answers', to='quizapi.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='possibleanswer',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='possible_answers', to='quizapi.Task'),
        ),
    ]
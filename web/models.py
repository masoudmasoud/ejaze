from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    question_text = models.CharField(max_length=200)

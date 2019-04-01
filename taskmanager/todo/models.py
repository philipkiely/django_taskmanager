from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Each task is owned by one user
    description = models.CharField(max_length=150) #Each task has a description of what needs to be done
    due = models.DateField() #Each task has a due date, which is a Python datetime.date

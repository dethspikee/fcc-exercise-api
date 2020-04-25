from django.db import models
from datetime import date
# Create your models here.

class UserAPIModel(models.Model):
    _id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.username


class Exercise(models.Model):
    user = models.ForeignKey(UserAPIModel, on_delete=models.CASCADE, related_name='logs')
    description = models.CharField(max_length=50)
    duration = models.IntegerField(null=False)
    date = models.DateField(blank=True, null=True, default=date.today)





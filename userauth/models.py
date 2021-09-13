from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.  
class Training(models.Model):
    date = models.DateField()
    bench = models.PositiveIntegerField(blank=True, null=True)
    squats = models.PositiveIntegerField(blank=True, null=True)
    pullups = models.PositiveIntegerField(blank=True, null=True)
    deadlift = models.PositiveIntegerField(blank=True, null=True)
    militarypress = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f'Training by {self.user} on {self.date}'


from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import UserAdmin


# Create your models here.


class User(AbstractUser):
    Star_H = models.FloatField(null= True, blank=True)
    Star_R = models.FloatField(null= True, blank=True)
    Star_T = models.FloatField(null= True, blank=True)

    def __str__(self):
        return f"{self.username}"


class Field(models.Model):
    Name = models.CharField(max_length=50) 

    def __str__(self):
        return f"<Name> {self.Name}> "

class Event(models.Model):
    Creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Event_creator")
    Date = models.DateField(max_length=10) 
    Sport = models.CharField(max_length=10)
    Field = models.ForeignKey(Field, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"<Date> {self.Date}> Sport: {self.Sport} "


class Subscription(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Match_field")
    Event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"<Subscription> "




    
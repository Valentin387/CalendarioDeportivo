from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    User.username=models.CharField(max_length=20)
    User.password = models.CharField(max_length=20)
    Star_H = models.FloatField()
    Star_R = models.FloatField()
    Star_T = models.FloatField()

    def __str__(self):
        return f"<User>: "


class Field(models.Model):
    Name = models.CharField(max_length=50) 

    def __str__(self):
        return f"<Name> {self.Name}> "

class Event(models.Model):
    Creator = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="Event_creator")
    Date = models.DateField(max_length=10) 
    Sport = models.CharField(max_length=10)
    Field = models.ForeignKey(Field, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"<Date> {self.Date}> Sport: {self.Sport} "


class Subscription(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="Match_field")
    Event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"<Subscription> "




    
from django.db import models

# Create your models here.

class User(models.Model):
    Password = models.CharField(max_length=10)
    User_Type = models.CharField(max_length=10)
    UserName = models.CharField(max_length=10)
    Star_H = models.FloatField()
    Star_R = models.FloatField()
    Star_T = models.FloatField()

    def __str__(self):
        return f"<UserType> {self.User_Type}> User: {self.UserName}"


class Event(models.Model):
    Creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Event_creator")
    Date = models.DateField(max_length=10) 
    Sport = models.CharField(max_length=10)
    Field = models.ForeignKey(Field, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"<Date> {self.Date}> Sport: {self.Sport} "


class Field(models.Model):
    Name = models.CharField(max_length=50) 

    def __str__(self):
        return f"<Name> {self.Name}> "

class Subscription(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Match_field")
    Event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"<Subscription> "




    
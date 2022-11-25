from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
from users.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    #password = models.CharField(_("password"), max_length=128)
    email = models.EmailField(_('email address'), unique=True)
    #is_staff = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    #date_joined = models.DateTimeField(default=timezone.now)
    
    Star_H = models.FloatField(null= True, blank=True)
    Star_R = models.FloatField(null= True, blank=True)
    Star_T = models.FloatField(null= True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} "


class Field(models.Model):
    Name = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.Name} "

class Event(models.Model):
    Creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="Event_creator")
    Name = models.CharField(max_length=50)
    Date = models.DateField(max_length=10) 
    Sport = models.CharField(max_length=10)
    Field = models.ForeignKey(Field, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"{self.Name} "


class Subscription(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="Match_field")
    Event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name="Match_field")

    def __str__(self):
        return f"{self.id} "




    
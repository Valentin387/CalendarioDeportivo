from django.contrib import admin

from .models import Profile, Event, Field, Subscription
# Register your models here.

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Field)
admin.site.register(Subscription)

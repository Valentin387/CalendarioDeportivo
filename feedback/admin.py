from django.contrib import admin

from .models import User, Event, Field, Subscription
# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Field)
admin.site.register(Subscription)

from django import forms
from users.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = []

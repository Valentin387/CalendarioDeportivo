from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("GoToProfile", views.GoToProfile, name="GoToProfile"),
    path("CreateNewEvent", views.CreateNewEvent, name="CreateNewEvent"),
]
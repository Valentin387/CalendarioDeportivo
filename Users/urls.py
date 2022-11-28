from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("RegisterAccount", views.RegisterAccount, name="register"),
    path("GoToFeedback", views.GoToFeedback, name="GoToFeedback"),
    path("CreateNewEvent", views.CreateNewEvent, name="CreateNewEvent"),
    path("GoToAdmin", views.GoToAdmin, name="GoToAdmin"),
    path('<app>/<action>/<subscription_id>/',views.detail, name='detail'),
]
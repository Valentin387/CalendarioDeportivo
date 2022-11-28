from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import CustomUser

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/profile.html")
    
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:index"))

def RegisterAccount(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        newUser = CustomUser.objects.get(email=email)
        if newUser is None:
            newUser = CustomUser.objects.create_user(email, password)
            newUser.save()
        else:
            return render(request, "users/login.html", {
                "message": "That email is not available"
            })
        return HttpResponseRedirect(reverse("users:index"))

def GoToFeedback(request):
   # lleveme a la app feedback/templates/index.html
   r = redirect("feedback:index")
   return r

def CreateNewEvent(request):
    r = redirect("feedback:CreateNewEvent")
    return r

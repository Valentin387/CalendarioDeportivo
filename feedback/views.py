from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
"""
def index(request):
    return render(request, "index.html")
"""
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "index.html")

def GoToProfile(request):
    r = redirect("users:index")
    return r

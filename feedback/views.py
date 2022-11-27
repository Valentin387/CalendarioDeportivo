from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, "index.html")


def GoToProfile(request):
    r = redirect("users:login")
    return r

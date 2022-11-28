from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from feedback.forms import EventForm

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


def CreateNewEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "NewEvent.html")
    else:
        form = EventForm()
    return render(request, 'index.html', {'form': form})

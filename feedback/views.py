from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from feedback.forms import EventForm
from users.models import Event, CustomUser, Field
from django.http import HttpResponse

# Create your views here.
"""
def index(request):
    return render(request, "index.html")
"""
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    else:
        table=Event.objects.select_related("Creator","Field") #you can do just: select_related()
        return HttpResponse(render(request, "index.html", {
            "events":table
        }))

def GoToProfile(request):
    r = redirect("users:index")
    return r


def CreateNewEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thanks.html")
    else:
        form = EventForm()
    return render(request, 'NewEvent.html', {'form': form})



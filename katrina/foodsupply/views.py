from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import pandas as pd
import datetime
from .models import Hub, household
from django.views import generic
from .forms import householdForm
"""
class IndexView(generic.ListView):
    def __init__(self, arg):
        superIndexView, self).__init__()
        self.arg = arg

"""

def index(request):
    #all_albums = Album.objects.all()
    #context = {'all_albums': all_albums}
    return render(request, 'foodsupply/index.html')
    #return HttpResponse("Hello, world. You're at the foodsupply index.")

def household(request):
    return render(request, 'foodsupply/household.html')

def hub(request):
    return render(request, 'foodsupply/hub.html')

def add_household(request):
    if request.method == 'POST':
        form = householdForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'foodsupply/thankyou.html')

def view_household(request):
    df = pd.DataFrame(list(Hub.objects.all().values()))
    all_hub = Hub.objects.all()
    context = {'all_hub': all_hub}
    return render(request, 'foodsupply/view_household.html', context)


"""
df = pd.DataFrame(list(BlogPost.objects.filter(date__gte=datetime.datetime(2012, 5, 1)).values()))

# limit which fields
df = pd.DataFrame(list(BlogPost.objects.all().values('author', 'date', 'slug')))
"""

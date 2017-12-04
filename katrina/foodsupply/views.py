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

def household_main(request):
    return render(request, 'foodsupply/household.html')

def hub(request):
    """
    Excuse the really disgusting redundancy, it was 3:30AM, and I had run out of juice
    """
    household_df = pd.DataFrame(list(household.objects.all().values()))
    hub_1 = dict()
    hub_1['house_count']=0
    hub_1['population']=0

    hub_2 = dict()
    hub_2['house_count']=0
    hub_2['population']=0

    hub_3 = dict()
    hub_3['house_count']=0
    hub_3['population']=0

    for ele,house in household_df.iterrows():
        if(house['household_id']> 0 and house['household_id'] < 6):
            hub_1['house_count']+=1
            hub_1['population']+=int(house['house_population'])
        elif(house['household_id']> 5 and house['household_id'] < 11):
            hub_2['house_count']+=1
            hub_2['population']+=int(house['house_population'])
        else:
            hub_3['house_count']+=1
            hub_3['population']+=int(house['house_population'])
    print("PROBLEM 2!!!")
    hub_db_1 = Hub.objects.get(pk=1)
    hub_db_1.population = hub_1['population']
    hub_db_1.save()
    hub_db_2 = Hub.objects.get(pk=2)
    hub_db_2.population = hub_1['population']
    hub_db_2.save()
    hub_db_3 = Hub.objects.get(pk=3)
    hub_db_3.population = hub_1['population']
    hub_db_3.save()

    hub_1['days_to_exhaustion'] = round(hub_db_1.current_storage/hub_1['population'],0)
    hub_2['days_to_exhaustion'] = round(hub_db_2.current_storage/hub_2['population'],0)
    hub_3['days_to_exhaustion'] = round(hub_db_3.current_storage/hub_3['population'],0)

    hub_1['critical_score'] = round(1/hub_1['days_to_exhaustion']*hub_1['population']/2,0)
    hub_2['critical_score'] = round(1/hub_2['days_to_exhaustion']*hub_2['population']/2,0)
    hub_3['critical_score'] = round(1/hub_3['days_to_exhaustion']*hub_3['population']/2,0)

    context = {'hub_1':hub_1, 'hub_2':hub_2, 'hub_3':hub_3}
    return render(request, 'foodsupply/hub.html',context)

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

def report_1(request):
    house_list = list(household.objects.all().values())
    hub_1_houses = []
    hub_1 = dict()
    hub_1['house_count']=0
    hub_1['population']=0
    for house in house_list:
        if(house['household_id']> 0 and house['household_id'] < 6):
            hub_1_houses.append(house)
            hub_1['house_count']+=1
            hub_1['population']+=int(house['house_population'])
    hub_db_1 = Hub.objects.get(pk=1)
    hub_1['days_to_exhaustion'] = round(hub_db_1.current_storage/hub_1['population'],0)
    hub_1['critical_score'] = round(1/hub_1['days_to_exhaustion']*hub_1['population']/2,0)
    context = {'hub_1_houses': hub_1_houses, 'hub_1': hub_1}
    return render(request, 'foodsupply/report_hub_1.html', context)

def report_2(request):
    house_list = list(household.objects.all().values())
    hub_2_houses = []
    hub_2 = dict()
    hub_2['house_count']=0
    hub_2['population']=0
    for house in house_list:
        if(house['household_id']> 5 and house['household_id'] < 11):
            hub_2_houses.append(house)
            hub_2['house_count']+=1
            hub_2['population']+=int(house['house_population'])
    hub_db_2 = Hub.objects.get(pk=1)
    hub_2['days_to_exhaustion'] = round(hub_db_2.current_storage/hub_2['population'],0)
    hub_2['critical_score'] = round(1/hub_2['days_to_exhaustion']*hub_2['population']/2,0)
    context = {'hub_2_houses': hub_2_houses, 'hub_2': hub_2}
    return render(request, 'foodsupply/report_hub_2.html', context)

def report_3(request):
    house_list = list(household.objects.all().values())
    hub_3_houses = []
    hub_3 = dict()
    hub_3['house_count']=0
    hub_3['population']=0
    for house in house_list:
        if(house['household_id']> 10):
            hub_3_houses.append(house)
            hub_3['house_count']+=1
            hub_3['population']+=int(house['house_population'])
    hub_db_3 = Hub.objects.get(pk=1)
    hub_3['days_to_exhaustion'] = round(hub_db_3.current_storage/hub_3['population'],0)
    hub_3['critical_score'] = round(1/hub_3['days_to_exhaustion']*hub_3['population']/2,0)
    context = {'hub_3_houses': hub_3_houses, 'hub_3': hub_3}
    return render(request, 'foodsupply/report_hub_3.html', context)

def optimization(request):
    hub_list = list(Hub.objects.all().values())
    hub_json_list=list()
    for hub in hub_list:
        #print(hub)
        hub_json = dict()
        hub_json['current_storage'] = hub['current_storage']
        hub_json['population'] = hub['population']
        hub_json['hub_id'] = hub['hub_id']
        hub_json['days_to_exhaust'] = round(hub['current_storage']/hub['population'],0)
        hub_json['critical_score'] = round(1/hub_json['days_to_exhaust']*hub['population']/2,0)
        #print(hub_json)
        hub_json_list.append(hub_json)
        hub_df = pd.DataFrame(hub_json_list)
    optimize = get_optimize(hub_df)
    context = {'optimize': optimize}
    print(context)
    return render(request, 'foodsupply/optimization.html', context)

def get_optimize(hub_df):
    critical_hub = hub_df.loc[hub_df['critical_score'].idxmax()]
    safe_hub = hub_df.loc[hub_df['critical_score'].idxmin()]
    move_quantity = round((safe_hub['current_storage']-critical_hub['current_storage'])/3,0)
    optimize = {'from_hub':safe_hub['hub_id'],
                'to_hub':critical_hub['hub_id'],
                'move_quantity': move_quantity}

    return(optimize)

"""
df = pd.DataFrame(list(BlogPost.objects.filter(date__gte=datetime.datetime(2012, 5, 1)).values()))

# limit which fields
df = pd.DataFrame(list(BlogPost.objects.all().values('author', 'date', 'slug')))
"""

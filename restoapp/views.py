from django.shortcuts import render
from restoapp.models import resto,dish
import json
# Create your views here.

def index(request):
    name_list = []
    location_list = []
    items_list = []

    search_data = resto.objects.all()
    all_dish = dish.objects.all()
    details_list = []
    for item in search_data:
        f_details = (item.full_details)
        if f_details != 'nan':
            details = {}
            dict1 = json.loads(f_details)
            details["name"] = (dict1['name'])
            details["cuisines"] = (dict1['cuisines'])
            details["address"] = (dict1['location']['address'])
            details["aggregate_rating"] = (dict1['user_rating']['aggregate_rating'])
            details["rating_text"] = (dict1['user_rating']['rating_text'])
            details_list.append(details)
    for data in search_data:
        if data.name not in name_list:
            name_list.append(data.name)
        if data.location not in location_list:
            location_list.append(data.location)
    for data in all_dish:
        if data.dish not in items_list:
            items_list.append(data.dish)
    location_list.sort()
    if request.method=="POST":
        search_location = request.POST.get("location")
        search_data = resto.objects.filter(location=search_location)
        if search_location != "":
            details_list = []
            for item in search_data:
                f_details = (item.full_details)
                if f_details != 'nan':
                    details = {}
                    dict1 = json.loads(f_details)
                    details["name"] = (dict1['name'])
                    details["cuisines"] = (dict1['cuisines'])
                    details["address"] = (dict1['location']['address'])
                    details["aggregate_rating"] = (dict1['user_rating']['aggregate_rating'])
                    details["rating_text"] = (dict1['user_rating']['rating_text'])
                    details_list.append(details)
        if search_location == None:
            search_name = request.POST.get("name")
            search_data = resto.objects.filter(name__icontains=search_name).values()
            if search_name != "":
                details_list=[]
                for item in search_data:
                    f_details=(item['full_details'])
                    if f_details != 'nan':
                        details={}
                        dict1 = json.loads(f_details)
                        details["name"]=(dict1['name'])
                        details["cuisines"]=(dict1['cuisines'])
                        details["address"]=(dict1['location']['address'])
                        details["aggregate_rating"]=(dict1['user_rating']['aggregate_rating'])
                        details["rating_text"]=(dict1['user_rating']['rating_text'])
                        details_list.append(details)
            if search_name == "":
                search_item = request.POST.get("items")
                search_dish = dish.objects.filter(dish__icontains=search_item).values()
                details_list = []
                for dish_id in search_dish:
                    details = {}
                    details["did"]=(dish_id['did'])
                    details["dish"]=(dish_id['dish'])
                    details["mrp"]=("₹"+dish_id['mrp'])

                    dd=(dish_id['did'])
                    id_data=resto.objects.filter(rid=dd)
                    for item in id_data:
                        f_details = (item.full_details)
                        if f_details != 'nan':
                            dict1 = json.loads(f_details)
                            details["name"] = (dict1['name'])
                            details["cuisines"] = (dict1['cuisines'])
                            details["address"] = (dict1['location']['address'])
                            details["aggregate_rating"] = (dict1['user_rating']['aggregate_rating'])
                            details["rating_text"] = (dict1['user_rating']['rating_text'])
                            details_list.append(details)

                if search_item == "":
                    details_list = resto.objects.all()

        context = {'name_list': name_list,'location_list': location_list,
                   'dishs':all_dish,'items_list':items_list,'dict1':details_list}

        return render(request, 'restoapp/index.html', context)

    else:

        context = {'name_list': name_list,'location_list': location_list,
                   'dishs':all_dish,'items_list':items_list,'dict1':details_list}

        return render(request, 'restoapp/index.html', context)




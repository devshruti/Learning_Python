from django.shortcuts import render
import json
# Create your views here.
def menu(request):
    with open('zomato/menu_data.json', 'r') as menu_file:
        menu_data = json.load(menu_file)
    return render(request, "zomato/menu.html", {"menu_data": menu_data})

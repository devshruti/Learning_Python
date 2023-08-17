from django.shortcuts import render, redirect
import json
import time
# Create your views here.
orders_list = []

def generate_unique_order_id():
    timestamp = int(time.time() * 1000)  # Get the current timestamp in milliseconds
    order_id = f"ORDER_{timestamp}"
    return order_id

def menu(request):
    with open('zomato/menu_data.json', 'r') as menu_file:
        menu_data = json.load(menu_file)

    return render(request, "zomato/menu.html", {"menu_data": menu_data, "orders_list": orders_list})

def add_dish(request):
    if request.method == 'POST':
        new_dish_id = int(request.POST['dish_id'])
        new_dish_name = request.POST['dish_name']
        new_dish_price = float(request.POST['dish_price'])
        new_dish_available = request.POST.get('dish_available') == 'on'

        with open('zomato/menu_data.json', 'r') as menu_file:
            menu_data = json.load(menu_file)

        new_dish = {
            "dish_id": new_dish_id,
            "dish_name": new_dish_name,
            "price": new_dish_price,
            "available": new_dish_available
        }

        menu_data.append(new_dish)

        with open('zomato/menu_data.json', 'w') as menu_file:
            json.dump(menu_data, menu_file, indent=4)

        return redirect('menu')

    return render(request, 'zomato/add_dish.html')

def remove_dish(request, dish_id):
    with open('zomato/menu_data.json', 'r') as menu_file:
        menu_data = json.load(menu_file)

    # Find the index of the dish with the given dish_id
    index_to_remove = None
    for index, dish in enumerate(menu_data):
        if dish["dish_id"] == dish_id:
            index_to_remove = index
            break

    if index_to_remove is not None:
        del menu_data[index_to_remove]

        # Save the updated menu data back to the JSON file
        with open('zomato/menu_data.json', 'w') as menu_file:
            json.dump(menu_data, menu_file, indent=4)

    # Return an HttpResponse to indicate a successful response
        return redirect('menu')
    return render(request, "zomato/menu.html")

def update_availability(request, dish_id):
    with open('zomato/menu_data.json', 'r') as menu_file:
        menu_data = json.load(menu_file)

    # Find the dish with the given dish_id
    for dish in menu_data:
        if dish["dish_id"] == dish_id:
            dish["available"] = not dish["available"]
            break

    # Save the updated menu data back to the JSON file
    with open('zomato/menu_data.json', 'w') as menu_file:
        json.dump(menu_data, menu_file, indent=4)

        return redirect('menu')
    return render(request, "zomato/menu.html")



def place_order(request):
    with open('zomato/menu_data.json', 'r') as menu_file:
        menu_data = json.load(menu_file)

    if request.method == 'POST':
        order_dish_ids = request.POST.getlist('order_dish')
        
        # Assuming you have a function to generate a unique order ID
        new_order_id = generate_unique_order_id()

        # Create a new order with the selected dish IDs and initial status
        new_order = {
            'order_id': new_order_id,
            'dishes': [],
            'status': 'Received'
        }
        for dish_id in order_dish_ids:
            # Find the corresponding dish from menu_data and add it to the order
            dish = next((dish for dish in menu_data if dish['dish_id'] == int(dish_id)), None)
            if dish:
                new_order['dishes'].append(dish)

        # Add the new order to the orders list
        orders_list.append(new_order)

        return redirect('menu')

        # return render(request, "zomato/menu.html", {"menu_data": menu_data})

    return render(request, 'zomato/place_order.html', {'menu_data': menu_data})


# ... (other view functions)

def update_order_status(request, order_id):
    global orders_list  # Use the global orders_list

    for order in orders_list:
        if order['order_id'] == order_id:
            order['status'] = 'Preparing'  # Update status to 'Preparing'
            break

    return render(request, "zomato/menu.html", {"orders_list": orders_list})


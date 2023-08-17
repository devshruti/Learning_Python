from django.urls import path 
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'), 
    path('remove_dish/<int:dish_id>/', views.remove_dish, name='remove_dish'),
    path('update_availability/<int:dish_id>/', views.update_availability, name='update_availability'),
    path('place_order/', views.place_order, name='place_order'),
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),

]



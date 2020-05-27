from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='foody'),                                                 #home page
    path('create-foody/', views.add_food, name='createFoody'),                          #add to food
    path('Nutrition/', views.index, name='listFood'),                                   #index of food
    path('Nutrition/<int:pk>/Details/', views.details_food, name='foodDetails'),        #get details for a single food item
    path('Nutrition/<int:pk>/Delete/', views.delete, name='deleteFood'),  #Specific food delete page , pk indicates food
    path('Nutrition/<int:pk>/Edit/', views.edit, name='editFood'),                      #Edit food items
    path('FoodNews/', views.food_news, name='FoodNews'),
    ]
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Nutrition
from .forms import NutritionForm
from django.utils import timezone
import requests                     #necessary for datascraping
from bs4 import BeautifulSoup as BS #necessary for datascraping


# function that renders the home page
def home(request):
    return render(request, 'FoodyApp/food_app_home.html')

#View function that controls the main index page - list of food
def index(request):
    get_food = Nutrition.food.all() #Gets all the current food from the database
    context = {'foods': get_food} #Creates a dictionary object of all the food for the template
    return render(request, 'FoodyApp/food_app_index.html', context)

# view function to add new food to the database
def add_food(request):
    form = NutritionForm(request.POST or None) # gets the posted form, if one exists
    if form.is_valid(): # checks the form for errors, ensures it's filled in
        form.save() # saves the valid form to the database
        return redirect('listFood') # redirects to the home page, which is named 'foody' in the urls
    else:
        print(form.errors) # prints any errors for the posted form to the form to the terminal
        form = NutritionForm()                #Creates a new blank form
    return render(request, 'FoodyApp/food_app_create.html', {'form': form})

#View function to look up the details of the food
def details_food(request, pk):
    pk = int(pk)                                    #Casts value of pk to an int so it's in the proper form
    food = get_object_or_404(Nutrition, pk=pk)      #Gets single instance of the food from the database
    context = {'food':food}                           #Creates dictionary object to pass the food object
    return render(request,'FoodyApp/food_app_details.html', context)

def delete(request, pk):
    pk = int(pk)
    food = get_object_or_404(Nutrition, pk=pk)
    # If user submits, model instance is deleted
    if request.method == 'POST':
        food.delete()
        return redirect('foody')    # returns to food display page
    context = {'food': food}
    return render(request, "FoodyApp/food_app_delete.html", context)

# View function to edit a food item
def edit(request, pk):
    #global form
    pk = int(pk)
    food = get_object_or_404(Nutrition, pk=pk)
    if request.method == 'POST':
        form = NutritionForm(request.POST, instance=food)
        if form.is_valid(): #validation
            food = form.save()
            food.save()
            return redirect('foodDetails', pk=food.pk) #redirects to details page
    else:
        form = NutritionForm(instance=food)
    context = {'form': form, 'pk': pk}
    return render(request, 'FoodyApp/food_app_edit.html', context) #renders to the edit template using the context and request

# view function for data scraping the food website for current news stories
def food_news(request):
    source = requests.get("https://www.foodandwine.com/news") # Get foodandwine.com/news as an html document
    print(source.status_code)                       # used for debugging to ensure a 'success' code of 200
    soup = BS(source.content, 'html.parser')        # Initial processing of the html by beautiful soup, soup is now a navigatable object
    nodes = soup.find_all(class_="category-page-item-content")      # Search for divs with class node-title
    articles = []                                   # create blank array to add articles to
    for i in range(0, 10):                              # iterates through all the objects with class of node-title
        node = nodes[i]
        title = node.find('h3').get_text()           # Sets title equal to the text of the a tag
        link = node.find('a').get('href')             # Sets link equal to the href of the a tag
        url = link  # Modifies the link to a full url, since the links were relative
        article={'title':title, 'url':url}    # Creates an article object dictionary with needed elements
        articles.append(article)                                # Adds article dictionary item to the array before iterating through next node
    context={'articles':articles}                               # Creates a dictionary element for the articles to pass to the template
    return render(request, 'FoodyApp/food_app_news.html', context)




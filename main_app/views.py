from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request):  
	treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})

def home(request):
    context = {'locations': locations}
    return render(request, 'home.html', context)
    

#class Treasure:
#    def __init__(self, name, value, material, location, img_url):
#        self.name = name
#        self.value = value
#        self.material = material
#        self.location = location
#        self.img_url = img_url

class Location:
    def __init__(self, name, predators, num_restaurants, img_url):
        self.name = name
        self.predators = predators
        self.num_restaurants = num_restaurants
        self.img_url = img_url

#treasures = [
#    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",'/static/images/nugget.png'),
#    Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO",'/static/images/fools-gold.png'),
#    Treasure('Coffee Can', 20.00, 'tin', 'Aacme, CA','/static/images/coffee-can.png'),
#]

locations = [
    Location("Fool's Falls, CO", 'Flash Floods', 0,
             'http://courseware.codeschool.com/try_django/images/fools-falls.jpg'),
    Location("Curly's Creek, NM", 'Rattle Snakes', 2,
             'http://courseware.codeschool.com/try_django/images/curlys-creek.jpg'),
    Location("The Delicate Arch, UT", "str", 5, 
             "http://courseware.codeschool.com/try_django/images/delicate-arch.jpg"),
]

from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Animal


# Main app 
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')


##animal resource 

def animals_index(request):
  animal = Animal.objects.all()
  return render(request, 'animals/index.html', {'animal': animal}) #rendeing to folder animas file about
  

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  return render(request, 'animals/detail.html', {'animal': animal})


class AnimalCreate(CreateView):
  model = Animal
  fields = ['name', 'breed', 'preferred_living_conditions']
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'breed', 'preferred_living_conditions']
  success_url = '/animals/'
  

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'














##feed resource 







#equipment resource 




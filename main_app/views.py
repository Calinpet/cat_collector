from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView
from .models import Cat

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })
# The cats_detail function is using the getmethod to obtain the cat object by its id.
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })

# The fieldsattribute is required and can be used to limit or change the ordering of the attributes from the Catmodel are generated in the ModelFormpassed to the template.
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'  
  success_url = '/cats/'
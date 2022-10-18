from django.shortcuts import render
# Add the following import
from .models import Cat

# Define the home view
def home(request):
  '''
  this is where we return a response
  in most cases we render a template
  we will need some data for that template in most cases
  '''
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })
# The cats_detailfunction is using the getmethod to obtain the cat object by its id.
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })
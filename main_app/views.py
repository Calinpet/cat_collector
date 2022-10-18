from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView
from .models import Cat
# Import the FeedingForm
from .forms import FeedingForm
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    # include the cat and feeding_form in the context
    'cat': cat, 'feeding_form': feeding_form
  })

def add_feeding(request, cat_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)  

# The fieldsattribute is required and can be used to limit or change the ordering of the attributes from the Catmodel are generated in the ModelFormpassed to the template.
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'  
  success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'
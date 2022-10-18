from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Cat(models.Model):
  name = models.CharField(max_length=100) 
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

# new code below
  def __str__(self):
      return self.name    

# Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})

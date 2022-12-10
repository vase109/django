from django.shortcuts import render
from .models import Food
from django.views.generic import ListView , DetailView
# Create your views here.

class FoodListView(ListView):
    model=Food
    template_name='food/home.html'
    context_object_name='food'

class FoodDetailView(DetailView):
    model=Food
    template_name='food/detail.html'
    context_object_name='detail'


from django.shortcuts import render
from .models import UserProfile, Food, Entry, DailyReport
from django.views.generic import ListView, DetailView


# Create your views here.

class AllFoodView(ListView):
    model = Food
    template_name = 'project/all_food.html'
    context_object_name = 'foods'

    
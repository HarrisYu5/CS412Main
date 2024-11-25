from django.urls import path
from . import views

urlpatterns = [
    path('food', views.AllFoodView.as_view(), name='all_food'),

]
from django.urls import path
from . import views

#url configuration for hw4 project
urlpatterns = [
    path('hello/', views.hello, name='hello'),
]


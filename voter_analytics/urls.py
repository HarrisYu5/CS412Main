from django.urls import path
from . import views

urlpatterns = [
    path('', views.VoterListView.as_view(), name='home'),
    path('vote', views.VoterListView.as_view(), name='voter'),
    path(r'vote/<int:pk>', views.VoteDetailedView.as_view(), name="voter_detail"),
    path('graph', views.GraphListView.as_view(), name='graph'),
]
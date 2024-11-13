from django.urls import path
from . import views

urlpatterns = [
    path('', views.VoterListView.as_view(), name='home'),
    path('voter', views.VoterListView.as_view(), name='voter'),
    path(r'voter/<int:pk>', views.VoteDetailedView.as_view(), name="voter_detail"),
    path('graphs', views.GraphListView.as_view(), name='graphs'),
]
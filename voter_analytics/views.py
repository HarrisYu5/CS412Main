from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Voter



class VoterListView(ListView):
    model = Voter
    template_name = 'voter_analytics/voter.html'
    context_object_name = 'voters'
    ordering = ['voter_score']
    paginate_by = 100

    def get_queryset(self):
        qs = super().get_queryset()
        if 'party_affiliation' in self.request.GET:
            party_affiliation = self.request.GET['party_affiliation']
            if party_affiliation:
                qs = qs.filter(party_affiliation=party_affiliation)
        if 'min_dob' in self.request.GET:
            min_dob = self.request.GET['min_dob']
            if min_dob:
                qs = qs.filter(dob__gte=f"{min_dob}-01-01")
        if 'max_dob' in self.request.GET:
            max_dob = self.request.GET['max_dob']
            if max_dob:
                qs = qs.filter(dob__lte=f"{max_dob}-12-31")
        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score:
                qs = qs.filter(voter_score=voter_score)
        if 'v20state' in self.request.GET:
            if self.request.GET['v20state']:
                qs = qs.filter(v20state=True)
        if 'v21town' in self.request.GET:
            if self.request.GET['v21town']:
                qs = qs.filter(v21town=True)
        if 'v21primary' in self.request.GET:
            if self.request.GET['v21primary']:
                qs = qs.filter(v21primary=True)
        if 'v22general' in self.request.GET:
            if self.request.GET['v22general']:
                qs = qs.filter(v22general=True)
        if 'v23town' in self.request.GET:
            if self.request.GET['v23town']:
                qs = qs.filter(v23town=True)
        return qs
    
class VoteDetailedView(DetailView):
    model = Voter
    template_name = 'voter_analytics/voter_detail.html'
    context_object_name = 'v'
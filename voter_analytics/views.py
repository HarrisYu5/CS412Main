from typing import Any
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Voter
import plotly 
import plotly.graph_objects as go
import datetime
import math




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

class GraphListView(ListView):
    model = Voter
    template_name = 'voter_analytics/graph.html'
    context_object_name = 'v'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        v=context['v']
        party_affiliation = v.values('party_affiliation')
        year_of_birth = [] #We need to filter out yob from dob
        for voter in v:
            year_of_birth.append(voter.dob.year)
        v20state = list(v.values('v20state'))
        v21town = list(v.values('v21town'))
        v21primary = list(v.values('v21primary'))
        v22general = list(v.values('v22general'))
        v23town = list(v.values('v23town'))
        #--------------------------------------------------------------------
        #Pie Chart for Party Affiliation
        party_count = {} #  In the form {party : num of voter}

        for party in party_affiliation:
            if party['party_affiliation'] in party_count:
                party_count[party['party_affiliation']] += 1
            else:
                party_count[party['party_affiliation']] = 1

        fig = go.Pie(labels=list(party_count.keys()), values=list(party_count.values()))
        pie_div = plotly.offline.plot([fig], output_type='div')

        context['pie_div'] = pie_div


        #--------------------------------------------------------------------
        #Histogram for Year of Birth
        yob_count = {}
        for yob in year_of_birth:
            if yob in yob_count:
                yob_count[yob] += 1
            else:
                yob_count[yob] = 1
        fig = go.Bar(x=list(yob_count.keys()), y=list(yob_count.values()))
        his1_div = plotly.offline.plot([fig], output_type='div')
        context['his1_div'] = his1_div
        #--------------------------------------------------------------------
        #Bar Chart for Voting History
        v20state_count = 0
        v21town_count = 0
        v21primary_count = 0
        v22general_count = 0
        v23town_count = 0

        for voter in v:
            if voter.v20state:
                v20state_count += 1
            if voter.v21town:
                v21town_count += 1
            if voter.v21primary:
                v21primary_count += 1
            if voter.v22general:
                v22general_count += 1
            if voter.v23town:
                v23town_count += 1
        
        election_count = {
            'v20state': v20state_count,
            'v21town': v21town_count,
            'v21primary': v21primary_count,
            'v22general': v22general_count,
            'v23town': v23town_count
        }

        fig=go.Bar(x=list(election_count.keys()), y=list(election_count.values()))
        his2_div = plotly.offline.plot([fig], output_type='div')
        context['his2_div'] = his2_div
        #--------------------------------------------------------------------
        return context
        
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

        





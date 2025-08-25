from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from . import  nba_data

def run_nba(request):
    return HttpResponse("""
        <h1>Welcome to the 24/25 NBA Database</h1>
        <a href='/team-stats/'>Search Team Stats</a>
    """)


def team_stats(request):
    if 'team' in request.GET:
        team = request.GET.get('team').lower()
        # Instead of displaying here, redirect to /team/<team_name>/
        return redirect('team_detail', team_name=team)
    
    return render(request, 'backend/team_stats.html') 


def team_detail(request, team_name):
    team_name = team_name.lower()
    stats = getattr(nba_data, team_name, None)  # get the variable from nba_data.py
    return render(request, 'backend/team_detail.html', {
        'team': team_name,
        'stats': stats,
    })
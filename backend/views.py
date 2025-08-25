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
    teams_dict = nba_data.nba_data()  # Call the function to get the dictionary

    if request.method == "GET" and 'team' in request.GET:
        team = request.GET.get('team').lower()
        if team in teams_dict:
            return redirect('team_detail', team_name=team)
        else:
            # Optional: show a message if the team doesn't exist
            return render(request, 'backend/team_stats.html', {
                'error': f"No data found for team '{team.title()}'",
                'teams': list(teams_dict.keys())
            })

    # If no GET parameter, just show the search form
    return render(request, 'backend/team_stats.html', {
        'teams': list(teams_dict.keys())
    })


def team_detail(request, team_name):
    team_name = team_name.lower()
    
    # Call the function to get the teams dictionary
    teams_dict = nba_data.nba_data()
    
    stats_string = teams_dict.get(team_name, "")  # Get the stats string
    
    # Split the string into lines for the template
    stats = [line.strip() for line in stats_string.strip().split("\n") if line.strip()]
    
    return render(request, 'backend/team_detail.html', {
        'team': team_name.title(),
        'stats': stats,
    })


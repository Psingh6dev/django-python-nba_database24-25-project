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


def parse_team_data(team_string):
    players = []
    for line in team_string.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        # "LeBron James:(24.4 ppg, 8.2 apg, 7.8 rpg, 0.513* fg)"
        if ":" in line:
            name, stats = line.split(":", 1)
            name = name.strip()
            stats = stats.strip("() ")  # remove parentheses
            stat_parts = [s.strip() for s in stats.split(",")]

            player = {"name": name}
            # Assign stats safely
            for part in stat_parts:
                if "ppg" in part:
                    player["ppg"] = part
                elif "apg" in part:
                    player["apg"] = part
                elif "rpg" in part:
                    player["rpg"] = part
                elif "fg" in part.lower():
                    player["fg"] = part
            players.append(player)
    return players



def team_detail(request, team_name):
    teams_dict = nba_data.nba_data()
    team_key = team_name.lower()

    if team_key in teams_dict:
        raw_data = teams_dict[team_key]
        players = parse_team_data(raw_data)

        return render(request, "backend/team_detail.html", {
            "team_name": team_key.title(),
            "players": players,
        })
    else:
        return render(request, "backend/team_detail.html", {
            "team_name": team_key.title(),
            "players": [],
        })



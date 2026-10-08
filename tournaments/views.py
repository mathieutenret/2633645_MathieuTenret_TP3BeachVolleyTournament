from .models import Team, Tournament
from .forms import OnePlayerForm, TwoPlayersForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tournament_list(request):
    tournaments = Tournament.objects.prefetch_related('teams__players').all()

    return render(request, 'tournament_list.html', {'tournaments' : tournaments})

def create_team_one(request):
    if request.method == 'POST':
        team_form = TwoPlayersForm(request.POST)
        player_form = OnePlayerForm(request.POST)

        if team_form.is_valid() and player_form.is_valid():
            tournament = team_form.cleaned_data['tournament']

            if tournament.teams.count() >= 16:
                messages.error(request, 'Impossible de créer cette équipe : le tournoi possède déjà 16 équipes !')
            else:
                team = team_form.save()

                player = player_form.save(commit=False)
                player.team = team
                player.save()

                messages.success(request, "L'équipe a été créée avec succès !")
                return redirect('tournament_list')
    else:
        team_form = TwoPlayersForm()
        player_form = OnePlayerForm()

    return render(request, 'two_players_form.html', {'team_form': team_form, 'player_form': player_form, 'two_players': False})


def create_team_two(request):
    if request.method == 'POST':
        team_form = TwoPlayersForm(request.POST)
        player1_form = OnePlayerForm(request.POST, prefix='player1')
        player2_form = OnePlayerForm(request.POST, prefix='player2')

        if (team_form.is_valid() and player1_form.is_valid() and player2_form.is_valid()):
            tournament = team_form.cleaned_data['tournament']

            if tournament.teams.count() >= 16:
                messages.error(request, 'Impossible de créer cette équipe : le tournoi possède déjà 16 équipes !')
            else:
                team = team_form.save()

                player1 = player1_form.save(commit=False)
                player1.team = team
                player1.save()

                player2 = player2_form.save(commit=False)
                player2.team = team
                player2.save()

                messages.success(request, "L'équipe a été créée avec succès !")
                return redirect('tournament_list')
    else:
        team_form = TwoPlayersForm()
        player1_form = OnePlayerForm(prefix='player1')
        player2_form = OnePlayerForm(prefix='player2')

    return render(request, 'two_players_form.html', {'team_form': team_form, 'player1_form': player1_form, 'player2_form': player2_form, 'two_players': True})

def add_player(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if team.players.count() >= 2:
        messages.error(request, 'Cette équipe possède déjà deux joueurs !')
        return redirect('tournament_list')

    if request.method == 'POST':
        form = OnePlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit=False)
            player.team = team
            player.save()

            messages.success(request, 'Le joueur a été ajouté avec succès !')
            return redirect('tournament_list')
    else:
        form = OnePlayerForm()

    return render(request, 'one_player_form.html', {'form': form, 'team': team})

def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    players = list(team.players.all())
    player1 = players[0] if len(players) >= 1 else None
    player2 = players[1] if len(players) >= 2 else None

    if request.method == 'POST':
        team_form = TwoPlayersForm(request.POST, instance=team)
        player1_form = OnePlayerForm(request.POST, instance=player1, prefix='player1')

        if player2:
            player2_form = OnePlayerForm(request.POST, instance=player2, prefix='player2')
        else:
            player2_form = None

        forms_valid = (team_form.is_valid() and player1_form.is_valid() and (player2_form is None or player2_form.is_valid()))

        if forms_valid:
            new_tournament = team_form.cleaned_data['tournament']

            if (new_tournament != team.tournament and new_tournament.teams.count() >= 16):
                messages.error(request, 'Impossible de déplacer cette équipe : le tournoi possède déjà 16 équipes !')

            else:
                team_form.save()
                player1_form.save()

                if player2_form:
                    player2_form.save()

                messages.success(request, "L'équipe et les joueurs ont été modifiés avec succès !")
                return redirect('tournament_list')
    else:
        team_form = TwoPlayersForm(instance=team)
        player1_form = OnePlayerForm(instance=player1, prefix='player1')

        if player2:
            player2_form = OnePlayerForm(instance=player2, prefix='player2')
        else:
            player2_form = None

    return render(request, 'team_edit.html', {'team': team, 'team_form': team_form, 'player1_form': player1_form, 'player2_form': player2_form})

def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        team.delete()

        messages.success(request, "L'équipe a été supprimée avec succès !")
        return redirect('tournament_list')

    return render(request, 'team_confirm_delete.html', {'team': team})

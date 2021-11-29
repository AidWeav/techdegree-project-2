from constants import PLAYERS
from constants import TEAMS
import random

def menu():
    menu_choice = input("""
    BASKETBALL TEAM STATS TOOL
    -----------MENU-----------
    Here are your choices:
    1: Display Team Stats
    2: Quit
    Enter an option:  """)

    if menu_choice == "1":
        team_stats()
    if menu_choice == "2":
        exit()
    else:
        print("Please choose a valid option")
        menu()


def team_stats():
    team_stats = input("""
    1) Panthers
    2) Bandits
    3) Warriors
    Enter an option: """)

    if team_stats == "1":
        team_stats_answer = "Panthers"
        display_stats(team_stats_answer)
    if team_stats == "2":
        team_stats_answer = "Bandits"
        display_stats(team_stats_answer)
    if team_stats == "3":
        team_stats_answer = "Warriors"
        display_stats(team_stats_answer)
    else:
        print("Please choose a valid option")
        team_stats()


def balance_teams():
    every_team_total = int(len(PLAYERS) / len(TEAMS))
    picked_team_players = random.sample(PLAYERS, every_team_total)
    players = []
    for player in picked_team_players:
        add_player_name = {}
        add_player_name = player["name"]
        players.append(add_player_name)
    return picked_team_players, players


def clean_data():
    players_names = []
    players_guardians = []
    players_experiences = []
    players_height = []
    for player in PLAYERS:
        player_names = player["name"]
        players_names.append(player_names)
        combine_names = "   ".join(players_names)
        player_guardians = player["guardians"].split (' and ')
        players_guardians.extend(player_guardians)
        combine_guardians = "   ".join(player_guardians)
        player_experience = player["experience"]
        if player_experience == "YES":
            player_experience = True
        else:
            player_experience = False
        players_experiences.append(player_experience)
    player_height = player["height"]
    player_height = int(player['height'].split(' ')[0])
    players_height.append(player_height)
    average_height = round(sum(players_height) / len(players_height))
    return combine_names, combine_guardians, players_experiences, players_height, average_height


def display_stats(team_stats):
    picked_team_players, player_names = balance_teams()
    total_players = len(picked_team_players)

    players_names, players_guardians, players_experiences, players_height, average_height = clean_data()


    enter = input("""
    Team: {} Stats
    --------------
    Total Players: {}
    Players:
      {}


    Press ENTER to continue... """.format(team_stats, total_players, ', '.join(player_names)))
    if enter =="":
        exit()
    else:
        exit()


if __name__ == "__main__":
    menu()

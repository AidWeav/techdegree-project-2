import constants
import random
import copy

replay = []
replayed = 1
my_teams = copy.deepcopy(constants.TEAMS)
my_players = copy.deepcopy(constants.PLAYERS)
store_cleaned_players = []



def menu(): 
    looped_game = True
    while looped_game:
        try:
            menu_choice = int(input("""
            BASKETBALL TEAM STATS TOOL
            -----------MENU-----------
            Here are your choices:
            1: Display Team Stats
            2: Quit
            Enter an option:  """))
            if menu_choice == 1:
                choose_team()
                looped_game = False
            if menu_choice == 2:
                exit()
            if menu_choice > 2:
                raise ValueError
            if menu_choice < 1:
                raise ValueError
        except ValueError:
            print("Please choose a valid option")
               
def choose_team():
    looped_game = True
    while looped_game:
        try:
            team_stats = int(input(""" 
            1) Panthers
            2) Bandits
            3) Warriors
            Enter an option: """))
            if team_stats == 1:
                team_stats_answer = "Panthers"
                display_stats(team_stats_answer)
                looped_game = False
            if team_stats == 2:
                team_stats_answer = "Bandits"
                display_stats(team_stats_answer)
                looped_game = False
            if team_stats == 3:
                team_stats_answer = "Warriors"
                display_stats(team_stats_answer)
                looped_game = False
            if team_stats > 3:
                raise ValueError
            if team_stats < 1:
                raise ValueError
        except ValueError:
            print("Please enter a valid choice")

def clean_data():
    if len(replay) == 0:
        cleaned_players = []
        players_experiences = []
        players_height = []
        for player in my_players:
            add_player_data = {}
            add_player_data["name"] = player["name"]
            player_experience = player["experience"]
            players_experiences.append(player_experience) 
            player_height = int(player['height'].split(' ')[0])
            players_height.append(player_height)
            cleaned_players.append(add_player_data)
        if player_experience == "YES":
            player_experience = True
        else:
            player_experience = False
    else:
        cleaned_players = store_cleaned_players[0].copy()
    return cleaned_players
			
			
def balance_teams():
    cleaned_players = clean_data()
    every_team_total = int(len(cleaned_players) / len(my_teams))
    if len(replay) == 0:
        shuffled_players = random.shuffle(cleaned_players)
        store_cleaned_players.append(cleaned_players.copy())
    player_names = []
    for player in cleaned_players:
        add_player_data = {}
        add_player_data = player["name"]
        player_names.append(add_player_data)
    panthers = []
    panthers.append(player_names[0:every_team_total])
    bandits = []
    bandits.append(player_names[every_team_total:every_team_total * 2])
    warriors = []
    warriors.append(player_names[every_team_total * 2:every_team_total * 3])
    return panthers, bandits, warriors, every_team_total    
       
    
def display_stats(team_name):
    panthers, bandits, warriors, total_players = balance_teams()
    if team_name == "Panthers":
        player_names = ','.join(panthers[0][0:total_players])
    if team_name == "Bandits":
        player_names = ','.join(bandits[0][0:total_players])
    if team_name == "Warriors":
        player_names = ','.join(warriors[0][0:total_players])
    
    enter = input("""
    Team: {} Stats
    --------------
    Total Players: {}
    Players:
      {}


    Press ENTER to continue... """.format(team_name, total_players, player_names))
    if enter == "":
        replay.append(replayed)
        menu()
    else:
        exit()

        
if __name__ == "__main__":
    menu()

import json
from pathlib import Path


# base path of the project Directory
base_path = Path(__file__).parent

# method to extract all players from json payload
def extractPlayers():
    with open(base_path/'../data/rcb_data.json', 'r') as file:
        data = json.load(file)
        return json.dumps(data['player'])


# method that returns total number of foreign players
def validateTeamHasOnlyFourForeignPlayers():
    players = extractPlayers()
    players_dict = json.loads(players)
    foreignPlayers = [x for x in players_dict if x['country'] != 'India']
    return (len(foreignPlayers))


# method that returns the number of wicket-keeper in the team
def validateOnlyOneWicketKeeper():
    players = extractPlayers()
    players_dict = json.loads(players)
    wicketKeeper = [x for x in players_dict if x['role'] == 'Wicket-keeper']
    return (len(wicketKeeper))
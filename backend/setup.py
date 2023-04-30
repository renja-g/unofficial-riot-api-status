import json
import cassiopeia as cass
import os

"""
Autpomatically configures the endpoints.json with the correct API KEY
"""

try:
    API_KEY = os.environ['RIOT_API_KEY']
except KeyError:
    print("Please set the environment variable API_KEY")
    exit(1)

summoner_name = "Aatrox"

def get_puuid(region):
    if region == "americas":
        region = 'na1'
    elif region == "asia":
        region = 'kr'
    elif region == "europe":
        region = 'eun1'
    elif region == "sea":
        region = 'oc1'
    summoner = cass.get_summoner(name=summoner_name, region=region)
    return summoner.puuid

def get_matchId():
    return "XXX"

def get_accountId():
    return "XXX"

def get_summonerName():
    return "XXX"

def get_summonerId():
    return "XXX"

with open('endpoints.json', 'r') as f:
    endpoints = json.load(f)
data = endpoints['data']

for game in data: # lol, tft, lor, val
    for region in data[game]: # "americas", "asia", "europe", "sea", "br1", "eun1", "euw1", "jp1", "kr", "la1","la2", "na1", "oc1", "ph2", "ru", "sg2", "th2", "tr1", "tw2", "vn2"
        for key in data[game][region]:
            # key = puuid | matchId | accountId | summonerName | summonerId

            if key == "puuid":
                value = get_puuid(region)
            elif key == "matchId":
                value = get_matchId()
            elif key == "accountId":
                value = get_accountId()
            elif key == "summonerName":
                value = get_summonerName()
            elif key == "summonerId":
                value = get_summonerId()

            data[game][region][key] = value

with open('endpoints.json', 'w') as f:
    json.dump(endpoints, f, indent=4)

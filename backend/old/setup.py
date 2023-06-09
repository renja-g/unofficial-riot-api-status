import json
from riotwatcher import LolWatcher, ApiError
import os
import requests
from dotenv import load_dotenv

"""
Autpomatically configures the endpoints.json with the correct API KEY
"""

load_dotenv()

API_KEY = os.environ.get('RIOT_API_KEY')
if API_KEY is None:
    print('Please set the environment variable RIOT_API_KEY in the .env file')
    exit(1)
whatcher = LolWatcher(API_KEY)

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

    summoner = whatcher.summoner.by_name(region, summoner_name)
    return summoner['puuid']


def get_matchId(region):
    if region == "americas":
        region = 'na1'
    elif region == "asia":
        region = 'kr'
    elif region == "europe":
        region = 'eun1'
    elif region == "sea":
        region = 'oc1'

    summoner = whatcher.summoner.by_name(region, summoner_name)
    match = whatcher.match.matchlist_by_puuid(region, summoner['puuid'])
    return match[0]


def get_accountId(region):
    if region == "americas":
        region = 'na1'
    elif region == "asia":
        region = 'kr'
    elif region == "europe":
        region = 'eun1'
    elif region == "sea":
        region = 'oc1'

    summoner = whatcher.summoner.by_name(region, summoner_name)
    return summoner['accountId']


def get_summonerName(region):
    if region == "americas":
        region = 'na1'
    elif region == "asia":
        region = 'kr'
    elif region == "europe":
        region = 'eun1'
    elif region == "sea":
        region = 'oc1'

    summoner = whatcher.summoner.by_name(region, summoner_name)
    return summoner['name']

def get_summonerId(region):
    if region == "americas":
        region = 'na1'
    elif region == "asia":
        region = 'kr'
    elif region == "europe":
        region = 'eun1'
    elif region == "sea":
        region = 'oc1'

    summoner = whatcher.summoner.by_name(region, summoner_name)
    return summoner['id']

def get_championId():
    url = "http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion.json"
    response = requests.get(url)
    data = response.json()
    return data['data']['Aatrox']['key']

def get_leagueId(region):
    if region == "americas":
        region = 'na1'
    elif region == "asia":
        region = 'kr'
    elif region == "europe":
        region = 'eun1'
    elif region == "sea":
        region = 'oc1'

    league = requests.get(f"https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={API_KEY}")
    data = league.json()
    return data['leagueId']

with open('endpoints_template.json', 'r') as f:
    endpoints = json.load(f)
data = endpoints['data']

for game in data: # lol, tft, lor, val
    for region in data[game]: # "americas", "asia", "europe", "sea", "br1", "eun1", "euw1", "jp1", "kr", "la1","la2", "na1", "oc1", "ph2", "ru", "sg2", "th2", "tr1", "tw2", "vn2"
        for key in data[game][region]:
            # key = puuid | matchId | accountId | summonerName | summonerId

            print(f"Getting {key} for {game} in {region}")
            if key == "puuid":
                value = get_puuid(region)
            elif key == "matchId":
                value = get_matchId(region)
            elif key == "accountId":
                value = get_accountId(region)
            elif key == "summonerName":
                value = get_summonerName(region)
            elif key == "summonerId":
                value = get_summonerId(region)
            elif key == "championId":
                value = get_championId()
            elif key == "queue":
                value = "RANKED_SOLO_5x5"
            elif key == "tier":
                value = "PLATINUM"
            elif key == "division":
                value = "IV"
            elif key == "leagueId":
                value = get_leagueId(region)
            elif key == "challengeId":
                value = "0"
            elif key == "level":
                value = "MASTER"

            data[game][region][key] = value

with open('endpoints.json', 'w') as f:
    json.dump(endpoints, f, indent=4)

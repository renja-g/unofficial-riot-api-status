import ujson
import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ.get('RIOT_API_KEY')
if API_KEY is None:
    print('Please set the environment variable RIOT_API_KEY in the .env file')
    exit(1)

schema = ujson.load(open('schema/openapi-3.0.0.json'))


def replace_platform(platform):
    match platform:
        case 'americas':
            return 'na1'
        case 'asia':
            return 'kr'
        case 'europe':
            return 'eun1'
        case 'sea':
            return 'oc1'
        case 'apac':
            return 'kr'
        case 'ap':
            return 'XXXX'
        case 'br':
            return 'XXXX'
        case 'eu':
            return 'XXXX'
        case 'kr':
            return 'XXXX'
        case 'latam':
            return 'XXXX'
        case 'na':
            return 'XXXX'

        case _:
            return platform


def get_championId():
    return 266


def get_encryptedSummonerId(platform):
    platform_v2 = replace_platform(platform)
    url = f"https://{platform_v2}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/II?page=1&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    return data[0]['summonerId']


def get_puuid(platform):
    platform_v2 = replace_platform(platform)
    url = f"https://{platform_v2}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/II?page=1&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    summonerId = data[0]['summonerId']

    url = f"https://{platform_v2}.api.riotgames.com/lol/summoner/v4/summoners/{summonerId}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    return data['puuid']


def get_tagLine(platform):
    puuid = get_puuid(platform)

    url = f"https://{platform}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    return data['tagLine']


def get_gameName(platform):
    puuid = get_puuid(platform)

    url = f"https://{platform}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    return data['gameName']


def get_game():
    return 'val'


def get_queueType():
    return 'RANKED_SOLO_5x5'


def get_tier():
    return 'PLATINUM'


def get_division():
    return 'II'


def get_challengeId():
    return 1


def get_level():
    return 'MASTER'


def get_leagueId(platform):
    platform_v2 = replace_platform(platform)
    url = f"https://{platform_v2}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/II?page=1&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data[0]['leagueId']


def get_matchId(platform):
    platform_v2 = replace_platform(platform)
    url = f"https://{platform_v2}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/II?page=1&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    summonerId = data[0]['summonerId']

    url_2 = f"https://{platform_v2}.api.riotgames.com/lol/summoner/v4/summoners/{summonerId}?api_key={API_KEY}"
    response_2 = requests.get(url_2)
    data_2 = response_2.json()
    puuid = data_2['puuid']

    url_3 = f"https://{platform}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1&api_key={API_KEY}"
    response_3 = requests.get(url_3)
    data_3 = response_3.json()

    return data_3[0]


def get_encryptedAccountId(platform):
    platform_v2 = replace_platform(platform)
    url = f"https://{platform_v2}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/II?page=1&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    summonerId = data[0]['summonerId']

    url_2 = f"https://{platform_v2}.api.riotgames.com/lol/summoner/v4/summoners/{summonerId}?api_key={API_KEY}"
    response_2 = requests.get(url_2)
    data_2 = response_2.json()

    return data_2['accountId']


def get_summonerName(platform):
    platform_v2 = replace_platform(platform)
    url = f"https://{platform_v2}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/II?page=1&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    return data[0]['summonerName']


def get_parameter_value(platform, parameter):
    if platform == 'esports':
        return 'ESPORTS PLATFORM NOT SUPPORTED YET'
    if platform == 'pbe1':
        return 'PBE1 PLATFORM NOT SUPPORTED YET'
    if platform == 'ap':
        return 'AP PLATFORM NOT SUPPORTED YET'
    if platform == 'br':
        return 'BR PLATFORM NOT SUPPORTED YET'
    if platform == 'eu':
        return 'EU PLATFORM NOT SUPPORTED YET'
    if platform == 'kr':
        return 'KR PLATFORM NOT SUPPORTED YET'
    if platform == 'latam':
        return 'LATAM PLATFORM NOT SUPPORTED YET'
    if platform == 'na':
        return 'NA PLATFORM NOT SUPPORTED YET'
    if platform == 'apac':
        return 'APAC PLATFORM NOT SUPPORTED YET'

    if parameter == 'Authorization':
        return 'AUTHORIZATION PARAMETER NOT SUPPORTED YET'
    if parameter == 'teamId':
        return 'TEAMID PARAMETER NOT SUPPORTED YET'
    if parameter == 'tournamentId':
        return 'TOURNAMENTID PARAMETER NOT SUPPORTED YET'
    if parameter == 'rsoPUUID':
        return 'RSOPUUID PARAMETER NOT SUPPORTED YET'
    if parameter == 'tournamentCode':
        return 'TOURNAMENTCODE PARAMETER NOT SUPPORTED YET'
    

    match parameter:
        case 'championId':
            return get_championId()
        case 'encryptedSummonerId' | 'summonerId':
            return get_encryptedSummonerId(platform)
        case 'puuid' | 'encryptedPUUID':
            return get_puuid(platform)
        case 'tagLine':
            return get_tagLine(platform)
        case 'gameName':
            return get_gameName(platform)
        case 'game':
            return get_game()
        case 'queueType' | 'queue':
            return get_queueType()
        case 'tier':
            return get_tier()
        case 'division':
            return get_division()
        case 'challengeId':
            return get_challengeId()
        case 'level':
            return get_level()
        case 'leagueId':
            return get_leagueId(platform)
        case 'matchId':
            return get_matchId(platform)
        case 'encryptedAccountId':
            return get_encryptedAccountId(platform)
        case 'summonerName':
            return get_summonerName(platform)
        case _:
            return 'TODO'


# appand an examples field to each path
def set_examples():
    for path, path_obj in schema['paths'].items():
        methods = [method for method in path_obj if method.startswith(
            'x-') or method.upper() in ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')]
        for method in methods:
            if 'parameters' in schema['paths'][path][method]:
                for param in schema['paths'][path][method]['parameters']:
                    if param['required'] == False:
                        continue
                    examples = {}
                    if 'x-route-enum' in schema['paths'][path]:
                        platforms_available = schema['paths'][path]['x-platforms-available']
                        for platform in platforms_available:
                            examples[platform] = get_parameter_value(
                                platform, param['name'])
                        param['examples'] = examples
                    elif param['name'] == 'platform':
                        platforms_available = schema['servers'][0]['variables']['platform']['enum']
                        for platform in platforms_available:
                            examples[platform] = get_parameter_value(
                                platform, param['name'])
                        param['examples'] = examples


set_examples()


# write the schema to a file
with open('schema/out.json', 'w') as f:
    ujson.dump(schema, f, indent=2, escape_forward_slashes=False)

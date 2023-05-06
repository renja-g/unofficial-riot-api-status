import json

GAME = 'lol' # 'lol', 'tft', 'lor', 'val'
NAME = 'MATCH-V5'

# ['americas', 'asia', 'europe', 'sea']
# ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2']
REGIONS = ['americas', 'asia', 'europe', 'sea']


CHILDREN = [
    {
        "child_url": "/lol/match/v5/matches/by-puuid/{puuid}/ids",
    },
    {
        "child_url": "/lol/match/v5/matches/{matchId}",
    },
    {
        "child_url": "/lol/match/v5/matches/{matchId}/timeline",
    }
]

with open('endpoints_template.json', 'r') as f:
    endpoints_template = json.load(f)
'''
    "endpoints": {
        "lol": [
            {
                "game": "lol",
                "name": "MATCH-V5",
                "regions": ["americas", "asia", "europe", "sea"],
                "children": [
                    {
                        "child_url": "/lol/match/v5/matches/by-puuid/{puuid}/ids"
                    },
                    {
                        "child_url": "/lol/match/v5/matches/{matchId}"
                    },
                    {
                        "child_url": "/lol/match/v5/matches/{matchId}/timeline"
                    }
                ]
            },
'''

endpoints_template['endpoints'][GAME].append({
    "game": GAME,
    "name": NAME,
    "regions": REGIONS,
    "children": CHILDREN
})

with open('new_endpoints_template.json', 'w') as f:
    json.dump(endpoints_template, f, indent=4)
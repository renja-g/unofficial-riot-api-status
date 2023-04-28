interface Endpoint {
	name: string;
	regions: string[];
	children: Children[];
}

interface Children {
	child_url: string;
}

interface Config {
	baseUrl: string;
	endpoints: Endpoint[];
}

const config: Config = {
	baseUrl: 'https://{region}.api.riotgames.com',
	endpoints: [
		{
			name: 'ACCOUNT-V1',
			regions: ['americas', 'asia', 'esports', 'europe'],
			children: [
				{
					child_url: '/riot/account/v1/accounts/by-puuid/{puuid}'
				},
				{
					child_url: '/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}'
				},
				{
					child_url: '/riot/account/v1/accounts/me'
				},
				{
					child_url: '/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}'
				}
			]
		},
		{
			name: 'CHAMPION-MASTERY-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}'
				},
				{
					child_url: '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}'
				},
				{
					child_url: '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/top'
				},
				{
					child_url: '/lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}'
				}
			]
		},
		{
			name: 'CHAMPION-V3',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/platform/v3/champion-rotations'
				}
			]
		},
		{
			name: 'CLASH-V1',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/clash/v1/players/by-puuid/{encryptedPUUID}'
				},
				{
					child_url: '/lol/clash/v1/players/by-summoner/{summonerId}'
				},
				{
					child_url: '/lol/clash/v1/teams/{teamId}'
				},
				{
					child_url: '/lol/clash/v1/tournaments'
				},
				{
					child_url: '/lol/clash/v1/tournaments/by-team/{teamId}'
				},
				{
					child_url: '/lol/clash/v1/tournaments/{tournamentId}'
				}
			]
		},
		{
			name: 'LEAGUE-EXP-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/league-exp/v4/entries/{queue}/{tier}/{division}}'
				}
			]
		},
		{
			name: 'LEAGUE-V4 ',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/league/v4/challengerleagues/by-queue/{queue}'
				},
				{
					child_url: '/lol/league/v4/entries/by-summoner/{encryptedSummonerId}'
				},
				{
					child_url: '/lol/league/v4/entries/{queue}/{tier}/{division}'
				},
				{
					child_url: '/lol/league/v4/grandmasterleagues/by-queue/{queue}'
				},
				{
					child_url: '/lol/league/v4/leagues/{leagueId}'
				},
				{
					child_url: '/lol/league/v4/masterleagues/by-queue/{queue}'
				}
			]
		},
		{
			name: 'LOL-CHALLENGES-V1',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/challenges/v1/challenges/config'
				},
				{
					child_url: '/lol/challenges/v1/challenges/percentiles'
				},
				{
					child_url: '/lol/challenges/v1/challenges/{challengeId}/config'
				},
				{
					child_url: '/lol/challenges/v1/challenges/{challengeId}/leaderboards/by-level/{level}'
				},
				{
					child_url: '/lol/challenges/v1/challenges/{challengeId}/percentiles'
				},
				{
					child_url: '/lol/challenges/v1/player-data/{puuid}'
				}
			]
		},
		{
			name: 'LOL-STATUS-V3',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/status/v3/shard-data'
				}
			]
		},
		{
			name: 'LOL-STATUS-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/status/v4/platform-data'
				}
			]
		},
		{
			name: 'LOR-DECK-V1',
			regions: ['americas', 'europe', 'sea'],
			children: [
				{
					child_url: '/lor/deck/v1/decks/me'
				}
			]
		},
		{
			name: 'LOR-INVENTORY-V1',
			regions: ['americas', 'europe', 'sea'],
			children: [
				{
					child_url: '/lor/inventory/v1/cards/me'
				}
			]
		},
		{
			name: 'LOR-MATCH-V1',
			regions: ['americas', 'apac', 'europe', 'sea'],
			children: [
				{
					child_url: '/lor/match/v1/matches/by-puuid/{puuid}/ids'
				},
				{
					child_url: '/lor/match/v1/matches/{matchId}'
				}
			]
		},
		{
			name: 'LOR-RANKED-V1',
			regions: ['americas', 'europe', 'sea'],
			children: [
				{
					child_url: '/lor/ranked/v1/leaderboards'
				}
			]
		},
		{
			name: 'LOR-STATUS-V1',
			regions: ['americas', 'europe', 'sea'],
			children: [
				{
					child_url: '/lor/status/v1/platform-data'
				}
			]
		},
		{
			name: 'MATCH-V5',
			regions: ['americas', 'asia', 'europe', 'sea'],
			children: [
				{
					child_url: '/lol/match/v5/matches/by-puuid/{puuid}/ids'
				},
				{
					child_url: '/lol/match/v5/matches/{matchId}'
				},
				{
					child_url: '/lol/match/v5/matches/{matchId}/timeline'
				}
			]
		},
		{
			name: 'SPECTATOR-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}'
				},
				{
					child_url: '/lol/spectator/v4/featured-games'
				}
			]
		},
		{
			name: 'SUMMONER-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/fulfillment/v1/summoners/by-puuid/{rsoPUUID}'
				},
				{
					child_url: '/lol/summoner/v4/summoners/by-account/{encryptedAccountId}'
				},
				{
					child_url: '/lol/summoner/v4/summoners/by-name/{summonerName}'
				},
				{
					child_url: '/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}'
				},
				{
					child_url: '/lol/summoner/v4/summoners/me'
				},
				{
					child_url: '/lol/summoner/v4/summoners/{encryptedSummonerId}'
				}
			]
		},
		{
			name: 'TFT-LEAGUE-V1',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/tft/league/v1/challenger'
				},
				{
					child_url: '/tft/league/v1/entries/by-summoner/{summonerId}'
				},
				{
					child_url: '/tft/league/v1/entries/{tier}/{division}'
				},
				{
					child_url: '/tft/league/v1/grandmaster'
				},
				{
					child_url: '/tft/league/v1/leagues/{leagueId}'
				},
				{
					child_url: '/tft/league/v1/master'
				},
				{
					child_url: '/tft/league/v1/rated-ladders/{queue}/top'
				}
			]
		},
		{
			name: 'TFT-MATCH-V1',
			regions: ['americas', 'asia', 'europe', 'sea'],
			children: [
				{
					child_url: '/tft/match/v1/matches/by-puuid/{puuid}/ids'
				},
				{
					child_url: '/tft/match/v1/matches/{matchId}'
				}
			]
		},
		{
			name: 'TFT-STATUS-V1',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/tft/status/v1/platform-data'
				}
			]
		},
		{
			name: 'TFT-SUMMONER-V1',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					child_url: '/tft/summoner/v1/summoners/by-account/{encryptedAccountId}'
				},
				{
					child_url: '/tft/summoner/v1/summoners/by-name/{summonerName}'
				},
				{
					child_url: '/tft/summoner/v1/summoners/by-puuid/{encryptedPUUID}'
				},
				{
					child_url: '/tft/summoner/v1/summoners/me'
				},
				{
					child_url: '/tft/summoner/v1/summoners/{encryptedSummonerId}'
				}
			]
		},
		// TODO: TOURNAMENT-STUB-V4
		// TODO: TOURNAMENT-V4
		{
			name: 'VAL-CONTENT-V1',
			regions: ['ap', 'br', 'esports', 'eu', 'kr', 'latam', 'na'],
			children: [
				{
					child_url: '/val/content/v1/contents'
				}
			]
		},
		{
			name: 'VAL-MATCH-V1',
			regions: ['ap', 'br', 'esports', 'eu', 'kr', 'latam', 'na'],
			children: [
				{
					child_url: '/val/match/v1/matches/{matchId}'
				},
				{
					child_url: '/val/match/v1/matchlists/by-puuid/{puuid}'
				},
				{
					child_url: '/val/match/v1/recent-matches/by-queue/{queue}'
				}
			]
		},
		{
			name: 'VAL-RANKED-V1',
			regions: ['ap', 'br', 'esports', 'eu', 'kr', 'latam', 'na'],
			children: [
				{
					child_url: '/val/ranked/v1/leaderboards/by-act/{actId}'
				}
			]
		},
		{
			name: 'VAL-STATUS-V1',
			regions: ['ap', 'br', 'esports', 'eu', 'kr', 'latam', 'na'],
			children: [
				{
					child_url: '/val/status/v1/platform-data'
				}
			]
		}
	]
};

export default config;

// full_url = https://{region}.api.riotgames.com{child_url}

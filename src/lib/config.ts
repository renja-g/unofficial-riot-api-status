interface Endpoint {
	name: string;
	regions: string[];
	children: Children[];
}

interface Children {
	children_url: string;
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
					children_url: '/riot/account/v1/accounts/by-puuid/{puuid}'
				},
				{
					children_url: '/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}'
				},
				{
					children_url: '/riot/account/v1/accounts/me'
				},
				{
					children_url: '/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}'
				}
			]
		},
		{
			name: 'CHAMPION-MASTERY-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}'
				},
				{
					children_url: '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}'
				},
				{
					children_url: '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/top'
				},
				{
					children_url: '/lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}'
				}
			]
		},
		{
			name: 'CHAMPION-V3',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/platform/v3/champion-rotations'
				}
			]
		},
		{
			name: 'CLASH-V1',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/clash/v1/players/by-puuid/{encryptedPUUID}'
				},
				{
					children_url: '/lol/clash/v1/players/by-summoner/{summonerId}'
				},
				{
					children_url: '/lol/clash/v1/teams/{teamId}'
				},
				{
					children_url: '/lol/clash/v1/tournaments'
				},
				{
					children_url: '/lol/clash/v1/tournaments/by-team/{teamId}'
				},
				{
					children_url: '/lol/clash/v1/tournaments/{tournamentId}'
				}
			]
		},
		{
			name: 'LEAGUE-EXP-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/league-exp/v4/entries/{queue}/{tier}/{division}}'
				}
			]
		},
		{
			name: 'LEAGUE-V4 ',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/league/v4/challengerleagues/by-queue/{queue}'
				},
				{
					children_url: '/lol/league/v4/entries/by-summoner/{encryptedSummonerId}'
				},
				{
					children_url: '/lol/league/v4/entries/{queue}/{tier}/{division}'
				},
				{
					children_url: '/lol/league/v4/grandmasterleagues/by-queue/{queue}'
				},
				{
					children_url: '/lol/league/v4/leagues/{leagueId}'
				},
				{
					children_url: '/lol/league/v4/masterleagues/by-queue/{queue}'
				}
			]
		},
		{
			name: 'LOL-CHALLENGES-V1',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/challenges/v1/challenges/config'
				},
				{
					children_url: '/lol/challenges/v1/challenges/percentiles'
				},
				{
					children_url: '/lol/challenges/v1/challenges/{challengeId}/config'
				},
				{
					children_url: '/lol/challenges/v1/challenges/{challengeId}/leaderboards/by-level/{level}'
				},
				{
					children_url: '/lol/challenges/v1/challenges/{challengeId}/percentiles'
				},
				{
					children_url: '/lol/challenges/v1/player-data/{puuid}'
				}
			]
		},
		{
			name: 'LOL-STATUS-V3',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/status/v3/shard-data'
				}
			]
		},
		{
			name: 'LOL-STATUS-V4',
			regions: ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ph2', 'ru', 'sg2', 'th2', 'tr1', 'tw2', 'vn2'],
			children: [
				{
					children_url: '/lol/status/v4/platform-data'
				}
			]
		},
		{
			name: 'LOR-DECK-V1',
			regions: ['americas', 'europe', 'sea'],
			children: [
				{
					children_url: '/lor/deck/v1/decks/me'
				}
			]
		},
		{
			name: 'LOR-INVENTORY-V1',
			regions: ['americas', 'europe', 'sea'],
			children: [
				{
					children_url: '/lor/inventory/v1/cards/me'
				}
			]
		},
		{
			name: 'LOR-MATCH-V1',
			regions: ['americas', 'apac', 'europe', 'sea'],
			children: [
				{
					children_url: '/lor/match/v1/matches/by-puuid/{puuid}/ids'
				},
				{
					children_url: '/lor/match/v1/matches/{matchId}'
				}
			]
		},
		{
			name: 'LOR-RANKED-V1',
			regions: ['americas', 'europe', 'sea'],
			children: [
				{
					children_url: '/lor/ranked/v1/leaderboards'
				}
			]
		}
	]
};

export default config;

// full_url = https://{region}.api.riotgames.com{children_url}

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
				//      {
				//        'url': '/riot/account/v1/accounts/me',
				//      },
				{
					children_url: '/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}'
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
		}
	]
};

export default config;

// full_url = https://{region}.api.riotgames.com{children_url}
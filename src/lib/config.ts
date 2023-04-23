interface Region {
  name: string;
  url: string;
}

interface Endpoint {
  name: string;
  url: string;
  regions: Region[];
}

interface Config {
  endpoints: Endpoint[];
}


const config: Config = {
  "endpoints": [
    {
      "name": "SUMMONER-V4",
      "url": "https://developer.riotgames.com/apis#summoner-v4",
      "regions": [
        {
          "name": "EUW1",
          "url": "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/someone"
        },
        {
          "name": "NA1",
          "url": "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/someone"
        }
      ]
    },
    {
      "name": "LEAGUE-V4",
      "url": "https://developer.riotgames.com/apis#league-v4",
      "regions": [
        {
          "name": "EUW1",
          "url": "https://euw1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
        },
        {
          "name": "NA1",
          "url": "https://na1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
        },
      ],
    },
  ],
};

export default config;
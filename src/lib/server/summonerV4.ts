// src\lib\server\summonerV4.ts
import axios from 'axios';
import { env } from '$lib/env';

const apiKey = env.RIOT_API_KEY;
const regions = ['na1', 'euw1'];

// retuen an object with the status for all regions
export async function getSummonerByName(name: string) {
    const promises = regions.map(region => {
        return axios.get(`https://${region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/${name}?api_key=${apiKey}`)
            .then(res => {
                return {
                    region: region,
                    status: res.status
                };
            })
            .catch(err => {
                return {
                    region: region,
                    status: err.response.status
                };
            });
    });

    return await Promise.allSettled(promises);
}
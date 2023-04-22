import type { PageServerLoad } from './$types';
import { getSummonerByName } from '$lib/server/summonerV4';

// return the status code of the request
export const load = (async () => {
    const status = await getSummonerByName('test');
    return {
        status: status
    };
}) satisfies PageServerLoad;
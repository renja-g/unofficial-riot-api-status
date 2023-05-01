import json
import os
import asyncio
import aiohttp
import time

try:
    API_KEY = os.environ['RIOT_API_KEY']
except KeyError:
    print("Please set the environment variable API_KEY")
    exit(1)

with open('endpoints.json', 'r') as f:
    endpoints_data = json.load(f)

async def build_url(base_url: str, game: str, endpoint: str, region: str) -> str:
    # Get the parameters for the specified game and region.
    parameters = endpoints_data['data'][game][region]

    # Replace any aliases in the endpoint with their corresponding parameter names.
    for alias, parameter in endpoints_data.get('alias', {}).items():
        if alias in endpoint:
            endpoint = endpoint.replace(alias, parameter)

    # Replace any placeholders in the endpoint with their corresponding values from the parameters.
    for key in parameters:
        placeholder = '{' + key + '}'
        if placeholder in endpoint:
            endpoint = endpoint.replace(placeholder, parameters[key])

    # Combine the base URL, region, and endpoint to create the final URL.
    url = base_url.format(region=region) + endpoint

    return url



async def make_request(url: str, api_key: str, session: aiohttp.ClientSession) -> dict:
    # Add the API key to the URL.
    url += f'?api_key={api_key}'

    while True:
        async with session.get(url) as response:
            if response.status == 429:
                # If the response status is 429 (Too Many Requests), wait for the specified time before retrying.
                retry_after = int(response.headers.get('Retry-After', '1'))
                print(f'Rate limited. Waiting for {retry_after} seconds.')
                await asyncio.sleep(retry_after)
            elif response.status == 200:
                # If the response status is 200 (OK), return the JSON.
                return await response.json()
            else:
                # If the response status is anything else, raise an exception.
                raise Exception(f'Request failed with status {response.status}.')

async def get_all_urls():
    urls = []
    for game in endpoints_data['endpoints']:
        game_endpoints = endpoints_data['endpoints'][game]
        for endpoint in game_endpoints:
            regions = endpoint['regions']
            for region in regions:
                for child in endpoint['children']:
                    child_url = child['child_url']
                    url = await build_url(base_url=endpoints_data['baseUrl'], game=game, endpoint=child_url, region=region)
                    urls.append(url)
    return urls

async def main():
    urls = await get_all_urls()
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(url)
            try:
                data = await make_request(url, API_KEY, session)
                print("200 OK")
            except Exception as e:
                print(e)
            print('\n')


if __name__ == '__main__':
    asyncio.run(main())

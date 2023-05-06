import json
import os
import asyncio
import aiohttp
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.environ.get('RIOT_API_KEY')
USER_AGENT = 'my-app/0.0.1'
if API_KEY is None:
    print('Please set the environment variable RIOT_API_KEY in the .env file')
    exit(1)

with open('endpoints.json', 'r') as f:
    endpoints_data = json.load(f)


def build_url(base_url: str, game: str, endpoint: str, region: str) -> str:
    # Get the parameters for the specified game and region.
    parameters = endpoints_data['data'][game][region]

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
    headers = {'User-Agent': USER_AGENT}
    original_url = url  
    url += f'?api_key={api_key}'
    while True:
        async with session.get(url, ssl=False, headers=headers) as response:
            if response.status == 429:
                # If the response status is 429 (Too Many Requests), wait for the specified time before retrying.
                retry_after = int(response.headers.get('Retry-After', '1'))
                print(f'Rate limited. Waiting for {retry_after} seconds.')
                await asyncio.sleep(retry_after)

            else:
                data = await response.json()
                return {'data': data, 'status': response.status, 'url': original_url}


def get_all_urls() -> dict:
    urls_by_region = {}
    for game, game_endpoints in endpoints_data['endpoints'].items():
        for endpoint in game_endpoints:
            regions = endpoint['regions']
            for region in regions:
                if region not in urls_by_region:
                    urls_by_region[region] = []
                for child in endpoint['children']:
                    child_url = child['child_url']
                    url = build_url(base_url=endpoints_data['baseUrl'], game=game, endpoint=child_url, region=region)
                    urls_by_region[region].append(url)
    return urls_by_region


async def get_responses_for_region(urls: list, api_key: str, session: aiohttp.ClientSession) -> list:
    semaphore = asyncio.Semaphore(20)
    tasks = [make_request(url, api_key, session) for url in urls]
    async with semaphore:
        responses = await asyncio.gather(*tasks)
    return responses


async def get_responses(urls_by_region: dict, api_key: str, session: aiohttp.ClientSession) -> list:
    tasks = [get_responses_for_region(
        urls, api_key, session) for region, urls in urls_by_region.items()]
    responses = await asyncio.gather(*tasks)
    return responses


async def main():
    urls_by_region = get_all_urls()

    async with aiohttp.ClientSession() as session:
        time_start = time.time()
        responses = await get_responses(urls_by_region, API_KEY, session)
        time_end = time.time()

    # If all responses are successful, Print a success message.
    if all([all([response['status'] == 200 for response in region_responses]) for region_responses in responses]):
        print('\033[32mAll requests were successful.\033[0m')
        print(f'The requests took {round(time_end - time_start, 2)} seconds to complete.')

    # Otherwise, print the status code and URL for each failed request.
    else:
        for region_responses in responses:
            for response in region_responses:
                if response['status'] != 200:
                    print(f'\033[31m{response["status"]}\033[0m - {response["url"]}')

if __name__ == '__main__':
    asyncio.run(main())

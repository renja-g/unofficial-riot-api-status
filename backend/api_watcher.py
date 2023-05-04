import json
import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table



load_dotenv() # load variables from .env file

API_KEY = os.environ.get('RIOT_API_KEY')
if API_KEY is None:
    print("Please set the environment variable RIOT_API_KEY in the .env file")
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
            
            else:
                # Extract the response data.
                data = await response.json()

                # Return the response data and status code as a dictionary.
                return {'data': data, 'status': response.status}


async def get_grouped_urls():
    urls = {}
    for game in endpoints_data['endpoints']:
        game_endpoints = endpoints_data['endpoints'][game]
        for endpoint in game_endpoints:
            endpoint_name = endpoint['name']
            regions = endpoint['regions']
            for region in regions:
                for child in endpoint['children']:
                    child_url = child['child_url']
                    url = await build_url(base_url=endpoints_data['baseUrl'], game=game, endpoint=child_url, region=region)
                    if endpoint_name not in urls:
                        urls[endpoint_name] = {}
                    if region not in urls[endpoint_name]:
                        urls[endpoint_name][region] = []
                    urls[endpoint_name][region].append(url)
    return urls

async def get_responses(urls: list, api_key: str, session: aiohttp.ClientSession) -> list:
    tasks = []
    for url in urls:
        tasks.append(make_request(url, api_key, session))
    responses = await asyncio.gather(*tasks)
    return responses

async def main():
    console = Console()
    urls = await get_grouped_urls()

    async with aiohttp.ClientSession() as session:
        # Make requests to all URLs and print the status codes.
        for endpoint in urls:
            print(endpoint)
            for region in urls[endpoint]:
                urls_to_request = urls[endpoint][region]
                responses = await get_responses(urls_to_request, API_KEY, session)
                table = Table(title=f"{endpoint} ({region})")
                table.add_column("URL")
                table.add_column("Status", justify="right")
                for response, url in zip(responses, urls_to_request):
                    status = str(response['status'])
                    status_color = "green" if status == "200" else "red"
                    table.add_row(url, f"[{status_color}]{status}[/{status_color}]")
                console.print(table)
            print()


if __name__ == '__main__':
    asyncio.run(main())
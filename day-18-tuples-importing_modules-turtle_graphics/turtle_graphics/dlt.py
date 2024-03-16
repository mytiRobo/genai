import aiohttp
import asyncio
async def make_api_call(query, url, port):
   endpoint = f"{url}:{port}/llm_query"
   payload = {"query": query}
   async with aiohttp.ClientSession() as session:
       async with session.post(endpoint, json=payload) as response:
           if response.status == 200:
               data = await response.json()
               return data["response"]
           else:
               return f"Error: Server responded with status code {response.status}"
url = "http://100.70.10.200"
port = 8895
query = "Why is the sky blue?"
loop = asyncio.get_event_loop()
response = loop.run_until_complete(make_api_call(query, url, port))
print(response)
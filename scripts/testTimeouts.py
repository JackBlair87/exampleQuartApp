import asyncio
import aiohttp

async def make_request(session, minutes):
    try:
        url = "http://172.174.232.226/timeoutTest"  # Replace with your actual API endpoint
        payload = {"minutes": minutes}
        
        #add header to request for content type
        headers = {'Content-Type': 'application/json'}

        async with session.post(url, json=payload, timeout=minutes * 60 + 10, headers=headers) as response:
            if response.content_type == "application/json":
                result = await response.json()
                print(result)
            else:
                print(f"Unexpected content type: {response.content_type}")
    except asyncio.TimeoutError:
        print(f"Request with {minutes} minutes timeout timed out.")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for minutes in range(0, 21):
            if minutes % 0.5 == 0:  # Make requests in half-minute increments
                tasks.append(make_request(session, minutes))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

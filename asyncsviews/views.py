import asyncio
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print("Async Request, Response N°: " + str(num))
    
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

async def async_api(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())

    return HttpResponse("HTTPS request, non-blocking")
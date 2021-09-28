import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://[fd11:22:0:0:144a:9200:648e:daed]:5683/LED', observe=0)

    protocol_request = protocol.request(request)
    protocol_request.observation.register_callback(observation_callback)
    r = await protocol_request.response

    print("First response: %s\n%r"%(r, r.payload))

    while True:
      await asyncio.sleep(2)
        
def observation_callback(response):
    print("callback: %r" % response.payload)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

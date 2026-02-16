import httpx
from a2a.client import A2ACardResolver, ClientFactory, ClientConfig
import asyncio
from a2a.types import TransportProtocol, Message, Role, Part, TextPart
import uuid


BASE_URL="http://localhost:9999/"
PUBLIC_AGENT_CARD_PATH = "/.well-known/agent.json"

async def main():
    async with httpx.AsyncClient() as httpx_client:
        # Get Agent Card
        resolver = A2ACardResolver(httpx_client=httpx_client, base_url=BASE_URL)
        agent_card = await resolver.get_agent_card()
        print("Agent Card", agent_card.model_dump_json(indent=2))

        # A2A Client 
        supported = [TransportProtocol.jsonrpc]
        factory = ClientFactory(
            ClientConfig(httpx_client=httpx_client, supported_transports= supported)
        )
        a2a_client = factory.create(agent_card)
        print("A2A Client Initialized")

        # Send message
        message = Message(
            role=Role.user,
            message_id=str(uuid.uuid4()),
            parts=[Part(root=TextPart(text="Hi How are you?"))],
        )

        async for event in a2a_client.send_message(message):
            print("Response", event.model_dump_json(indent=2))




        
if __name__ == "__main__":
    asyncio.run(main())
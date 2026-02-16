# Create a dummy agent
import asyncio

class GreetingAgent():
    """Greeting agent that returns a greeting"""

    async def invoke(self) -> str:
        return "Hi Everyone! Welcome to A2A basics."
    

# Create Agent Executor
from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message


class GreetingAgentExecutor(AgentExecutor):

    def __init__(self):
        self.agent = GreetingAgent()

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        result = await self.agent.invoke()
        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise Exception("Cancel not supported")


"""async def main():
    agent = GreetingAgent()
    greeting = await agent.invoke()
    print(greeting)

if __name__ == "__main__":
    asyncio.run(main())"""
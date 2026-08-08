import asyncio

from agent import GitHubAgent


async def main():

    agent = GitHubAgent()

    answer = await agent.ask(
        "Analyze the GitHub profile of yukktha747"
    )

    print(answer)


asyncio.run(main())
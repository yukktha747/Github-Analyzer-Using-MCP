import asyncio

from mcp_client import MCPClient


async def main():

    client = MCPClient()

    print("Calling github_profile...\n")

    result = await client.call_tool(
        "github_profile",
        {
            "username": "yukktha747"
        }
    )

    print(result)


asyncio.run(main())
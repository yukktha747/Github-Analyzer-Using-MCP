import os
from dotenv import load_dotenv
import sys
from mcp import (
    ClientSession,
    StdioServerParameters,
    stdio_client,
)

load_dotenv()


class MCPClient:

    def __init__(self):

        self.server_params = StdioServerParameters(
            command=sys.executable,
            args=[
                r"C:\Users\i_yukktha.srisaila\Downloads\AI_Udemy\github_profile\mcp_server\server.py"
            ],
            env=os.environ.copy(),
        )

    async def list_tools(self):

        async with stdio_client(self.server_params) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                response = await session.list_tools()

                return response.tools

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict,
    ):

        async with stdio_client(self.server_params) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.call_tool(
                    tool_name,
                    arguments,
                )

                return result
import json

from llm import LLM
from prompts.github_prompts import SYSTEM_PROMPT
from mcp_client import MCPClient


class GitHubAgent:

    def __init__(self):

        self.llm = LLM()
        self.mcp = MCPClient()

    async def ask(self, question: str):

        # Discover MCP tools
        mcp_tools = await self.mcp.list_tools()

        openai_tools = []

        for tool in mcp_tools:

            openai_tools.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description or "",
                        "parameters": tool.inputSchema,
                    },
                }
            )

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            },
        ]

        # First LLM call
        response = self.llm.chat(
            messages,
            openai_tools,
        )

        assistant_message = response.choices[0].message

        # No tool needed
        if not assistant_message.tool_calls:
            return assistant_message.content

        messages.append(
            assistant_message.model_dump()
        )

        # Execute tool(s)
        for tool_call in assistant_message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            result = await self.mcp.call_tool(
                tool_name,
                arguments,
            )

            tool_result = ""

            if result.content:
                for item in result.content:
                    if hasattr(item, "text"):
                        tool_result += item.text

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result,
                }
            )

        # Second LLM call
        final_response = self.llm.chat(messages)

        return final_response.choices[0].message.content
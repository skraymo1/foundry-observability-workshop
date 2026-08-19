import asyncio
from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, ResultMessage, query


async def main():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Glob"],
        permission_mode="default",
    )

    async for message in query(
        prompt=(
            "Read the workshop policy file. Summarize the return policy, "
            "identify any missing fields, and do not modify any files."
        ),
        options=options,
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                elif hasattr(block, "name"):
                    print(f"Tool: {block.name}")
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}")


asyncio.run(main())
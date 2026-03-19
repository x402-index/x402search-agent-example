import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

load_dotenv()

async def main():
    print("Starting x402search agent...")
    print("This agent will pay $0.01 USDC to discover a crypto price API.\n")

    async with MCPServerStdio(
        params={
            "command": "npx",
            "args": ["-y", "x402search-mcp@1.0.3"],
            "env": {
                **os.environ,
                "EVM_PRIVATE_KEY": os.environ["EVM_PRIVATE_KEY"]
            }
        },
        cache_tools_list=True
    ) as mcp_server:

        agent = Agent(
            name="API Discovery Agent",
            instructions="""You are an autonomous agent with a Base mainnet wallet.
You can discover x402-enabled APIs using the search_x402_apis tool.
When asked to find data:
1. Use search_x402_apis to find APIs that provide the data
2. Report the top 3 results with their endpoint URLs, descriptions, and prices
3. Explain which one you would use and why
You pay $0.01 USDC per search automatically from your wallet.""",
            mcp_servers=[mcp_server]
        )

        result = await Runner.run(
            agent,
            input="Find me x402-enabled APIs that provide crypto token prices or market data. Search for 'crypto market data' and show me what is available."
        )

        print("\n=== Agent Response ===")
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

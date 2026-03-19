# x402search Agent Example

An autonomous agent that discovers and pays for APIs at runtime using OpenAI Agents SDK + x402search MCP.

No hardcoded endpoints. The agent finds what it needs, pays $0.01 USDC for the search, then returns the discovered APIs — all from its own Base wallet.

## What it does

1. Agent receives task: "find a crypto price API and get the ETH price"
2. Calls x402search ($0.01 USDC) → gets back list of matching APIs
3. Reports top results with endpoint URLs, descriptions, and prices

## Requirements

- Python 3.10+
- Node.js 18+ (for x402search-mcp via npx)
- OpenAI API key
- EVM wallet private key with USDC on Base mainnet

## Setup
```bash
git clone https://github.com/x402-index/x402search-agent-example
cd x402search-agent-example
pip install -r requirements.txt
cp .env.example .env
# Fill in your keys in .env
python main.py
```

## Get USDC on Base

https://www.coinbase.com/how-to-buy/usdc

At $0.01 per search, $1 gets you 100 queries.

## Links

- x402search: https://x402search.xyz
- npm: https://www.npmjs.com/package/x402search-mcp
- x402 protocol: https://x402.org
- Full tutorial: https://dev.to/x402index

# python-loopring

![status](https://img.shields.io/badge/status-work%20in%20progress-yellow) ![license](https://img.shields.io/badge/license-MIT-green) ![python version](https://img.shields.io/badge/python->%203.6-blue)

This repository hosts the `python-loopring` library for Python.

This is an unofficial implementation of the Loopring DEX REST API to facilitate development of applications based on Loopring's Ethereum Layer 2 solution with Python.

I am not affiliated with Loopring, use at your own risk.

**Loopring REST API documentation**

https://docs.loopring.io/en/

This library is currently a work in progress.

## Features (to come)

- Implementation of all Loopring DEX REST API endpoints
- Implementation of all Loopring DEX WebSockets API endpoints
- Asynchronous client
- NFT Minting & Trading

### Loopring DEX API Features

- Account data
- Market data
- AMM (Automated Market Maker)
- Mint, buy and sell NFTs on Loopring L2

### Implemented REST API Endpoints (45/59)

| Status  | Endpoint | Description | Method |
| ------- | -------- | ----------- | ------ |
| `[x]` | `/api/v3/timestamp` | Get relayer's current time | GET |
| `[x]` | `/api/v3/apiKey` | Get user ApiKey | GET |
| `[x]` | `/api/v3/apiKey` | Update user's ApiKey | POST |
| `[x]` | `/api/v3/storageId` | Get next storage ID | GET |
| `[x]` | `/api/v3/order` | Get order details | GET |
| `[x]` | `/api/v3/order` | Submit an order | POST |
| `[x]` | `/api/v3/order` | Cancel an order | DELETE |
| `[x]` | `/api/v3/orders` | Get multiple orders | GET |
| `[x]` | `/api/v3/exchange/markets` | Get market configurations | GET |
| `[x]` | `/api/v3/exchange/tokens` | Get token configurations | GET |
| `[x]` | `/api/v3/exchange/info` | Get exchange configurations | GET |
| `[x]` | `/api/v3/depth` | Get market orderbook | GET |
| `[x]` | `/api/v3/ticker` | Get market ticker | GET |
| `[x]` | `/api/v3/candlestick` | Get market candlestick | GET |
| `[x]` | `/api/v3/price` | Get token fiat prices | GET |
| `[x]` | `/api/v3/trade` | Get market recent trades | GET |
| `[ ]` | `/api/v3/transfer` | Submit internal transfer | POST |
| `[x]` | `/api/v3/account` | Query user information | GET |
| `[ ]` | `/api/v3/account` | Update account EDDSA key | POST |
| `[x]` | `/api/v3/user/createInfo` | Get user registration transactions | GET |
| `[x]` | `/api/v3/user/updateInfo` | Get password reset transactions | GET |
| `[x]` | `/api/v3/user/balances` | Get user exchange balances | GET |
| `[t]` | `/api/v3/user/deposits` | Get user deposit history | GET |
| `[t]` | `/api/v3/user/withdrawals` | Get user onchain withdrawal history | GET |
| `[ ]` | `/api/v3/user/withdrawals` | Submit offchain withdrawal request | POST |
| `[x]` | `/api/v3/user/transfers` | Get user transfer list | GET |
| `[x]` | `/api/v3/user/trades` | Get user trade history | GET |
| `[x]` | `/api/v3/user/orderFee` | Query user place order fee rate | GET |
| `[x]` | `/api/v3/user/orderUserRateAmount` | Query current token minimum amount to place order based on user's VIP level and max fee bips | GET |
| `[x]` | `/api/v3/user/offchainFee` | Query current fee amount | GET |
| `[x]` | `/api/v3/amm/pools` | Get AMM pool configurations | GET |
| `[x]` | `/api/v3/amm/balance` | Get AMM pool balance snapshot | GET |
| `[ ]` | `/api/v3/amm/join` | Join AMM pool | POST |
| `[ ]` | `/api/v3/amm/exit` | Exit AMM pool | POST |
| `[x]` | `/api/v3/amm/transactions` | Return the user's AMM join/exit transactions | GET |
| `[x]` | `/api/v3/amm/trades` | Get AMM pool trade transactions | GET |
| `[ ]` | `/api/v3/mix/depth` | api.getMixedDepth.value | GET |
| `[ ]` | `/api/v3/mix/ticker` | api.getMixedTicker.value | GET |
| `[ ]` | `/api/v3/mix/candlestick` | api.getMixedCandlestick.value | GET |
| `[ ]` | `/api/v3/mix/markets` | api.getMixedMarkets.value | GET |
| `[ ]` | `/api/v3/nft/mint` | Mint a NFT token on Loopring L2 | POST |
| `[ ]` | `/api/v3/nft/transfer` | Submit internal NFT transfer | POST |
| `[ ]` | `/api/v3/nft/validateOrder` | Validate a NFT order | POST |
| `[ ]` | `/api/v3/nft/trade` | Settle down an NFT trade which has two matched orders | POST |
| `[ ]` | `/api/v3/nft/withdrawal` | Withdraw a NFT token | POST |
| `[x]` | `/api/v3/nft/info/nfts` | Query NFT info by looprings nftData | GET |
| `[x]` | `/api/v3/nft/info/nftData` | Query nftData by minter, tokenAddress and nftID | GET |
| `[x]` | `/api/v3/nft/info/nftHolders` | Query NFT holders by looprings nftData | GET |
| `[x]` | `/api/v3/nft/info/orderUserRateAmount` | Query current token minimum amount to place order based on user's VIP level and max fee bips | GET |
| `[x]` | `/api/v3/user/nft/balances` | Get user's NFT balance | GET |
| `[t]` | `/api/v3/user/nft/trades` | Get user's NFT trade list | GET |
| `[x]` | `/api/v3/user/nft/transfers` | Get user's NFT transfer history | GET |
| `[t]` | `/api/v3/user/nft/mints` | Get user's NFT mint history | GET |
| `[t]` | `/api/v3/user/nft/deposits` | Get user's NFT deposit history | GET |
| `[t]` | `/api/v3/usesr/nft/withdrawals` | Get user's NFT withdrawal history | GET |
| `[x]` | `/api/v3/user/nft/offchainFee` | Query current NFT requests fee amount | GET |
| `[x]` | `/api/v3/user/nft/orderFee` | Query user's place order fee rate | GET |
| `[x]` | `/api/v3/block/getBlock` | Get L2 block info | GET |
| `[x]` | `/api/v3/block/getPendingRequests` | Get pending transactions | GET |

### Implemented WebSocket API Endpoints (0/8)

| Status  | Topic name | ApiKey required | Description |
| ------- | ---------- | --------------- | ----------- |
| `[ ]` | `account` | Yes | Account Notification |
| `[ ]` | `order` | Yes | Order Notification |
| `[ ]` | `orderbook` | No | Orderbook Notification |
| `[ ]` | `trade` | No | Trade Notification |
| `[ ]` | `ticker` | No | Ticker Notification |
| `[ ]` | `candlestick` | No | Candlestick Notification |
| `[ ]` | `ammpool` | No | AMM Pool Snapshot Notification |
| `[ ]` | `blockgen` | No | L2 Block Generation Notification |


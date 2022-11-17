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
- Dual Investment

### Loopring DEX API Features

- Account data
- Market data
- AMM (Automated Market Maker)
- Mint, buy and sell NFTs on Loopring L2
- Dual Investment


### Implemented API Endpoints (41/146)
| Status  | Endpoint | Description | Method |
| ------- | -------- | ----------- | ------ |
| `[ ]` | `/api/v2/amm/poolsStats` | TBD | GET |
| `[ ]` | `/api/v2/game/user/rank` | TBD | GET |
| `[ ]` | `/api/v2/orders/byClientOrderId` | Cancel multiple orders by clientOrderIds | DELETE |
| `[ ]` | `/api/v2/orders/byHash` | Cancel multiple orders by hash | DELETE |
| `[ ]` | `/api/v2/sidecar/liquidityMining` | TBD | TBD |
| `[ ]` | `/api/v2/sidecar/liquidityMiningUserHistory` | TBD | TBD |
| `[x]` | `/api/v3/account` | Query user information | GET |
| `[ ]` | `/api/v3/amm/assets` | TBD | TBD |
| `[x]` | `/api/v3/amm/balance` | Get AMM pool balance snapshot | GET |
| `[ ]` | `/api/v3/amm/balances` | TBD | GET |
| `[ ]` | `/api/v3/amm/exit` | Exit AMM pool | POST |
| `[ ]` | `/api/v3/amm/join` | Join AMM pool | POST |
| `[x]` | `/api/v3/amm/pools` | Get AMM pool configurations | GET |
| `[ ]` | `/api/v3/amm/rewards` | TBD | GET |
| `[x]` | `/api/v3/amm/trades` | Get AMM pool trade transactions | GET |
| `[x]` | `/api/v3/amm/transactions` | Return the user's AMM join/exit transactions | GET |
| `[ ]` | `/api/v3/amm/user/rewards` | TBD | GET |
| `[ ]` | `/api/v3/amm/user/transactions` | TBD | GET |
| `[x]` | `/api/v3/apiKey` | Update user's ApiKey | POST |
| `[x]` | `/api/v3/candlestick` | Get market candlestick | GET |
| `[ ]` | `/api/v3/collection/deployTokenAddress` | TBD | POST |
| `[ ]` | `/api/v3/counterFactualInfo` | TBD | TBD |
| `[ ]` | `/api/v3/datacenter/getLatestTokenPrices` | TBD | GET |
| `[ ]` | `/api/v3/datacenter/getUserAssets` | Get user VIP assets | GET |
| `[ ]` | `/api/v3/datacenter/getUserTradeAmount` | TBD | GET |
| `[ ]` | `/api/v3/defi/markets` | TBD | GET |
| `[ ]` | `/api/v3/defi/order` | TBD | POST |
| `[ ]` | `/api/v3/defi/rewards` | TBD | GET |
| `[ ]` | `/api/v3/defi/tokens` | TBD | GET |
| `[ ]` | `/api/v3/defi/transactions` | TBD | GET |
| `[ ]` | `/api/v3/delegator/getCode` | TBD | TBD |
| `[ ]` | `/api/v3/delegator/ipfs` | TBD | TBD |
| `[x]` | `/api/v3/depth` | Get market orderbook | GET |
| `[ ]` | `/api/v3/dual/balance` | TBD | GET |
| `[ ]` | `/api/v3/dual/index` | TBD | GET |
| `[ ]` | `/api/v3/dual/infos` | TBD | GET |
| `[ ]` | `/api/v3/dual/lockRecordAmount` | TBD | GET |
| `[ ]` | `/api/v3/dual/order` | TBD | POST |
| `[ ]` | `/api/v3/dual/prices` | TBD | GET |
| `[ ]` | `/api/v3/dual/rules` | TBD | GET |
| `[ ]` | `/api/v3/dual/transactions` | TBD | GET |
| `[ ]` | `/api/v3/eth/allowances` | TBD | GET |
| `[ ]` | `/api/v3/eth/balances` | TBD | GET |
| `[ ]` | `/api/v3/eth/nonce` | TBD | GET |
| `[ ]` | `/api/v3/eth/recommendedGasPrice` | TBD | GET |
| `[ ]` | `/api/v3/eth/recommendedGasPriceRange` | TBD | GET |
| `[ ]` | `/api/v3/eth/tokenBalances` | TBD | GET |
| `[ ]` | `/api/v3/eth/tokenBalances/all` | TBD | GET |
| `[ ]` | `/api/v3/exchange/feeInfo` | TBD | GET |
| `[x]` | `/api/v3/exchange/info` | Get exchange configurations | GET |
| `[x]` | `/api/v3/exchange/markets` | Get market configurations | GET |
| `[ ]` | `/api/v3/exchange/notWithdrawContractTokens` | TBD | GET |
| `[ ]` | `/api/v3/exchange/recommended` | TBD | GET |
| `[x]` | `/api/v3/exchange/tokens` | Get token configurations | GET |
| `[ ]` | `/api/v3/exchange/withdrawalAgents` | TBD | GET |
| `[ ]` | `/api/v3/game/rank` | Get AMM Pool game rank | GET |
| `[ ]` | `/api/v3/getAvailableBroker` | Get available broker | GET |
| `[ ]` | `/api/v3/luckyToken/agents` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/authorizedSigners` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/claimLuckyToken` | TBD | POST |
| `[ ]` | `/api/v3/luckyToken/sendLuckyToken` | TBD | POST |
| `[ ]` | `/api/v3/luckyToken/user/balances` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/user/claimHistory` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/user/claimedLuckyTokens` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/user/luckyTokenDetail` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/user/luckyTokens` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/user/summary` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/user/withdrawals` | TBD | GET |
| `[ ]` | `/api/v3/luckyToken/user/withdraws` | TBD | POST |
| `[x]` | `/api/v3/mix/candlestick` | api.getMixedCandlestick.value | GET |
| `[x]` | `/api/v3/mix/depth` | api.getMixedDepth.value | GET |
| `[x]` | `/api/v3/mix/markets` | api.getMixedMarkets.value | GET |
| `[x]` | `/api/v3/mix/ticker` | api.getMixedTicker.value | GET |
| `[ ]` | `/api/v3/new/user/nft/trades` | Get user NFT trade history (new) | GET |
| `[ ]` | `/api/v3/nft/collection` | Get NFT collection | GET |
| `[ ]` | `/api/v3/nft/collection` | Create NFT collection | POST |
| `[ ]` | `/api/v3/nft/collection` | Delete NFT collection | DELETE |
| `[ ]` | `/api/v3/nft/collection/edit` | Edit NFT collection | POST |
| `[ ]` | `/api/v3/nft/collection/legacy` | Get NFT legacy collection | GET |
| `[ ]` | `/api/v3/nft/collection/legacy/balance` | Get NFT legacy balance | GET |
| `[ ]` | `/api/v3/nft/collection/legacy/tokenAddress` | Get NFT legacy collection token address | GET |
| `[ ]` | `/api/v3/nft/collection/legacy/tokenAddress` | Create NFT legacy collection | POST |
| `[ ]` | `/api/v3/nft/collection/legacy/updateNftCollection` | Update NFT legacy collection | POST |
| `[ ]` | `/api/v3/nft/deployTokenAddress` | TBD | GET |
| `[ ]` | `/api/v3/nft/image/refresh` | TBD | POST |
| `[x]` | `/api/v3/nft/info/nfts` | Query NFT info by looprings nftData | GET |
| `[ ]` | `/api/v3/nft/mint` | Mint a NFT token on Loopring L2 | POST |
| `[ ]` | `/api/v3/nft/public/collection` | TBD | GET |
| `[ ]` | `/api/v3/nft/public/collection/items` | TBD | GET |
| `[ ]` | `/api/v3/nft/trade` | Settle down an NFT trade which has two matched orders | POST |
| `[ ]` | `/api/v3/nft/transfer` | Submit internal NFT transfer | POST |
| `[ ]` | `/api/v3/nft/validateOrder` | Validate a NFT order | POST |
| `[ ]` | `/api/v3/nft/withdrawal` | Withdraw a NFT token | POST |
| `[x]` | `/api/v3/order` | Submit an order | POST |
| `[x]` | `/api/v3/orders` | Get multiple orders | GET |
| `[x]` | `/api/v3/price` | Get token fiat prices | GET |
| `[ ]` | `/api/v3/refer` | Set referrer | TBD |
| `[ ]` | `/api/v3/sidecar/ProtocolPortrait` | Get Protocol Portrait | GET |
| `[ ]` | `/api/v3/sidecar/activityRules` | Get AMM activity rules | GET |
| `[ ]` | `/api/v3/spi/getAccountServices` | Get account services | GET |
| `[x]` | `/api/v3/storageId` | Get next storage ID | GET |
| `[x]` | `/api/v3/ticker` | Get market ticker | GET |
| `[x]` | `/api/v3/timestamp` | Get relayer's current time | GET |
| `[x]` | `/api/v3/trade` | Get market recent trades | GET |
| `[ ]` | `/api/v3/transfer` | Submit internal transfer | POST |
| `[x]` | `/api/v3/user/balances` | Get user exchange balances | GET |
| `[ ]` | `/api/v3/user/collection/details` | TBD | GET |
| `[x]` | `/api/v3/user/createInfo` | Get user registration transactions | GET |
| `[t]` | `/api/v3/user/deposits` | Get user deposit history | GET |
|  | `/api/v3/user/feeRates` | DEPRECATED | --- |
| `[ ]` | `/api/v3/user/forceWithdrawals` | TBD | POST |
| `[x]` | `/api/v3/user/nft/balances` | Get user's NFT balance | GET |
| `[ ]` | `/api/v3/user/nft/collection/balances` | Get user NFT balances by collection | GET |
| `[t]` | `/api/v3/user/nft/deposits` | Get user's NFT deposit history | GET |
| `[t]` | `/api/v3/user/nft/mints` | Get user's NFT mint history | GET |
| `[x]` | `/api/v3/user/nft/offchainFee` | Query current NFT requests fee amount | GET |
| `[t]` | `/api/v3/user/nft/trades` | Get user's NFT trade list (old) | GET |
| `[ ]` | `/api/v3/user/nft/transactions` | Get user NFT transaction history | GET |
| `[x]` | `/api/v3/user/nft/transfers` | Get user's NFT transfer history | GET |
| `[ ]` | `/api/v3/user/nft/updateNftPreference` | TBD | GET |
| `[t]` | `/api/v3/user/nft/withdrawals` | Get user's NFT withdrawal history | GET |
| `[x]` | `/api/v3/user/offchainFee` | Query current fee amount | GET |
|  | `/api/v3/user/orderAmount` | IGNORED (per Loopring doc) | --- |
| `[x]` | `/api/v3/user/orderFee` | Query user place order fee rate | GET |
| `[x]` | `/api/v3/user/orderUserRateAmount` | Query current token minimum amount to place order based on user's VIP level and max fee bips | GET |
| `[x]` | `/api/v3/user/trades` | Get user trade history | GET |
| `[ ]` | `/api/v3/user/transactions` | TBD | GET |
| `[x]` | `/api/v3/user/transfers` | Get user transfer list | GET |
| `[x]` | `/api/v3/user/updateInfo` | Get password reset transactions | GET |
| `[ ]` | `/api/v3/user/vipInfo` | Get user's VIP info | GET |
| `[t]` | `/api/v3/user/withdrawals` | Get user onchain withdrawal history | GET |
| `[ ]` | `/api/v3/user/withdrawals` | TBD | POST |
| `[ ]` | `/api/wallet/v3/contractVersion` | Get wallet contract version | GET |
| `[ ]` | `/api/wallet/v3/getAppConfigs` | Get Hebao config | GET |
| `[ ]` | `/api/wallet/v3/getGuardianApproveList` | Get Guardian Approve list | GET |
| `[ ]` | `/api/wallet/v3/getProtects` | TBD | GET |
| `[ ]` | `/api/wallet/v3/officialLockOrUnlock` | TBD | GET |
| `[ ]` | `/api/wallet/v3/operationLogs` | Get operation logs | GET |
| `[ ]` | `/api/wallet/v3/rejectApproveSignature` | Get rejected 'Approve Signature' | GET |
| `[ ]` | `/api/wallet/v3/resolveEns` | TBD | GET |
| `[ ]` | `/api/wallet/v3/resolveName` | TBD | GET |
| `[ ]` | `/api/wallet/v3/sendMetaTx` | TBD | GET |
| `[ ]` | `/api/wallet/v3/submitApproveSignature` | Get accepted 'Approve Signature' | TBD |
| `[ ]` | `/api/wallet/v3/tokenPrices` | TBD | GET |
| `[ ]` | `/api/wallet/v3/userAssets` | TBD | GET |
| `[ ]` | `/api/wallet/v3/wallet/type` | TBD | GET |
| `[ ]` | `/api/wallet/v3/walletModules` | TBD | GET |
| `[x]` | `/v3/ws/key` | Get WebSocket API key | GET |



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


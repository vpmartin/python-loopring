import json
import loopring

from loopring.client import Client
from loopring.utils.enums import *

with open('account.json', 'r') as f:
    params = json.load(f)

client = Client(**params, base_url=BaseUrl.MAINNET)

resp = client.get_nft_order_minimum_amount('0x14c9909135bc3ca8761cdbc7f8926a8b0de7de49a2dc32eac540cee21144cdd0')

# "nftData": "0x14c9909135bc3ca8761cdbc7f8926a8b0de7de49a2dc32eac540cee21144cdd0",
# "tokenAddress": "0x9d226054324360d8eeb024f66731d6c5e44e8c6f",
#minter": "0x8d0b24f4c4eb9b0b450cfce37e1b842d3005c1d8",

print(f'Request response:\n{json.dumps(resp, indent=4)}')

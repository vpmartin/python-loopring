import json
import loopring

from loopring.client import Client
from loopring.utils.enums import *

with open('account.json', 'r') as f:
    params = json.load(f)

client = Client(**params, base_url=BaseUrl.MAINNET)

"""
resp = client.submit_order(sell_token='USDC', sell_volume=101,
                           buy_token='ETH', buy_volume=0.07875,
                           all_or_none=False, fill_amount_b_or_s=False,
                           valid_until=1700000000, max_fee_bips=30)
"""

resp = client.get_l2_block_info(31131)

print(f'Request response:\n{json.dumps(resp, indent=4)}')

import json
import loopring

from loopring.client import Client
from loopring.utils.enums import *

with open('account.json', 'r') as f:
    params = json.load(f)

client = Client(**params, base_url=BaseUrl.MAINNET)

resp = client.get_current_fee(OffchainRequestType.OPEN_ACCOUNT)

print(f'Request response:\n{json.dumps(resp, indent=4)}')

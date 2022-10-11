import json

from loopring.client import Client

with open('account.json', 'r') as f:
    params = json.load(f)

client = Client(**params)

print(f'Server timestamp: f{client.get_server_timestamp()}')

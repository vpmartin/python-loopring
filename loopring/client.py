import requests

from py_eth_sig_utils import utils as sig_utils
from py_eth_sig_utils.signing import v_r_s_to_signature

from typing import Optional

from loopring.utils.enums import *
from loopring.utils.sign.eddsa import *
from loopring.utils.exceptions import *

SIGN_MAX_INPUT = 13


class BaseClient:
    def __init__(self, **kwargs):
        # Defaults to Mainnet if no `base_url` kwarg found
        self.base_url = kwargs.get('base_url', BaseUrl.MAINNET)

        self.account_id = int(kwargs.get('accountId'))
        self.address = kwargs.get('address')
        self.api_key  = kwargs.get('apiKey')
        self.public_key_x = kwargs.get('publicX')
        self.public_key_y = kwargs.get('publicY')
        self.eddsa_key = kwargs.get('privateKey')

        if kwargs.get('ecdsaKey', None) is not None:
            self.ecdsa_key = int(kwargs.get('ecdsaKey', 16).to_bytes(32, byteorder='big'))

        self.pairs = None
        self.tokens = None
        self.token_configs = None

        self.exchange_address = self.get_exchange_configurations()['exchangeAddress']

        print(f'Client initialized on {self.base_url} for {self.address}')

    def _sign(self, req: requests.Request, sec: Security) -> requests.Request:
        """
        Signs an HTTP request with the correct security level

        :param req: HTTP request to sign
        :type req: requests.Request
        :return: signed request
        :rtype: requests.Request
        """
        # Add the API Key as a header
        req.headers.update({'X-API-KEY': self.api_key})

        # Compute the right signature given the security level
        signature = None

        if sec in [Security.EDDSA_URL, Security.BODY_EDDSA]:
            signer = UrlEddsaSignHelper(self.eddsa_key, self.base_url)
            signature = signer.sign(req)

        elif sec == Security.ECDSA_URL:
            signer = UrlEddsaSignHelper(self.eddsa_key, self.base_url)
            msg = signer.hash(req)
            v, r, s = sig_utils.ecsign(msg, self.ecdsa_key)
            signature = "0x" + bytes.hex(v_r_s_to_signature(v, r, s)) + "02"

        if sec == Security.EDDSA_ORDER:
            signer = OrderEddsaSignHelper(self.eddsa_key)
            hash = signer.hash(req.data)
            signature = signer.sign(req.data)

        # Add the signature to the right place, either header or body
        if signature is not None:
            if sec in [Security.BODY_EDDSA, Security.EDDSA_ORDER]:
                req.data['eddsaSignature'] = signature

            if sec == Security.EDDSA_ORDER:
                req.data['hash'] = hash

            req.headers.update({'X-API-SIG': signature})

        return req


    def _make(self, method: str,  endpoint: str, params: dict={},
              data: dict={}, security=Security.NONE) -> requests.Request:
        """
        Creates a `requests.Request` object to be sent later.

        :param method: GET, POST, DELETE, PUT, QUERY
        :param endpoint: REST API endpoint to request to
        :param params: GET in-url parameters
        :param data: POST in-body parameters
        :param security: security level
        :type method: str
        :type endpoint: str
        :type params: dict
        :type data: dict
        :type security: Security
        :return: raw HTTP request that needs to be sent
        :rtype: requests.Request
        """
        # Clear the eventual 'None' values in GET params and POST data
        filtered_params = {k: v for k, v in params.items() if v is not None}
        params.clear()
        params.update(filtered_params)

        filtered_data = {k: v for k, v in data.items() if v is not None}
        data.clear()
        data.update(filtered_data)

        # Get the full URL
        full_url = urllib.parse.urljoin(self.base_url, endpoint)

        # Create the Request object
        req = requests.Request(
                method=method, url=full_url, params=params, data=data
        )
        # Include Content-Type header
        req.headers.update({'Content-Type': 'application/json'})

        # Sign the request with the corresponding signature type
        req = self._sign(req, security)

        return req

    def _send(self, req: requests.Request) -> requests.Response:
        """
        Prepare a `Request` object in a `PreparedRequest` object, send it to
        the server, close the session and return the reponse.

        :param req: HTTP request to send
        :type req: requests.Request
        :return: response
        :rtype: requests.Response
        """
        req.data = json.dumps(req.data, separators=(',',':'))
        pr = req.prepare()
        self._dump(pr)
        s = requests.Session()
        res = s.send(pr)
        s.close()
        return res

    def request(self, method: str,  endpoint: str, params: dict={},
                data: dict={}, security=Security.NONE) -> dict:
        """
        Creates a request by calling `BaseClient._make`, which also signs the
        request given the security level, then send it and return the response
        in JSON format.

        :param method: GET, POST, DELETE, PUT, QUERY
        :param endpoint: REST API endpoint to request to
        :param params: GET in-url parameters
        :param data: POST in-body parameters
        :param security: security level
        :type method: str
        :type endpoint: str
        :type params: dict
        :type data: dict
        :type security: Security
        :return: reponse from the server
        :rtype: dict
        """
        req = self._make(method, endpoint, params, data, security)
        res = self._send(req)
        return res.json()

    def _dump(self, req):
        """
        Debugging purposes. From https://stackoverflow.com/a/23816211.
        """
        print('{}\n{}\r\n{}\r\n\r\n'.format(
            '-----------START-----------',
            req.method + ' ' + req.url,
            '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            ) + json.dumps(req.body, indent=4))
        print()

    def _format_reponse(self, resp, keys):
        if type(resp[0]) == list:
            result = []
            for values in resp:
                result.append(dict(zip(keys, values)))
        else:
            result = dict(zip(keys, resp))

        return result

    def _init_pairs(self):
        resp = self.get_market_configurations()
        self.pairs = [pair['market'] for pair in resp['markets']]

    def _init_tokens(self):
        resp = self.get_token_configurations()
        self.tokens = {token['symbol']: token['tokenId'] for token in resp}

    def _init_token_configs(self):
        self.token_configs = {}
        for tk_cfg in self.get_token_configurations():
            # Add an entry with key being the token symbol
            self.token_configs[tk_cfg['symbol']] = tk_cfg
            # Add a second entry with key being the token ID
            self.token_configs[self.token_symbol_to_id(tk_cfg['symbol'])] = tk_cfg

    def _validate_pair(self, pair, allow_none=False, allow_multipair=False):
        if pair is None and allow_none:
            return True

        if self.pairs is None:
            self._init_pairs()

        if type(pair) == str:
            all_pairs = pair.split(',')
        else:
            all_pairs = list(pair)

        if not allow_multipair and len(all_pairs) > 1:
            raise MultipleNotAllowedException('Trading Pair', pair)

        if len(all_pairs) > 1:
            for p in all_pairs:
                self._validate_enum(p)
        else:
            if not pair in self.pairs:
                inverted = '-'.join(pair.split('-')[::-1])
                if inverted in self.pairs:
                    raise InvertedTradingPairException(pair)
                else:
                    raise InvalidTradingPairException(pair)

        return True

    def _validate_enum(self, cls, value, allow_none=False, allow_multiple=False):
        if value is None and allow_none:
            return True

        class_values = [getattr(cls, attr) for attr in dir(cls)
                  if not callable(getattr(cls, attr))
                  and not attr.startswith("__")]

        if type(value) == str:
            all_values = value.split(',')
        else:
            all_values = list(value)

        if not allow_multiple and len(all_values) > 1:
            raise MultipleNotAllowedException(cls, value)

        if len(all_values) > 1:
            for v in all_values:
                self._validate_enum(v, allow_none=allow_none)
        else:
            if allow_none:
                class_values.append(None)

            if value not in class_values:
                raise InvalidEnumException(cls, value)

        return True

    def _validate_symbol(self, symbol, allow_none=False):
        if symbol is None and allow_none:
            return True

        if self.tokens is None:
            self._init_tokens()

        if symbol not in self.tokens.keys():
            raise InvalidSymbolException(symbol,
                                         valid_symbols=list(self.tokens.keys()))

    def token_symbol_to_id(self, symbol):
        if self.tokens is None:
            self._init_tokens()

        if symbol is None:
            return None

        if all([s.isnumeric() for s in symbol.split(',')]):
            return symbol

        all_tokens = symbol.split(',')
        all_token_ids = []
        for token in all_tokens:
            if not token.isnumeric():
                all_token_ids.append(str(self.tokens[token]))

        tokens = ','.join(all_token_ids)
        return tokens

    def adjust_volume(self, token, vol):
        if self.token_configs is None:
            self._init_token_configs()

        dec = self.token_configs[token]['decimals']

        if sum(c.isdigit() for c in str(vol)) < dec:
            new_vol = float(vol) * (10 ** dec)
            return f'{new_vol:.{dec}f}'.split('.')[0]
        else:
            return str(vol)

    ### --- API ENDPOINTS --- ###

    # -- Loopring Utilities --
    def get_l2_block_info(self):
        pass

    def get_pending_txs(self):
        pass

    def get_server_timestamp(self):
        return self.request('GET', '/api/v3/timestamp')


    # -- User-related Endpoints --
    def get_user_apikey(self):
        return self.request('GET', '/api/v3/apiKey',
                            params={'accountId': self.account_id},
                            security=Security.EDDSA_URL)

    def update_user_apikey(self):
        return self.request('POST', '/api/v3/apiKey',
                            data={'accountId': self.account_id},
                            security=Security.EDDSA_URL)

    def get_next_storage_id(self, sell_token_id, max_next: Optional = None):
        sell_token_id = self.token_symbol_to_id(sell_token_id)
        return self.request('GET', '/api/v3/storageId',
                            params={'accountId': self.account_id,
                                    'sellTokenId': sell_token_id,
                                    'maxNext': max_next})

    def get_order_details(self, order_hash):
        return self.request('GET', '/api/v3/order',
                            params={'accountId': self.account_id,
                                    'orderHash': order_hash})

    def submit_order(self, sell_token, sell_volume, buy_token, buy_volume,
                     all_or_none, fill_amount_b_or_s, valid_until,
                     max_fee_bips, client_order_id: Optional = None,
                     order_type: Optional = None,
                     trade_channel: Optional = None, taker: Optional = None,
                     pool_address: Optional = None, affiliate: Optional = None):
        sell_token_id = self.token_symbol_to_id(sell_token)
        buy_token_id = self.token_symbol_to_id(buy_token)

        storage_id = self.get_next_storage_id(sell_token)['orderId']

        buy_volume = self.adjust_volume(buy_token_id, buy_volume)
        sell_volume = self.adjust_volume(sell_token_id, sell_volume)

        return self.request('POST', 'api/v3/order',
                            data={
                                'exchange': self.exchange_address,
                                'accountId': self.account_id,
                                'storageId': storage_id,
                                'sellToken': {
                                    'tokenId': int(sell_token_id),
                                    'volume': sell_volume
                                },
                                'buyToken': {
                                    'tokenId': int(buy_token_id),
                                    'volume': buy_volume
                                },
                                'allOrNone': all_or_none,
                                'fillAmountBOrS': fill_amount_b_or_s,
                                'validUntil': valid_until,
                                'maxFeeBips': max_fee_bips,
                                'clientOrderId': client_order_id,
                                'orderType': order_type,
                                'tradeChannel': trade_channel,
                                'taker': taker,
                                'poolAddress': pool_address,
                                'affiliate': affiliate
                            },
                            security=Security.EDDSA_ORDER)

    def cancel_order(self, order_hash: Optional = None,
                     client_order_id: Optional = None):
        if order_hash is None and client_order_id is None:
            raise Exception("cancel_order: One of order_hash or client_order_id"
                            " must be specified for an order to be cancelled.")

        return self.request('DELETE', '/api/v3/order',
                            params={'accountId': self.account_id,
                                    'orderHash': order_hash,
                                    'clientOrderId': client_order_id},
                            security=Security.EDDSA_URL)

    def get_multiple_orders(self):
        pass

    def get_market_configurations(self):
        return self.request('GET', '/api/v3/exchange/markets')

    def get_token_configurations(self):
        return self.request('GET', '/api/v3/exchange/tokens')

    def get_exchange_configurations(self):
        return self.request('GET', '/api/v3/exchange/info')

    def get_market_orderbook(self, pair, level, limit=50):
        self._validate_pair(pair)

        return self.request('GET', '/api/v3/depth',
                            params={'market': pair, 'level': level,
                                    'limit': limit})

    def get_market_ticker(self, pair):
        self._validate_pair(pair, allow_multipair=True)

        resp = self.request('GET', '/api/v3/ticker',
                            params={'market': pair})

        return self._format_reponse(resp['tickers'],
                                    keys=['tradingPair', 'timestamp',
                                          'baseVolume', 'quoteVolume',
                                          'open', 'high', 'low', 'close',
                                          'trades',
                                          'highestBid', 'lowestAsk',
                                          'baseFee', 'quoteFee'])

    def get_market_candlestick(self, pair, interval, start: Optional = None,
                               end: Optional = None, limit: Optional = None):
        self._validate_pair(pair)
        self._validate_enum(KlineInterval, interval)

        resp = self.request('GET', '/api/v3/candlestick',
                            params={'market': pair, 'interval': interval,
                                    'start': start, 'end': end,
                                    'limit': limit})

        resp['candlesticks'] =  self._format_reponse(resp['candlesticks'],
                                            keys=['timestamp', 'trades',
                                                  'open', 'close', 'high',
                                                  'low', 'baseVolume',
                                                  'quoteVolume'])
        return resp

    def get_token_fiat_prices(self, fiat):
        self._validate_enum(Fiat, fiat)
        return self.request('GET', '/api/v3/price',
                            params={'legal': fiat})

    def get_market_recent_trades(self, pair, limit: Optional = None,
                                 fill_type: Optional = None):
        self._validate_pair(pair)
        self._validate_enum(FillType, fill_type, allow_none=True)

        resp = self.request('GET', '/api/v3/trade',
                            params={'market': pair,
                                    'limit': limit,
                                    'fillTypes': fill_type})

        trades = self._format_reponse(resp['trades'],
                                      keys=['timestamp', 'recordId', 'side',
                                            'volume', 'price', 'market',
                                            'fees', 'blockId', 'indexInBlock'])

        resp['trades'] = trades
        return resp

    def submit_internal_transfer(self):
        pass

    def get_user_info(self):
        return self.request('GET', '/api/v3/account',
                            params={'owner': self.address,
                                    'accountId': self.account_id})

    def update_eddsa_key(self):
        pass

    def get_registration_txs(self, start: Optional = None, end: Optional = None,
                             status: Optional = None, limit: Optional = None,
                             offset: Optional = None):
        self._validate_enum(AccountTransactionStatus, status, allow_none=True,
                            allow_multiple=True)

        return self.request('GET', '/api/v3/user/createInfo',
                            params={'accountId': self.account_id,
                                    'start': start, 'end': end,
                                    'status': status, 'limit': limit,
                                    'offset': offset})

    def get_password_reset_txs(self, start: Optional = None, end: Optional = None,
                             status: Optional = None, limit: Optional = None,
                             offset: Optional = None):
        self._validate_enum(AccountTransactionStatus, status, allow_none=True,
                            allow_multiple=True)

        return self.request('GET', '/api/v3/user/updateInfo',
                            params={'accountId': self.account_id,
                                    'start': start, 'end': end,
                                    'status': status, 'limit': limit,
                                    'offset': offset})

    def get_balance(self, tokens: Optional = None):
        tokens = self.token_symbol_to_id(tokens)
        return self.request('GET', '/api/v3/user/balances',
                            params={'accountId': self.account_id,
                                    'tokens': tokens})

    def get_onchain_withdrawal_history(
            self, start: Optional = None, end: Optional = None,
            status: Optional = None, limit: Optional = None,
            token_symbol: Optional = None, offset: Optional = None,
            withdrawal_types: Optional = None, hashes: Optional = None):
        self._validate_symbol(token_symbol, allow_none=True)
        self._validate_enum(AccountTransactionStatus, status, allow_none=True,
                            allow_multiple=True)
        self._validate_enum(WithdrawalType, withdrawal_types, allow_none=True)

        return self.request('GET', '/api/v3/user/deposits',
                            params={'accountId': self.account_id,
                                    'start': start, 'end': end,
                                    'status': status, 'limit': limit,
                                    'tokenSymbol': token_symbol,
                                    'offset': offset,
                                    'withdrawalTypes': withdrawal_types,
                                    'hashes': hashes})

    def submit_offchain_withdrawal_request(self):
        pass

    def get_deposit_history(self, start: Optional = None, end: Optional = None,
                             status: Optional = None, limit: Optional = None,
                             token_symbol: Optional = None,
                             offset: Optional = None, hashes: Optional = None):
        self._validate_symbol(token_symbol, allow_none=True)
        self._validate_enum(AccountTransactionStatus, status, allow_none=True,
                            allow_multiple=True)

        return self.request('GET', '/api/v3/user/deposits',
                            params={'accountId': self.account_id,
                                    'start': start, 'end': end,
                                    'status': status, 'limit': limit,
                                    'tokenSymbol': token_symbol,
                                    'offset': offset, 'hashes': hashes})

    def get_transfer_history(
            self, start: Optional = None, end: Optional = None,
            status: Optional = None, limit: Optional = None,
            token_symbol: Optional = None, offset: Optional = None,
            transfer_types: Optional = None, hashes: Optional = None):
        self._validate_symbol(token_symbol, allow_none=True)
        self._validate_enum(AccountTransactionStatus, status, allow_none=True,
                            allow_multiple=True)
        #self._validate_enum(WithdrawalType, withdrawal_type, allow_none=True)

        return self.request('GET', '/api/v3/user/transfers',
                            params={'accountId': self.account_id,
                                    'start': start, 'end': end,
                                    'status': status, 'limit': limit,
                                    'tokenSymbol': token_symbol,
                                    'offset': offset,
                                    'transferTypes': transfer_types,
                                    'hashes': hashes})

    def get_trade_history(self, pair: Optional = None,
                          order_hash: Optional = None, offset: Optional = None,
                          limit: Optional = None, from_id: Optional = None,
                          fill_types: Optional = None):
        self._validate_pair(pair, allow_none=True)
        self._validate_enum(FillType, fill_types, allow_none=True,
                            allow_multiple=True)

        resp = self.request('GET', '/api/v3/user/trades',
                            params={'accountId': self.account_id,
                                    'market': pair, 'orderHash': order_hash,
                                    'offset': offset, 'limit': limit,
                                    'fromId': from_id, 'fillTypes': fill_types}
                            )

        resp['trades'] = self._format_reponse(resp['trades'],
                                              keys=['timestamp', 'recordId',
                                                    'side', 'baseVolume',
                                                    'quoteVolume', 'market',
                                                    'UNKNOWN1', 'UNKNOWN2',
                                                    'UNKNOWN3', 'accountId',
                                                    'tokenId', 'storageId',
                                                    'orderId'])
        return resp

    def get_order_placing_fee(self, market, buy_token, buy_amount):
        self._validate_pair(market, allow_multipair=True)
        buy_token = self.token_symbol_to_id(buy_token)

        return self.request('GET', '/api/v3/user/orderFee',
                            params={'accountId': self.account_id,
                                    'market': market,
                                    'tokenB': buy_token,
                                    'amountB': buy_amount})

    def get_order_minimum_amount(self, pair):
        self._validate_pair(pair)
        return self.request('GET', '/api/v3/user/orderUserRateAmount',
                            params={'accountId': self.account_id,
                                    'market': pair})

    def get_current_fee(self, request_type, token_symbol: Optional = None,
                        amount: Optional = None):
        self._validate_enum(OffchainRequestType, request_type)
        self._validate_symbol(token_symbol, allow_none=True)
        return self.request('GET', '/api/v3/user/offchainFee',
                            params={'accountId': self.account_id,
                                    'requestType': request_type,
                                    'tokenSymbol': token_symbol,
                                    'amount': amount})

    # --- AMM Pool Endpoints ---

    def get_amm_pool_configurations(self):
        pass

    def get_amm_pool_balance_snapshot(self):
        pass

    def join_amm_pool(self):
        pass

    def exit_amm_pool(self):
        pass

    def get_amm_join_exit_txs(self):
        pass

    def get_amm_pool_trade_txs(self):
        pass

    # --- NFT Endpoints ---

    def mint_nft(self):
        pass

    def transfer_nft(self):
        pass

    def validate_nft_order(self):
        pass

    def settle_nft_trade(self):
        pass

    def withdraw_nft(self):
        pass

    def get_nft_info1(self):
        pass

    def get_nft_info2(self):
        pass

    def get_nft_holders(self):
        pass

    def get_nft_order_minimum_amount(self):
        pass

    def get_nft_balance(self):
        pass

    def get_nft_trade_history(self):
        pass

    def get_nft_transfer_history(self):
        pass

    def get_nft_mint_history(self):
        pass

    def get_nft_deposit_history(self):
        pass

    def get_nft_withdrawal_history(self):
        pass

    def get_nft_fee(self):
        pass

    def get_nft_order_placing_fee(self):
        pass


class Client(BaseClient):
    pass


class AsyncClient(BaseClient):
    pass

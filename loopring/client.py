import re
import requests

SIGN_MAX_INPUT = 13

from py_eth_sig_utils import utils as sig_utils
from py_eth_sig_utils.signing import v_r_s_to_signature

from typing import Optional, Any

from loopring.utils.enums import *
from loopring.utils.sign.eddsa import *

class BaseClient:
    def __init__(self, **kwargs):
        # Defaults to Mainnet if no `base_url` kwarg found
        self.base_url = kwargs.get('base_url', BaseUrl.MAINNET)

        self.address = kwargs.get('address')
        self.api_key  = kwargs.get('apiKey')
        self.public_key_x = kwargs.get('publicX')
        self.public_key_y = kwargs.get('publicY')
        self.eddsa_key = kwargs.get('privateKey')

        if kwargs.get('ecdsaKey', None) is not None:
            self.ecdsa_key = int(kwargs.get('ecdsaKey', 16).to_bytes(32, byteorder='big'))

        print(f'Client initialized on {self.base_url} for {self.address}')

    def _validate(self, pattern: str, value: Any) -> bool:
        """
        Checks if the value given as parameter is allowed by the constants of
        BaseClient following the regex pattern `pattern`.

        :param pattern: regex pattern
        :param value: value to check
        :type pattern: str
        :type value: Any
        :return: whether 'value' is allowed
        :rtype: bool
        """
        r = re.compile(pattern)
        allowed = [getattr(self.__class__, s)
                   for s in list(filter(r.match, dir(self.__class__)))]
        return value in allowed

    def _sign(self, req: requests.Request) -> requests.Request:
        """
        Signs an HTTP request with the correct security level

        :param req: HTTP request to sign
        :type req: requests.Request
        :return: signed request
        :rtype: requests.Request
        """
        req.headers.update({'X-API-KEY': self.api_key})

        sec = req.data.pop('security', Security.NONE)

        signature = None

        if sec == Security.EDDSA_URL:
            signer = UrlEddsaSignHelper(self.eddsa_key, self.base_url)
            signature = signer.sign(req)
        elif sec == Security.ECDSA_URL:
            signer = UrlEddsaSignHelper(self.eddsa_key, self.base_url)
            msg = signer.hash(req)
            v, r, s = sig_utils.ecsign(msg, self.ecdsa_key)
            signature = "0x" + bytes.hex(v_r_s_to_signature(v, r, s)) + "02"

        if signature is not None:
            req.headers.update({'X-API-SIG': signature})

        return req


    def _make(self, method: str,  endpoint: str, params: list=[],
              data: dict= {}, security=Security.NONE) -> requests.Request:
        """
        Creates a `requests.Request` object to be sent later.

        :param method: GET, POST, DELETE, PUT, QUERY
        :param endpoint: REST API endpoint to request to
        :param params: GET in-url parameters
        :param data: POST in-body parameters
        :param security: security level
        :type method: str
        :type endpoint: str
        :type params: list
        :type data: dict
        :type security: Security
        :return: raw HTTP request that needs to be sent
        :rtype: requests.Request
        """
        data['security'] = security
        full_url = urllib.parse.urljoin(self.base_url, endpoint)
        req = requests.Request(
                method=method, url=full_url, params=params, data=data
        )
        req = self._sign(req)

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
        pr = req.prepare()
        s = requests.Session()
        res = s.send(pr)
        s.close()
        return res

    def request(self, method: str,  endpoint: str, params: list=[],
                data: dict={}, security=Security.NONE) -> dict:
        req = self._make(method, endpoint, params, data, security)
        res = self._send(req)
        return res.json()


    ### --- API ENDPOINTS ---
    def get_server_timestamp(self):
        return self.request('GET', '/api/v3/timestamp')

class Client(BaseClient):
    pass


class AsyncClient(BaseClient):
    pass

# EdDSA Signature Helpers
#
# Code base extracted from
# Loopring/hello_loopring/sdk/sign_utils/eddsa_utils.py
# with minor reformatting.
# All credit goes to Loopring dev team.

from abc import abstractmethod

from ethsnarks.field import FQ, SNARK_SCALAR_FIELD
from ethsnarks.poseidon import poseidon_params, poseidon
from loopring.utils.poseidoneddsa import PoseidonEdDSA

import urllib
import hashlib
import json


class EddsaSignHelper:
    def __init__(self, poseidon_sign_params, private_key):
        self.poseidon_sign_params = poseidon_sign_params
        self.private_key = private_key

    @abstractmethod
    def serialize_data(self, structure_data):
        pass

    def hash(self, structure_data):
        serialized_data = self.serialize_data(structure_data)
        msg_hash = poseidon(serialized_data, self.poseidon_sign_params)
        return msg_hash

    def sign(self, structure_data):
        msg_hash = self.hash(structure_data)
        signed_msg = PoseidonEdDSA.sign(msg_hash,
                                        FQ(int(self.private_key, 16)))
        return "0x" + "".join([
            hex(int(signed_msg.sig.R.x))[2:].zfill(64),
            hex(int(signed_msg.sig.R.y))[2:].zfill(64),
            hex(int(signed_msg.sig.s))[2:].zfill(64),
        ])


class UrlEddsaSignHelper(EddsaSignHelper):
    def __init__(self, private_key, host=""):
        self.host = host
        super(UrlEddsaSignHelper, self).__init__(
            poseidon_sign_params=poseidon_params(SNARK_SCALAR_FIELD, 2, 6, 53,
                                                 b'poseidon', 5,
                                                 security_target=128),
            private_key=private_key
        )

    def hash(self, structure_data):
        serialized_data = self.serialize_data(structure_data)
        hasher = hashlib.sha256()
        hasher.update(serialized_data.encode('utf-8'))
        msg_hash = int(hasher.hexdigest(), 16) % SNARK_SCALAR_FIELD
        # print(f"serialized_data = {serialized_data}, prehash = {
        # hasher.hexdigest()}, msg_hash = {hex(msg_hash)}")
        return msg_hash

    def serialize_data(self, request):
        method = request.method
        url = urllib.parse.quote(request.url, safe='')
        if method in ["GET", "DELETE"]:
            data = urllib.parse.quote("&".join(
                [f"{k}={urllib.parse.quote(str(v), safe='')}" for k, v in
                 request.params.items()]), safe='')
        elif method in ["POST", "PUT"]:
            data = urllib.parse.quote(
                json.dumps(request.data, separators=(',', ':')), safe='')
            print(f'data: {data}')
        else:
            raise Exception(f"Unknown request method {method}")

        # return "&".join([method, url.replace("http", "https"), data])
        print("&".join([method, url, data]))
        return "&".join([method, url, data])


class OrderEddsaSignHelper(EddsaSignHelper):
    def __init__(self, private_key):
        super(OrderEddsaSignHelper, self).__init__(
            poseidon_params(SNARK_SCALAR_FIELD, 12, 6, 53, b'poseidon', 5,
                            security_target=128),
            private_key
        )

    def serialize_data(self, order):
        return [
            int(order["exchange"], 16),
            int(order["storageId"]),
            int(order["accountId"]),
            int(order["sellToken"]['tokenId']),
            int(order["buyToken"]['tokenId']),
            int(order["sellToken"]['volume']),
            int(order["buyToken"]['volume']),
            int(order["validUntil"]),
            int(order["maxFeeBips"]),
            int(order["fillAmountBOrS"]),
            int(order.get("taker", "0x0"), 16)
        ]


class UpdateAccountEddsaSignHelper(EddsaSignHelper):
    def __init__(self, private_key):
        super(UpdateAccountEddsaSignHelper, self).__init__(
            poseidon_params(SNARK_SCALAR_FIELD, 9, 6, 53, b'poseidon', 5,
                            security_target=128),
            private_key
        )

    def serialize_data(self, account_update):
        return [
            int(account_update['exchange'], 16),
            int(account_update['accountId']),
            int(account_update['maxFee']['tokenId']),
            int(account_update['maxFee']['volume']),
            int(account_update['publicKey']['x'], 16),
            int(account_update['publicKey']['y'], 16),
            int(account_update['validUntil']),
            int(account_update['nonce'])
        ]


class OriginTransferEddsaSignHelper(EddsaSignHelper):
    def __init__(self, private_key):
        super(OriginTransferEddsaSignHelper, self).__init__(
            poseidon_params(SNARK_SCALAR_FIELD, 13, 6, 53, b'poseidon', 5,
                            security_target=128),
            private_key
        )

    def serialize_data(self, origin_transfer):
        return [
            int(origin_transfer['exchange'], 16),
            int(origin_transfer['payerId']),
            int(origin_transfer['payeeId']),  # payer_toAccountID
            int(origin_transfer['token']['tokenId']),
            int(origin_transfer['token']['volume']),
            int(origin_transfer['maxFee']['tokenId']),
            int(origin_transfer['maxFee']['volume']),
            int(origin_transfer['payeeAddr'], 16),  # payer_to
            0,  # int(origin_transfer.get('dualAuthKeyX', '0'),16),
            0,  # int(origin_transfer.get('dualAuthKeyY', '0'),16),
            int(origin_transfer['validUntil']),
            int(origin_transfer['storageId'])
        ]


class DualAuthTransferEddsaSignHelper(EddsaSignHelper):
    def __init__(self, private_key):
        super(DualAuthTransferEddsaSignHelper, self).__init__(
            poseidon_params(SNARK_SCALAR_FIELD, 13, 6, 53, b'poseidon', 5,
                            security_target=128),
            private_key
        )

    def serialize_data(self, dual_auth_transfer):
        return [
            int(dual_auth_transfer['exchange'], 16),
            int(dual_auth_transfer['accountId']),
            int(dual_auth_transfer['payee_toAccountID']),
            int(dual_auth_transfer['token']),
            int(dual_auth_transfer['amount']),
            int(dual_auth_transfer['feeToken']),
            int(dual_auth_transfer['maxFeeAmount']),
            int(dual_auth_transfer['to'], 16),
            int(dual_auth_transfer.get('dualAuthKeyX', '0'), 16),
            int(dual_auth_transfer.get('dualAuthKeyY', '0'), 16),
            int(dual_auth_transfer['validUntil']),
            int(dual_auth_transfer['storageId']),
        ]


class WithdrawalEddsaSignHelper(EddsaSignHelper):
    def __init__(self, private_key):
        super(WithdrawalEddsaSignHelper, self).__init__(
            poseidon_params(SNARK_SCALAR_FIELD, 10, 6, 53, b'poseidon', 5,
                            security_target=128),
            private_key
        )

    def serialize_data(self, withdraw):
        return [
            int(withdraw['exchange'], 16),
            int(withdraw['accountId']),
            int(withdraw['token']['tokenId']),
            int(withdraw['token']['volume']),
            int(withdraw['maxFee']['tokenId']),
            int(withdraw['maxFee']['volume']),
            int(withdraw['onChainDataHash'], 16),
            int(withdraw['validUntil']),
            int(withdraw['storageId']),
        ]


class MessageHashEddsaSignHelper(EddsaSignHelper):
    def __init__(self, private_key):
        super(MessageHashEddsaSignHelper, self).__init__(
            poseidon_params(SNARK_SCALAR_FIELD, 2, 6, 53, b'poseidon', 5, security_target=128),
            private_key
        )

    def hash(self, eip712_hash_bytes):
        return self.serialize_data(eip712_hash_bytes)

    def serialize_data(self, data):
        if isinstance(data, bytes):
            return int(data.hex(), 16) >> 3
        elif isinstance(data, str):
            return int(data, 16) >> 3
        else:
            raise TypeError("Unknown type " + str(type(data)))


from ethsnarks.eddsa import _SignatureScheme, as_scalar
from ethsnarks.field import SNARK_SCALAR_FIELD
from ethsnarks.poseidon import poseidon_params, poseidon

# Copy of PoseidonEdDSA class from Loopring/hello_loopring/sdk/ethsnarks/poseidoneddsa.py
#  for some reason it's not in the module downloaded from pypi
class PoseidonEdDSA(_SignatureScheme):
    @classmethod
    def hash_public(cls, *args):
        PoseidonHashParams = poseidon_params(SNARK_SCALAR_FIELD, 6, 6, 52, b'poseidon', 5, security_target=128)
        inputMsg = list(as_scalar(*args))
        return poseidon(inputMsg, PoseidonHashParams)
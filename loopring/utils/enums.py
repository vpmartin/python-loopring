class BaseUrl():
    MAINNET      = 'https://api3.loopring.io/'
    TESTNET_UAT2 = 'https://uat2.loopring.io/'
    TESTNET_UAT3 = 'https://uat3.loopring.io/'


class KlineInterval():
    INT_1MINUTE  = '1min'
    INT_5MINUTE  = '5min'
    INT_15MINUTE = '15min'
    INT_30MINUTE = '30min'
    INT_1HOUR    = '1hr'
    INT_2HOUR    = '2hr'
    INT_4HOUR    = '4hr'
    INT_12HOUR   = '12hr'
    INT_1DAY     = '1d'
    INT_1WEEK    = '1w'


class OrderType():
    LIMIT      = 'LIMIT'
    TAKER_ONLY = 'TAKER_ONLY'
    MAKER_ONLY = 'MAKER_ONLY'
    AMM        = 'AMM'


class OrderChannel():
    ORDER_BOOK = 'ORDER_BOOK'
    AMM_POOL   = 'AMM_POOL'
    MIXED      = 'MIXED'


class Side():
    BUY  = 'BUY'
    SELL = 'SELL'

class AccountTransactionStatus():
    PROCESSING = 'processing'
    PROCESSED  = 'processed'
    RECEIVED   = 'received'
    FAILED     = 'failed'

class OrderStatus():
    PROCESSING = 'processing'
    PROCESSED = 'processed'
    FAILED = 'failed'
    CANCELLED = 'cancelled'
    CANCELLING = 'cancelling'
    EXPIRED = 'expired'


class Fiat():
    USD = 'USD'
    CNY = 'CNY'
    JPY = 'JPY'
    EUR = 'EUR'
    GBP = 'GBP'
    HKD = 'HKD'


class FillType():
    DEX = 'dex'
    AMM = 'amm'


class WithdrawalType():
    FORCE = 'force_withdrawal'
    OFFCHAIN = 'offchain_withdrawal'


class OffchainRequestType():
    ORDER                       = '0'
    OFFCHAIN_WITHDRAWAL         = '1'
    UPDATE_ACCOUNT              = '2'
    TRANSFER                    = '3'
    FAST_OFFCHAIN_WITHDRAWAL    = '4'
    OPEN_ACCOUNT                = '5'
    AMM_EXIT                    = '6'
    DEPOSIT                     = '7'
    AMM_JOIN                    = '8'
    TRANSFER_AND_UPDATE_ACCOUNT = '15'

    # NFT-specific Request Types
    NFT_MINT                        = '9'
    NFT_WITHDRAWAL                  = '10'
    NFT_TRANSFER                    = '11'
    NFT_DEPLOY_TOKENADDRESS         = '13'
    NFT_TRANSFER_AND_UPDATE_ACCOUNT = '19'


class NftType():
    EIP1155 = '0'
    EIP712  = '1'


class NftTransferStatus():
    PROCESSING = 'processing'
    PROCESSED  = 'processed'
    FAILED     = 'failed'
    RECEIVED   = 'received'


class NftMintStatus():
    PROCESSING = 'processing'
    PROCESSED  = 'processed'
    FAILED     = 'failed'
    RECEIVED   = 'received'


class NftDepositStatus():
    PROCESSING = 'processing'
    PROCESSED  = 'processed'
    FAILED     = 'failed'
    RECEIVED   = 'received'


class NftWithdrawalStatus():
    PROCESSING = 'processing'
    PROCESSED  = 'processed'
    FAILED     = 'failed'
    RECEIVED   = 'received'


class L2BlockStatus():
    FINALIZED = 'finalized'
    CONFIRMED = 'confirmed'


class SignatureType():
    ECDSA = '0'
    EDDSA = '1'
    APPROVED_HASH = '2'


class Security():
    NONE      = '0'
    API_KEY   = '1'
    EDDSA_URL = '2'
    ECDSA_URL = '3'
    ECDSA_EIP = '4'
    BODY_EDDSA = '5'
    BODY_ECDSA = '6'
    BODY_HASH = '7'

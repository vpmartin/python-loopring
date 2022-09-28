

class BaseClient:
    # API Mainnet/Testnet base URLs
    API_MAINNET = 'https://api3.loopring.io/'
    API_TESTNET_UAT2 = 'https://uat2.loopring.io/'
    API_TESTNET_UAT3 = 'https://uat3.loopring.io/'

    # Candlestick Intervals
    KLINE_INTERVAL_1MINUTE = '1min'
    KLINE_INTERVAL_5MINUTE = '5min'
    KLINE_INTERVAL_15MINUTE = '15min'
    KLINE_INTERVAL_30MINUTE = '30min'
    KLINE_INTERVAL_1HOUR = '1hr'
    KLINE_INTERVAL_2HOUR = '2hr'
    KLINE_INTERVAL_4HOUR = '4hr'
    KLINE_INTERVAL_12HOUR = '12hr'
    KLINE_INTERVAL_1DAY = '1d'
    KLINE_INTERVAL_1WEEK = '1w'

    # Order Types
    ORDER_TYPE_LIMIT = 'LIMIT'
    ORDER_TYPE_TAKER_ONLY = 'TAKER_ONLY'
    ORDER_TYPE_MAKER_ONLY = 'MAKER_ONLY'
    ORDER_TYPE_AMM = 'AMM'

    # Order Channels
    ORDER_CHANNEL_ORDER_BOOK = 'ORDER_BOOK'
    ORDER_CHANNEL_AMM_POOL = 'AMM_POOL'
    ORDER_CHANNEL_MIXED = 'MIXED'

    # Sides
    SIDE_BUY = 'BUY'
    SIDE_SELL = 'SELL'

    # Order Statuses
    STATUS_PROCESSING = 'processing'
    STATUS_PROCESSED = 'processed'
    STATUS_FAILED = 'failed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CANCELLING = 'cancelling'
    STATUS_EXPIRED = 'expired'

    # Fiat Currency Types
    FIAT_USD = 'USD'
    FIAT_CNY = 'CNY'
    FIAT_JPY = 'JPY'
    FIAT_EUR = 'EUR'
    FIAT_GBP = 'GBP'
    FIAT_HKD = 'HKD'

    # Transaction Fill Types
    FILL_TYPE_DEX = 'dex'
    FILL_TYPE_AMM = 'amm'

    # Withdrawal Types
    WITHDRAWAL_TYPE_FORCE = 'force_withdrawal'
    WITHDRAWAL_TYPE_OFFCHAIN = 'offchain_withdrawal'

    # Offchain Request Types
    OFFCHAIN_REQ_ORDER = '0'
    OFFCHAIN_REQ_OFFCHAIN_WITHDRAWAL = '1'
    OFFCHAIN_REQ_UPDATE_ACCOUNT = '2'
    OFFCHAIN_REQ_TRANSFER = '3'
    OFFCHAIN_REQ_FAST_OFFCHAIN_WITHDRAWAL = '4'
    OFFCHAIN_REQ_OPEN_ACCOUNT = '5'
    OFFCHAIN_REQ_AMM_EXIT = '6'
    OFFCHAIN_REQ_DEPOSIT = '7'
    OFFCHAIN_REQ_AMM_JOIN = '8'
    OFFCHAIN_REQ_NFT_MINT = '9'
    OFFCHAIN_REQ_NFT_WITHDRAWAL = '10'
    OFFCHAIN_REQ_NFT_TRANSFER = '11'
    OFFCHAIN_REQ_DEPLOY_TOKENADDRESS = '13'
    OFFCHAIN_REQ_TRANSFER_AND_UPDATE_ACCOUNT = '15'
    OFFCHAIN_REQ_NFT_TRANSFER_AND_UPDATE_ACCOUNT = '19'

    # NFT Types
    NFT_TYPE_EIP1155 = '0'
    NFT_TYPE_EIP712 = '1'

    # NFT Transfer Statuses
    NFT_TRANSFER_STATUS_PROCESSING = 'processing'
    NFT_TRANSFER_STATUS_PROCESSED = 'processed'
    NFT_TRANSFER_STATUS_FAILED = 'failed'
    NFT_TRANSFER_STATUS_RECEIVED = 'received'

    # NFT Mint Statuses
    NFT_MINT_STATUS_PROCESSING = 'processing'
    NFT_MINT_STATUS_PROCESSED = 'processed'
    NFT_MINT_STATUS_FAILED = 'failed'
    NFT_MINT_STATUS_RECEIVED = 'received'

    # NFT Deposit Statuses
    NFT_DEPOSIT_STATUS_PROCESSING = 'processing'
    NFT_DEPOSIT_STATUS_PROCESSED = 'processed'
    NFT_DEPOSIT_STATUS_FAILED = 'failed'
    NFT_DEPOSIT_STATUS_RECEIVED = 'received'

    # NFT Withdrawal Statuses
    NFT_WITHDRAWAL_STATUS_PROCESSING = 'processing'
    NFT_WITHDRAWAL_STATUS_PROCESSED = 'processed'
    NFT_WITHDRAWAL_STATUS_FAILED = 'failed'
    NFT_WITHDRAWAL_STATUS_RECEIVED = 'received'

    L2_BLOCK_STATUS_FINALIZED = 'finalized'
    L2_BLOCK_STATUS_CONFIRMED = 'confirmed'

    def __init__(self):
        print('i am a new client')
        pass

        # EDDSA key stuff


class Client(BaseClient):
    pass


class AsyncClient(BaseClient):
    pass

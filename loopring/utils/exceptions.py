import inspect

class InvalidTradingPairException(Exception):
    def __init__(self, pair):
        msg = f'"{pair}" is not a valid trading pair.'
        super().__init__(msg)


class InvertedTradingPairException(Exception):
    def __init__(self, pair):
        inverted = '-'.join(pair.split('-')[::-1])
        msg = f'"{pair}" is not a valid trading pair. However, "{inverted}"' \
              f' is valid.'
        super().__init__(msg)


class InvalidEnumException(Exception):
    def __init__(self, cls, value):
        attrs = [attr for attr in dir(cls) if not callable(getattr(cls, attr))
                 and not attr.startswith("__")]

        labels = [f'{cls.__name__}.{attr}' for attr in attrs]
        values = [getattr(cls, attr) for attr in attrs]

        msg = f'{value} is not a valid value of {cls}. Please try one of the' \
              f' following: {labels}, or their respective values: {values}.'

        super().__init__(msg)

class MultipleNotAllowedException(Exception):
    def __init__(self, group, value):
        if inspect.isclass(group):
            group = group.__name__

        msg = f'Validation of value {value} in {group} does not allow ' \
              f'multiple values.'

        super().__init__(msg)

class InvalidSymbolException(Exception):
    def __init__(self, symbol, valid_symbols):
        msg = f'"{symbol}" is not a valid symbol. Please try one of the ' \
              f'following: {valid_symbols}.'

        super().__init__(msg)
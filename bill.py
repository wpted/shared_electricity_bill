from typing import Union


class Bill:
    """
    Object that contains data and the lasting period of the bill to share.
    """

    def __init__(self, amount: Union[int, float], period: str):
        self.amount = amount
        self.period = period

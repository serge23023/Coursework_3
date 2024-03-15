from src.currency import Currency


class Amount:
    def __init__(self, amount: str, currency: dict):
        self.amount = amount
        self.currency = Currency(**currency)

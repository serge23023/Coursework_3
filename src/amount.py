from src.currency import Currency


class Amount:
    """
    Класс Amount представляет сумму в определенной валюте.
    Таким образом, каждый объект Amount содержит сумму и объект Currency, представляющий валюту этой суммы.
    """

    def __init__(self, amount: str, currency: dict):
        self.amount = amount
        self.currency = Currency(**currency)

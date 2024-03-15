import re
from datetime import datetime
from src.amount import Amount


class Operation:

    def __init__(self,
                 operation_id: int,
                 state: str,
                 date: str,
                 operation_amount: dict,
                 description: str,
                 to: str,
                 from_account: str = None,
                 ) -> None:
        self.id = operation_id
        self.state = state
        self.date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        self.operation_amount = Amount(**operation_amount)
        self.description = description
        self.to = self.__get_to_or_from(to)
        self.from_ = self.__get_to_or_from(from_account)

    def __repr__(self) -> str:
        return (f"{self.date.strftime("%d.%m.%Y")} {self.description}\n"
                f"{self.from_} -> {self.to}\n"
                f"{self.operation_amount.amount} {self.operation_amount.currency.name}\n")

    @staticmethod
    def __get_to_or_from(item: str | None) -> str | None:
        if item is None:
            return None
        index = re.search(r"\d", item).start()
        match len(item[index:]):
            case 16:
                return (item[:index] + item[index:index + 4] + ' ' + item[index + 4:index + 6]
                        + '** **** ' + item[index + 12:])
            case _:
                return item[:index] + '**' + item[-4:]

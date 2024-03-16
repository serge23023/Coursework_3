# Импорт модулей re, datetime и Amount из src.amount
from datetime import datetime

from src.amount import Amount


class Operation:
    """
    Класс Operation представляет операцию.
    """

    def __init__(self,
                 operation_id: int,
                 state: str,
                 date: str,
                 operation_amount: dict,
                 description: str,
                 to: str,
                 from_account: str = None,
                 ) -> None:
        """
        Инициализация атрибутов класса
        """
        self.id = operation_id
        self.state = state
        self.date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        self.operation_amount = Amount(**operation_amount)
        self.description = description
        self.to = self.__get_to_or_from(to)
        self.from_ = self.__get_to_or_from(from_account)

    def __repr__(self) -> str:
        """
        Представление объекта в виде строки
        """
        if self.from_ is None:
            return (f"{self.date.strftime("%d.%m.%Y")} {self.description}\n"
                    f"{self.to}\n"
                    f"{self.operation_amount.amount} {self.operation_amount.currency.name}\n")
        else:
            return (f"{self.date.strftime("%d.%m.%Y")} {self.description}\n"
                    f"{self.from_} -> {self.to}\n"
                    f"{self.operation_amount.amount} {self.operation_amount.currency.name}\n")

    # Статический метод для обработки атрибутов to и from_
    @staticmethod
    def __get_to_or_from(item: str | None) -> str | None:
        """
        Статический метод для обработки атрибутов to и from_
        """
        if item is None:
            return None
        split_ = item.split()
        match len(split_[-1:][0]):
            case 16:
                return (' '.join(split_[:-1]) + ' ' + split_[-1:][0][:4] + ' ' + split_[-1:][0][4:6]
                        + '** **** ' + item[-4:])
            case _:
                return ' '.join(split_[:-1]) + ' **' + item[-4:]

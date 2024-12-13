# TODO: Подробно описать три произвольных класса
import datetime


# TODO: описать класс
class Dog:
    """
    Класс, описывающий собаку.

    Attributes:
        name (str): Имя собаки.
        breed (str): Порода собаки.
        age (int): Возраст собаки (в годах). Должен быть неотрицательным числом.
    """

    def __init__(self, name: str, breed: str, age: int) -> None:
        """
        Инициализация объекта класса Dog.

        Args:
            name (str): Имя собаки.
            breed (str): Порода собаки.
            age (int): Возраст собаки.

        Raises:
            ValueError: Если возраст меньше 0.
        """
        if age < 0:
            raise ValueError("Возраст собаки не может быть отрицательным.")
        self.name: str = name
        self.breed: str = breed
        self.age: int = age

    def bark(self, times: int = 1) -> None:
        """
        Заставляет собаку лаять.

        Args:
            times (int, optional): Сколько раз собака должна лаять. Значение по умолчанию - 1.

        Raises:
            ValueError: Если количество лаев меньше 1.
        """
        if times < 1:
            raise ValueError("Собака должна лаять хотя бы один раз.")
        print("Гав" * times)

    def get_age_in_dog_years(self) -> int:
        """
        Вычисляет возраст собаки в "собачьих годах". (Упрощенное вычисление)

        Returns:
            int: Возраст собаки в "собачьих годах".

        >>> dog = Dog("Рекс", "Овчарка", 5)
        >>> dog.get_age_in_dog_years()
        35
        """
        return self.age * 7


# TODO: описать ещё класс
class BankAccount:
    """
    Класс, описывающий банковский счёт.

    Attributes:
        owner (str): Имя владельца счёта.
        balance (float): Баланс счёта. Должен быть неотрицательным числом.
    """

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """
        Инициализация объекта класса BankAccount.

        Args:
            owner (str): Имя владельца счёта.
            balance (float, optional): Начальный баланс счёта. Значение по умолчанию - 0.0.

        Raises:
            ValueError: Если начальный баланс меньше 0.

        """
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner: str = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> float:
        """
        Вносит деньги на счёт.

        Args:
            amount (float): Сумма для внесения.

        Returns:
            float: Новый баланс счёта.

        Raises:
            ValueError: Если сумма для внесения меньше или равна 0.

        >>> account = BankAccount("Иван", 100.0)
        >>> account.deposit(50.0)
        150.0
        """
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть больше 0.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снимает деньги со счёта.

        Args:
            amount (float): Сумма для снятия.

        Returns:
            float: Новый баланс счёта.

        Raises:
            ValueError: Если сумма для снятия больше баланса или меньше или равна 0.

        >>> account = BankAccount("Иван", 100.0)
        >>> account.withdraw(50.0)
        50.0
        """
        if amount <= 0 or amount > self.balance:
            raise ValueError("Сумма для снятия должна быть больше 0 и не превышать баланс.")
        self.balance -= amount
        return self.balance


# TODO: и ещё один
class Event:
    """
    Класс, описывающий событие в календаре.

    Attributes:
        title (str): Название события.
        date (datetime.date): Дата события.
        description (str): Описание события.
    """

    def __init__(self, title: str, date: datetime.date, description: str = "") -> None:
        """Инициализация объекта класса Event."""
        self.title: str = title
        self.date: datetime.date = date
        self.description: str = description

    def get_formatted_date(self) -> str:
        """
        Возвращает отформатированную дату события.

        Returns:
            str: Отформатированная дата события (ДД.ММ.ГГГГ).
        >>> event = Event("Встреча", datetime.date(2024, 3, 15))
                >>> event.get_formatted_date()
                '15.03.2024'
                """
        return self.date.strftime("%d.%m.%Y")

    def update_description(self, new_description: str) -> None:
        """
        Обновляет описание события.

        Args:
            new_description (str): Новое описание события. Не может быть None.

        Raises:
            TypeError: Если новое описание не является строкой.
        """
        if not isinstance(new_description, str):
            raise TypeError("Описание должно быть строкой.")
        self.description = new_description

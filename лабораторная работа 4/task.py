# TODO: описать базовый класс
class Animal:
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int, species: str):
        """
        Конструктор класса Animal.

        Args:
            name: Имя животного.
            age: Возраст животного.
            species: Вид животного.
        """
        self._name = name  # Инкапсуляция: доступ только через геттер
        self._age = age  # Инкапсуляция: доступ только через геттер
        self._species = species  # Инкапсуляция: доступ только через геттер

    @property
    def name(self) -> str:
        """Возвращает имя животного."""
        return self._name

    @property
    def age(self) -> int:
        """Возвращает возраст животного."""
        return self._age

    @property
    def species(self) -> str:
        """Возвращает вид животного."""
        return self._species

    def make_sound(self) -> str:
        """
        Издает звук.

        Returns:
            Звук, который издает животное.
        """
        return "Generic animal sound"

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"Animal: {self.name}, Age: {self.age}, Species: {self.species}"

    def __repr__(self) -> str:
        """Возвращает строку для повторного создания объекта."""
        return f"Animal(name='{self.name}', age={self.age}, species='{self.species}')"


# TODO: описать дочерний классclass Dog(Animal):
class Dog(Animal):
    """
    Класс для собак, наследуется от Animal.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        Args:
            name: Имя собаки.
            age: Возраст собаки.
            breed: Порода собаки.
        """
        super().__init__(name, age, species="Dog")  # Использование суперкласса для общих атрибутов
        self._breed = breed  # Инкапсуляция: доступ только через геттер

    @property
    def breed(self) -> str:
        """Возвращает породу собаки."""
        return self._breed

    def make_sound(self) -> str:
        """
        Перегруженный метод make_sound.
        Изменяет звук, издаваемый животным на лай.

        Returns:
            Звук, который издает собака (лай).
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Собака приносит предмет.

        Args:
            item: Предмет, который нужно принести.

        Returns:
            Сообщение о том, что собака принесла предмет.
        """
        return f"Dog {self.name} fetched the {item}."

    def __str__(self) -> str:
        """Возвращает строковое представление собаки."""
        return f"Dog: {self.name}, Age: {self.age}, Breed: {self.breed}"

    def __repr__(self) -> str:
        """Возвращает строку для повторного создания объекта."""
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"


# Пример использования:
animal = Animal("Generic Animal", 5, "Unknown")
dog = Dog("Buddy", 3, "Golden Retriever")

print(animal)
print(animal.make_sound())
print(dog)
print(dog.make_sound())
print(dog.fetch("ball"))
print(repr(animal))
print(repr(dog))

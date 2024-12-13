from task_1 import # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
import datetime
import task_1
if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
     # TODO: вызвать метод с некорректными аргументами(b)
     dog = Dog("Белка", "Такса", 3)
     print("Собака создана успешно:", dog.name)
    except ValueError as e:
        print("Ошибка при создании собаки:", e)

try:
    account = BankAccount("Петров", 1000)
    print("Счет создан успешно:", account.owner)
except ValueError as e:
    print("Ошибка при создании счета:", e)

try:
    event = Event("Концерт", datetime.date(2024, 5, 10), "Билеты куплены")
    print("Событие создано успешно:", event.title)
except Exception as e:
    print("Ошибка при создании события:", e)

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
     dog.bark(0)  # Некорректное значение times
     except ValueError as e:
     print("Ошибка при вызове bark():", e)

    try:
        account.deposit(-100)  # Некорректное значение amount
    except ValueError as e:
        print("Ошибка при вызове deposit():", e)

    try:
        account.withdraw(2000)  # Некорректное значение amount (слишком большая сумма)
    except ValueError as e:
        print("Ошибка при вызове withdraw():", e)

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
     event.update_description(123)  # Некорректный тип new_description
     except TypeError as e:
     print("Ошибка при вызове update_description():", e)

    try:
        dog = Dog("Рекс", "Овчарка", -2)  # проверка на отрицательный возраст
    except ValueError as e:
        print("Ошибка при создании собаки:", e)

    try:
        account = BankAccount("Сидоров", -500)  # проверка на отрицательный баланс
    except ValueError as e:
        print("Ошибка при создании счета:", e)

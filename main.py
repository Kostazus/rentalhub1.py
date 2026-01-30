from storage import Storage
from managers.user_manager import UserManadger
from managers.item_manager import ItemManadger
from managers.rental_manager import RentalManager
from exceptions import (
    ItemNotFoundError,
    UserNotFoundError,
    ItemNotAvailableError
)

user_storage = Storage("data/users.json")
item_storage = Storage("data/items.json")
rental_storage = Storage("data/rentals.json")

user_manadger = UserManadger(user_storage)
item_manadger = ItemManadger(item_storage)
rental_manadger = RentalManager(
    rental_storage,
    user_manadger,
    item_manadger
)

while True:
    print("""
1 — создать пользователя
2 — создать предмет
3 — взять предмет в аренду
4 — показать все предметы
5 — показать всех пользователей
0 — выход
""")

    try:
        choice = int(input("Введите номер действия: "))
    except ValueError:
        print("Введите число от 0 до 5!")
        continue

    if choice == 1:
        user_id = input("Введите id пользователя: ")
        name = input("Введите имя пользователя: ")
        user_manadger.create_user(user_id, name)
        print("Пользователь создан!")

    elif choice == 2:
        item_id = input("Введите id предмета: ")
        name = input("Введите название предмета: ")
        item_manadger.add_item(item_id, name)
        print("Предмет добавлен!")

    elif choice == 3:
        user_id = input("Введите id пользователя: ")
        item_id = input("Введите id предмета: ")

        try:
            days = int(input("Введите количество дней: "))
        except ValueError:
            print("Количество дней должно быть числом")
            continue

        try:
            rental_id = f"{user_id}_{item_id}"
            rental_manadger.rent_item(
                rental_id,
                user_id,
                item_id,
                days
            )
            print("Вы арендовали вещь!")

        except (UserNotFoundError, ItemNotFoundError, ItemNotAvailableError) as e:
            print(e)

    elif choice == 4:
        items = item_manadger.show_items()
        if not items:
            print("Предметов нет!")
        else:
            for item in items:
                print(item)

    elif choice == 5:
        users = user_manadger.show_users()
        if not users:
            print("Пользователей нет!")
        else:
            for user in users:
                print(user)

    elif choice == 0:
        print("Выход из программы")
        break

    else:
        print("Неверный пункт меню")

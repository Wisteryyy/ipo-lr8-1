import json 

def file():
    with open("dump.json", "r", encoding="utf-8") as file:
        return json.load(file)

def menu():
    print("-----------------Меню-----------------")
    print("-------1. Вывести все записи----------")
    print("-------2. Вывести запись по ID----------")
    print("-------3. Добавить запись----------")
    print("-------4. Удалить запись по ID----------")
    print("-------5. Выйти из программы----------")

def correct_input(prompt):
    while True:
        try:
            option = int(input(prompt))
            if option <= 0 or option > 5:
                print("Введите корректный номер.")
            else:
                return option
        except ValueError:
            print("Введите число.")

def first(data):
    print("Все записи:")
    for entry in data:
        print(f"Код: {entry['id']}")
        print(f"Имя рыбы: {entry['name']}")
        print(f"Латинское имя рыбы: {entry['latin_name']}")
        print(f"Является ли соленоводной: {entry['is_salt_water_fish']}")
        print(f"Количество подвидов: {entry['sub_type_count']}")

def second(data):
    while True:
        search_id = int(input("Введите ID записи для поиска: ")) # запрашиваем ID для поиска
        found = False # флаг для отслеживания, была ли найдена запись
        for entry in data: # перебираем все записи
            if entry["id"] == search_id: # если запись по id равна введенному id
                print(f"Код: {entry['id']}")
                print(f"Имя рыбы: {entry['name']}")
                print(f"Латинское имя рыбы: {entry['latin_name']}")
                print(f"Является ли соленоводной: {entry['is_salt_water_fish']}")
                print(f"Количество подвидов: {entry['sub_type_count']}")
                found = True # запись найдена
                break # прерываем цикл
        if found:
            break # выходим из цикла, если запись найдена
        print("Запись не найдена. Попробуйте еще раз.") # выводим, если запись не найдена

def third(data):
    while True:
        id_add = int(input("Введите ID: ")) # вводим ID
        exist = False
        for entry in data: # проверяем, существует ли ID
            if entry["id"] == id_add:
                exist = True
                print("Такое id уже существует. Попробуйте что-то другое.")
                break
        if not exist:
            break
    name_add = input("Введите общее название рыбы: ") # вводим название
    latin_name = input("Введите латинское название рыбы: ") # вводим латинское название
    is_salt_water_fish = input("Является ли рыба соленоводной? ") # вводим тип рыбы
    sub_type_count = int(input("Введите количество подвидов: ")) # вводим количество подвидов

    new_record = { # создаём словарь для новой записи
        "id": id_add,
        "name": name_add,
        "latin_name": latin_name,
        "is_salt_water_fish": is_salt_water_fish,
        "sub_type_count": sub_type_count
    }
    data.append(new_record) # добавляем новую запись в список

    with open("dump.json", 'w', encoding='utf-8') as file: # открываем файл для записи
        json.dump(data, file) # записываем данные
    return 1

def fourth(data):
    while True:
        delete_id = int(input("Введите ID для удаления: ")) # запрашиваем ID для удаления

        for index, entry in enumerate(data): # используем enumerate для получения индекса
            if entry["id"] == delete_id: # если запись найдена
                del data[index] # удаляем запись
                print("Запись удалена.")
                break
        else:
            print("Запись не найдена. Попробуйте еще раз.")
            continue # запрашиваем ID снова
        break # выходим из цикла, если запись удалена

def main():
    data = file()
    operation_count = 0

    while True:
        menu()
        option = correct_input("Введите номер пункта: ")

        if option == 1:
            first(data)
            operation_count += 1
            
        elif option == 2:
            second(data)
            operation_count += 1
            
        elif option == 3:
            operation_count += third(data)
            
        elif option == 4:
            fourth(data)
            operation_count += 1
            
        elif option == 5:
            print(f"Количество выполненных операций с записями: {operation_count}")
            break
main()

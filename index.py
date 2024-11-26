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
    search_id = int(input("Введите ID записи для поиска: "))
    found = False
    for entry in data:
        if entry["id"] == search_id:
            print(f"Код: {entry['id']}")
            print(f"Имя рыбы: {entry['name']}")
            print(f"Латинское имя рыбы: {entry['latin_name']}")
            print(f"Является ли соленоводной: {entry['is_salt_water_fish']}")
            print(f"Количество подвидов: {entry['sub_type_count']}")
            found = True
            break
    if not found:
        print("Запись не найдена.")

def third(data):
    new_record = {
        "id": int(input("Введите ID: ")),
        "name": input("Введите общее название рыбы: "),
        "latin_name": input("Введите латинское название рыбы: "),
        "is_salt_water_fish": input("Является ли рыба соленоводной? "),
        "sub_type_count": int(input("Введите количество подвидов: "))
    }
    data.append(new_record)
    with open("dump.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return 1

def fourth(data):
    delete_id = int(input("Введите ID для удаления: "))
    found = False
    for index, entry in enumerate(data):
        if entry["id"] == delete_id:
            del data[index]
            found = True
            break
    if not found:
        print("Запись не найдена.")

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

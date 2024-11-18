import json

def failik():
    with open("dump.json", "r", encoding="utf-8") as file:
        return json.load(file)

def menu():
    print("-----------------Меню-----------------")
    print("-------1. Вывести все записи----------")
    print("-------2. Вывести запись по полю----------")
    print("-------3. Добавить запись----------")
    print("-------4. Удалить запись по полю----------")
    print("-------5. Выйти из программы----------")

def first(data):
    print("Все записи:")
    for d in data:
        print(json.dumps(d))

def second(data):
    idd = int(input("Введите id записи для поиска: "))
    find = False
    for d in data:
        if d["id"] == idd:
            print(json.dumps(d, indent=4))
            find = True
            break
    if not find:
        print("Запись не найдена.")

def third(data):
    new = {
        "id": int(input("Введите id: ")),
        "name": input("Введите общее название рыбы: "),
        "latin_name": input("Введите латинское название рыбы: "),
        "is_salt_water_fish": str(input("Является ли рыба соленоводной (yes/no)? ")),
        "sub_type_count": int(input("Введите количество подвидов: "))
    }
    data.append(new)
    with open("dump.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    return 1

def fourth(data):
    iddd = int(input("Введите id: "))
    find = False
    for index, d in enumerate(data):
        if d["id"] == iddd:
            del data[index]
            find = True
            break
    if not find:
        print("Запись не найдена.")

def main():
    s = failik()
    C = 0

    while True:
        menu()
        a = int(input("Введите номер пункта: "))

        if a <= 0 or a > 5:
            print("Введите корректный номер.")
            continue

        elif a == 1:
            first(s)
            C += len(s)

        elif a == 2:
            second(s)
        
        elif a == 3:
            C += third(s)

        elif a == 4:
            fourth(s)

        elif a == 5:
            print(f"Количество выполненных операций с записями: {C}")
            break

if __name__ == "__main__":
    main()
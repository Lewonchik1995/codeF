import sqlite3


# Функция для создания таблицы объявлений в базе данных
def create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS ads
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT,
                 description TEXT,
                 price REAL,
                 phone_number TEXT)''')

    conn.commit()
    conn.close()


# Функция для просмотра всех объявлений
def view_ads():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ads")
    ads = c.fetchall()

    for ad in ads:
        print(ad)

    conn.close()


# Функция для добавления объявления
def add_ad(title, description, price, phone_number):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO ads (title, description, price, phone_number) VALUES (?, ?, ?, ?)",
              (title, description, price, phone_number))

    conn.commit()
    conn.close()


# Функция для изменения цены объявления
def update_price(title, new_price):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("UPDATE ads SET price = ? WHERE title = ?", (new_price, title))

    conn.commit()
    conn.close()


# Функция для удаления объявления
def delete_ad(title):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("DELETE FROM ads WHERE title = ?", (title,))

    conn.commit()
    conn.close()


# Функция для поиска объявления по названию
def find_ad(title):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ads WHERE title = ?", (title,))
    ad = c.fetchone()

    if ad:
        print(ad)
    else:
        print("Объявление не найдено")

    conn.close()


# Основной цикл программы
create_table()
while True:
    print("1 - Просмотреть все объявления")
    print("2 - Добавить объявление")
    print("3 - Изменить цену")
    print("4 - Удалить объявление")
    print("5 - Найти объявление по названию")
    print("0 - Выход из программы")

    choice = input("Введите номер команды: ")

    if choice == "1":
        view_ads()
    elif choice == "2":
        title = input("Введите название объявления: ")
        description = input("Введите описание объявления: ")
        price = float(input("Введите цену объявления: "))
        phone_number = input("Введите номер телефона: ")

        add_ad(title, description, price, phone_number)
    elif choice == "3":
        title = input("Введите название объявления: ")
        new_price = float(input("Введите новую цену объявления: "))

        update_price(title, new_price)
    elif choice == "4":
        title = input("Введите название объявления: ")

        delete_ad(title)
    elif choice == "5":
        title = input("Введите название объявления: ")

        find_ad(title)
    elif choice == "0":
        break
    else:
        print("Неверная команда")

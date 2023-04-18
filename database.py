import sqlite3


# Создать/подключиться к базе данных
connection = sqlite3.connect('dostavka.db')
# Создаем переводчика
sql = connection.cursor()


# Запрос на создание таблицы
#sql.execute('CREATE TABLE users (id INTEGER, name TEXT, phone_number TEXT, loc_lat REAL, loc_long REAL, gender TEXT);')

# Зарпос на создание таблицы для продуктов
# sql.execute('CREATE TABLE products (pr_name TEXT, pr_des TEXT, pr_price REAL, pr_picture TEXT);')


# Добавление пользователя
def add_user(user_id, name, phone_number, latitude, longitude, gender):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    # Добавление пользователя в базу
    sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?);', (user_id, name, phone_number, latitude, longitude, gender))

    # Фиксируем обновления
    connection.commit()


# Получение пользователя
def get_users():
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    # Зпрос для получения данных из базе
    users = sql.execute('SELECT name, id, gender FROM users;')

    # Вывод всего в виде списка с кортежами
    return users.fetchall()


# Запрос для удаления из базы
def delete_user():
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    # Отправляем запрос на удаление
    sql.execute('DELETE FROM users;')

    # Зафиксировать обновления
    connection.commit()


# Функция для добавления продуктов
def add_product(pr_name, pr_des, pr_price, pr_picture):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    sql.execute('INSERT INTO products VALUES (?,?,?,?);', (pr_name, pr_des, pr_price, pr_picture))

    # Зафиксировать обновления
    connection.commit()


# Функция для получения всех данных о продукте
def get_all_info_product(current_product):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    all_products = sql.execute('SELECT * FROM products WHERE pr_name=?;', (current_product, ))

    return all_products.fetchone()


# Функция для получения наименований продукта
def get_name_product():
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    products_name = sql.execute('SELECT pr_name FROM products;')

    return products_name.fetchall()


# Функция для проверки пользователя на наличие в базе
def check_user(user_id):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    checker = sql.execute('SELECT id FROM users WHERE id=?;', (user_id,))

    # Проверка есть ли данные из запроса
    if checker.fetchone():
        return True

    else:
        return False

## Дз ##
# Создать таблицу корзины
# Колонки: user_id, product_name, product_count
# sql.execute('CREATE TABLE cart (user_id INTEGER, product_name TEXT, product_count INTEGER);')


# Создать функцию добавления user_id, product_name, product_count в корзину
def add_product_to_cart(user_id, product_name, product_count):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    sql.execute('INSERT INTO cart VALUES (?,?,?);', (user_id, product_name, product_count))

    # Зафиксировать
    connection.commit()


# Создать функцию получения корзины (WHERE user_id=?)
def get_user_cart(user_id):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    all_products_from_cart = sql.execute('SELECT * FROM cart WHERE user_id=?;', (user_id,))

    return all_products_from_cart.fetchall()


# Создать функцию удаления корзины (WHERE user_id=?)
def delete_from_cart(user_id):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    sql.execute('DELETE FROM cart WHERE user_id=?;', (user_id,))

    # Зафиксировать
    connection.commit()


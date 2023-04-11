from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопка для отправки номера телефона
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Поделиться контактом', request_contact=True)

    kb.add(button)

    return kb


# Кнопка для отправки локации
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Поделиться локацией', request_location=True)

    kb.add(button)

    return kb


# Кнопка для выбора пола
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Мужчина')
    button2 = KeyboardButton('Женщина')

    kb.add(button, button2)

    return kb


# Кнопки для выбора количества
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    buttons = [KeyboardButton(str(i)) for i in range(1, 10)]
    back = KeyboardButton('Назад')

    kb.add(*buttons, back)

    return kb


# Кнопки для корзины
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Очистить')
    button2 = KeyboardButton('Оформить заказ')
    button3 = KeyboardButton('Редактировать')
    button4 = KeyboardButton('Назад')

    kb.add(button, button2, button3, button4)

    return kb


# Кнопки при выборе способа оплаты
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Наличные')
    button2 = KeyboardButton('Картой')
    button3 = KeyboardButton('Назад')

    kb.add(button, button2, button3)

    return kb


# Кнопки для подтверждения заказа
def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Подтвердить')
    button2 = KeyboardButton('Отменить')
    button3 = KeyboardButton('Назад')

    kb.add(button, button2, button3)

    return kb


# Кнопки с названиями товаров
def products_kb():
    pass










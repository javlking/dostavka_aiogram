from aiogram import Dispatcher, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from states import Registration, GetProduct
import buttons
import database


bot = Bot('5871305426:AAEoSBdVM7_OfSL3Ea33AiYeq8lGp26O0f4')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):

    # Получить user_id пользователя
    user_id = message.from_user.id
    # Происходит проверка в базе
    checker = database.check_user(user_id)

    if checker: # Если пользователь есть в базе то отправим главное меню
        await message.answer('Выбери продукт', reply_markup=buttons.products_kb())

    else:
        await message.answer('Привет, я бот для доставки\nОтправь имя для регистрации')

        # Переход на этап получения имени
        await Registration.getting_name_state.set()


# Этап получения имени
@dp.message_handler(state=Registration.getting_name_state)
async def get_name(message, state=Registration.getting_name_state):
    # Получаем отправленное имя
    user_answer = message.text

    # Временно сохраняем
    await state.update_data(name=user_answer)

    await message.answer('Имя сохранил\nОтправь номер телефона', reply_markup=buttons.phone_number_kb())

    # Переход на этап получения номера
    await Registration.getting_phone_number.set()


# Этап получения номера телефона
@dp.message_handler(state=Registration.getting_phone_number, content_types=['contact'])
async def get_number(message, state=Registration.getting_phone_number):
    # Получаем отправленный контакт
    user_answer = message.contact.phone_number

    # Временно сохраняем
    await state.update_data(number=user_answer)

    await message.answer('Номер сохранил\nОтправь локацию', reply_markup=buttons.location_kb())

    # Переход на этап получения локации
    await Registration.getting_location.set()


# Этап получения локации
@dp.message_handler(state=Registration.getting_location, content_types=['location'])
async def get_location(message, state=Registration.getting_location):
    # Получаем отправленную локацию
    user_answer = message.location.latitude
    user_answer_2 = message.location.longitude

    # Временно сохраняем
    await state.update_data(latitude=user_answer, longitude=user_answer_2)

    await message.answer('Локацию сохранил\nОтправь пол', reply_markup=buttons.gender_kb())

    # Переход на этап получения пола
    await Registration.getting_gender.set()


# Этап получения пола
@dp.message_handler(state=Registration.getting_gender)
async def get_gender(message, state=Registration.getting_gender):
    # Получаем пол
    user_answer = message.text

    await message.answer('Успешно зарегистрирован', reply_markup=buttons.gender_kb())

    # Сохраняем пользователя в базу
    all_info = await state.get_data()
    name = all_info.get('name')
    phone_number = all_info.get('number')
    latitude = all_info.get('latitude')
    longitude = all_info.get('longitude')
    gender = user_answer
    user_id = message.from_user.id

    database.add_user(user_id, name, phone_number, latitude, longitude, gender)
    print(database.get_users())

    # Остановка
    await state.finish()


# Независимый обработчик текста для основного меню
@dp.message_handler(content_types=['text'])
async def text_messages(message):
    user_answer = message.text

    # Актуальный список продуктов
    actual_products = [i[0] for i in database.get_name_product()]

    # Проверка на какую кнопку нажал пользователь
    if user_answer == 'Корзина':
        await message.answer('Ваша корзина')

    elif user_answer == 'Оформить заказ':
        await message.answer('Оформляем заказ')

    # А если отправленное сообщение - это продукт
    elif user_answer in actual_products:
        await message.answer('Выберите количество', reply_markup=buttons.product_count())

        # Сохранить ввод пользователя без state
        await dp.current_state(user=message.from_user.id).update_data(user_product=message.text)

        # Перекинуть на этап получения количества продукта
        await GetProduct.getting_pr_count.set()

    else:
        await message.answer('Выберите продукт из списка', reply_markup=buttons.products_kb())


# Обработчик для получения количества продукта
@dp.message_handler(state=GetProduct.getting_pr_count)
async def get_pr_count(message, state=GetProduct.getting_pr_count):
    product_count = message.text

    await message.answer('Продукт добавлен\nМожет что-то еще?', reply_markup=buttons.products_kb())
    await state.finish()




executor.start_polling(dp)

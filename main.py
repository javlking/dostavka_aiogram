from aiogram import Dispatcher, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from states import Registration
import buttons


bot = Bot('Token')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):

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
async def get_location(message, state=Registration.getting_gender):
    # Получаем пол
    user_answer = message.text

    await message.answer('Успешно зарегистрирован', reply_markup=buttons.gender_kb())

    # Остановка
    await state.finish()


executor.start_polling(dp)

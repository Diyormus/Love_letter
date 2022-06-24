from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
import sqlite3, random
from dotenv import load_dotenv
from keyboards import *

load_dotenv()

bot = Bot(token='5468733836:AAG6ZPxmzX6Kux1Req27bFhWvOKjcv4YuF0')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command_start(message: Message):
    await message.answer(f'''Этого бота я сделал специально для тебя Алина 🤖
Если ты будешь чувствовать не хватку внимания ну или просто захочешь прочитать что нибудь хорошее о себе просто нажми на кнопку получить☺️
Уверен что хоть чуть чуть, но это тебе поможет 👍''')
    await get_message(message)


async def get_message(message: Message):
    text = 'Нажми на кнопку 👇👇👇'
    await message.answer(text, reply_markup=generate_keyboard())


@dp.message_handler(content_types='text')
async def get_letter(message: Message):
    database = sqlite3.connect('compliment.db')
    cursor = database.cursor()
    cursor.execute('''
        SELECT compliment_description FROM compliment;
        ''')
    letter = cursor.fetchall()
    random_index = random.randint(1, 1000)
    random_index_compliment = letter[random_index][0]
    await bot.send_message(chat_id=message.chat.id,
                           text=random_index_compliment)


executor.start_polling(dp)

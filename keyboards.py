from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def generate_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text='Получить ✉️')]
        ], resize_keyboard=True)

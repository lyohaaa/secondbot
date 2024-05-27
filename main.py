from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Отправь фото кота')
button2 = KeyboardButton('Перейти на следующую клавиатуру')
keyboard.add(button1, button2)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.reply('Привет, я эхо-бот', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat_id)

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Ты нажал кнопку 2')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
import logging

from aiogram import Bot, Dispatcher, executor, types

from googletrans import Translator


API_TOKEN = '5860732372:AAH46N36t3TaKWCK1vV4_lIyEyWlD2-pKTI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum! Botimizdan foydalanish\nyo'riqnomasi bilan tanishib chiqish uchun uchun /help buyrug'ini yuboring!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # await message.answer("Ushbu bot uz-en en-uz yoki uz-ru, ru-uz shakldagi tarjima qilib bera oladi!\nuz-en - /uzen buyrug'ini yuboring\nen-uz - /enuz buyrug'ini yuboring\nuz-ru - /uzru - buyrug'ini yuboring\nru-uz - /ruuz buyrug'ini yuboring")
    await message.answer("Ushbu bot uzbek-english o'zbek tilidagi matnlarni ingliz tiliga tarjima qilib bera oladi!")

# # uzbek-english translator
#
# @dp.message_handler(commands=['uzen'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#
#     await message.answer("O'zbekcha matn yuboring")
#
#
# @dp.message_handler()
# async def send_welcome(message: types.Message):
#
#     tarjimon = Translator()
#     matn = message.text
#
#     try:
#        tarjima = tarjimon.translate(matn, src="uz", dest="en")
#
#        await message.answer(tarjima.text)
#
#     except:
#         await message.answer("Tarjima jarayonida xatolik yuz berdi")
#
#
#
#  # english-uzbek translator
#
#
# @dp.message_handler(commands=['enuz'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.answer("Send English text!")
#
#
# @dp.message_handler()
# async def send_welcome(message: types.Message):
#     tarjimon = Translator()
#     matn = message.text
#
#     try:
#         tarjima = tarjimon.translate(matn, src="en", dest="uz")
#         await message.answer(tarjima.text)
#
#     except:
#         await message.answer("Tarjima jarayonida xatolik yuz berdi")
#
#
#  # uzbek-rus translator
#
#
# @dp.message_handler(commands=['uzru'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.answer("O'zbekcha matn yuboring")
#
#
# @dp.message_handler()
# async def send_welcome(message: types.Message):
#     tarjimon = Translator()
#     matn = message.text
#
#     try:
#         tarjima = tarjimon.translate(matn, src="uz", dest="ru")
#         await message.answer(tarjima.text)
#
#     except:
#         await message.answer("Tarjima jarayonida xatolik yuz berdi")
#
#
#  # rus-uzbek translator
#
#
# @dp.message_handler(commands=['ruuz'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#
#     await message.answer("Отправить текст на русском языке!")
#
#
# @dp.message_handler()
# async def send_welcome(message: types.Message):
#
#
#     tarjimon = Translator()
#     matn = message.text
#
#     try:
#
#         tarjima = tarjimon.translate(matn, src="ru", dest="uz")
#
#         await message.answer(tarjima.text)
#
#     except:
#         await message.answer("Tarjima jarayonida xatolik yuz berdi")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    # await message.answer("Faqat uzbek-english, english-uzbek, uzbek-rus, rus-uzbek shu yo'nalishlarda tarjima qilinadi!")
    tarjimon = Translator()


    matn = message.text

    try:
       tarjima = tarjimon.translate(matn, src="uz", dest="en")

       await message.answer(tarjima.text)
    except:

       await message.answer("Tarjima jarayonida xatolik yuz berdi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

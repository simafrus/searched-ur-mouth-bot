import logging
# import hashlib
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery
import search_queries
import utils
import os


def bot_(API_TOKEN):
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.answer(
            "Привет\n"
            "Я еще в разработке, но уже умею составлять поисковые запросы в инлайн режиме. Попробуй написать "
            "@searched_ur_mouth_bot")

    @dp.message_handler()
    async def echo(message: types.Message):
        mess = message.answer(message.text)
        print(f"{message.from_user.username} сказал:\n {message.text} \n\n")
        await mess

    @dp.inline_handler()
    async def inline_process(inline_query: InlineQuery):
        text = inline_query.query
        results = []

        if text:
            await bot.answer_inline_query(inline_query.id, results=search_queries.create_results_list(text), cache_time=1)

    executor.start_polling(dp, skip_updates=True)

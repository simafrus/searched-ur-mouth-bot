import logging
# import hashlib
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
import utils


def bot_(API_TOKEN):
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply(
            "Привет\n"
            "Я еще в разработке, но уже умею составлять поисковые запросы в инлайн режиме. Попробуй написать "
            "@searched_ur_mouth_bot")

    @dp.message_handler()
    async def echo(message: types.Message):
        mess = message.answer(message.text)
        await mess
        print(message)

    @dp.inline_handler()
    async def inline_echo(inline_query: InlineQuery):
        text = inline_query.query

        input_content = InputTextMessageContent(utils.google(text))
        result_id: str = "0"
        google = InlineQueryResultArticle(
            id=result_id,
            title=f'Google {text!r}',
            input_message_content=input_content,
        )

        input_content = InputTextMessageContent(utils.yandex(text))
        result_id: str = "1"
        yandex = InlineQueryResultArticle(
            id=result_id,
            title=f'Yandex {text!r}',
            input_message_content=input_content,
        )

        await bot.answer_inline_query(inline_query.id, results=[google, yandex], cache_time=1)

    executor.start_polling(dp, skip_updates=True)

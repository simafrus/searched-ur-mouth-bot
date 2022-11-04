from aiogram.types import InlineQueryResultArticle, InputTextMessageContent


class SearchSystem(object):
    def __init__(self, name, result_id, link, logo_link=None):
        self.name = name
        self.link = link
        self.buff_link = link
        self.result_id = result_id
        self.logo_link = logo_link

    # создание ссылки
    def create_link(self, query):
        self.buff_link += query.replace(" ", "+")
        res = InputTextMessageContent(self.buff_link)
        return res

    # создание инлайн ответа
    def create_inline_answer(self, text):
        answer: object = InlineQueryResultArticle(
            id=self.result_id,
            title=f'{self.name} {text!r}',
            input_message_content=self.create_link(text),
            thumb_url=self.logo_link
        )
        self.buff_link = self.link
        return answer


google = SearchSystem("Google",
                      "0",
                      "https://www.google.com/search?q=",
                      "https://dobralama.com.ua/catalog/view/theme/tt_oregon1/img/ico_google.png")

yandex = SearchSystem("Yandex",
                      "1",
                      "https://yandex.ru/search/?text=",
                      "https://xn-----6kcabbjccw0bpo1amardxdsph4h0k.xn--p1ai/img/22842117.png")

duckduckgo = SearchSystem("DuckDuckGo",
                          "2",
                          "https://duckduckgo.com/?t=ffab&q=",
                          "https://www.tadviser.ru/images/e/eb/DuckDuckGo_logo.png")

stackowerflow = SearchSystem("StackOverflow",
                             "3",
                             "https://stackoverflow.com/search?q=",
                             "https://png2.cleanpng.com/sh/09e5e7394bc6802ad430499ade840f3a/L0KzQYm3V8E5N5lBR91yc4Pzfri0kCRia5wyhAhucnbvf8i0gB9ueKZ5feQ2aXPyfsS0kCRia5wyfepsaHHxd7a0jP9od15qe9H3b33sc7LzTcVjPJdmUNU6MUDmcoO9TsE0OWc4SqU5MUW2QYq7V8IxOWE7UKo3cH7q/kisspng-stack-overflow-computer-icons-stack-exchange-logo-economical-5b4fa8c110cb26.1316323015319472010688.png")


async def create_results_list(text):
    # google = google.create_inline_answer(text)
    # yandex = yandex.create_inline_answer(text)
    # duckduckgo = duckduckgo.create_inline_answer(text)
    # stackowerflow = stackowerflow.create_inline_answer(text)
    return [google.create_inline_answer(text),
            yandex.create_inline_answer(text),
            duckduckgo.create_inline_answer(text),
            stackowerflow.create_inline_answer(text)]

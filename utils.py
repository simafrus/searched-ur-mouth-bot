def google(text):
    link = "https://www.google.com/search?q="
    link += text.replace(" ", "+")

    return link


def yandex(text):
    link = "https://yandex.ru/search/?text="
    link += text.replace(" ", "+")

    return link

def duckduckgo(text):
    link = "https://yandex.ru/search/?text="
    link += text.replace(" ", "+")

    return link


def test(text):
    print(text)

    return text

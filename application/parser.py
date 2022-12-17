from requests_html import HTMLSession


def get_netology_h1(timeout=8) -> str | None:
    """
    Парсит сайт netology.ru и возвращает значение тега h1.
    Если timeout превышен, то ничего не вернет.
    :param timeout: задает время ожидания в секундах. (По умолчанию 8)
    :return: str или None (если превышено время timeout)
    """
    with HTMLSession() as session:
        try:
            netology = session.get('https://netology.ru')
            netology.html.render(timeout=timeout)
            title = netology.html.find('h1', first=True).text
            return title
        except Exception as ex:
            if type(ex).__name__ == 'TimeoutError':
                print('Превышен timeout, установите значение выше')
            else:
                print(ex)

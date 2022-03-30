from requests import get
from bs4 import BeautifulSoup


def extract_estadao_data() -> list:
    r = get('https://www.estadao.com.br/')
    soup = BeautifulSoup(r.text, features='html.parser')

    articles = soup.find_all('article')
    extracted_data = [parse_estadao_article(article) for article in articles]

    return extracted_data


def parse_estadao_article(article) -> tuple | None:
    if not article.h3 or not article.h3.a:
        return None

    title = article.h3.text.strip()
    url = article.h3.a.get('href')
    topic = article.h2.text.strip()
    photo = article.figure.a.img.get('data-src-desktop')

    return (url, title, topic, photo)

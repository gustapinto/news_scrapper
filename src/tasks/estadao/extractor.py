from requests import get
from bs4 import BeautifulSoup

from src.interfaces.webcrawler import Webcrawler


class EstadaoWebcrawler(Webcrawler):
    @property
    def url(self) -> str:
        return 'https://www.estadao.com.br/'

    def extract_data(self) -> list:
        r = get(self.url)
        soup = BeautifulSoup(r.text, features='html.parser')

        articles = soup.find_all('article')
        extracted_data = [self.__parse_article(article)
                          for article in articles if article]

        return extracted_data

    def __parse_article(self, article) -> tuple | None:
        if not article.h3 or not article.h3.a:
            return None

        title = article.h3.text.strip()
        url = article.h3.a.get('href')
        hat = article.h2.text.strip()
        photo = article.figure.a.img.get('data-src-desktop')

        author, topic = self.__get_intern_article_data(url)

        return ('estadao', topic, hat, title, url, photo, author)

    def __get_intern_article_data(self, url: str) -> tuple:
        r = get(url)
        soup = BeautifulSoup(r.text, features='html.parser')

        infodiv = soup.find('div', class_='n--noticia__state-title')
        headerdiv = soup.find('article', class_='n--noticia__header')

        author = None
        if infodiv:
            inforow = infodiv.text.split(',')
            author = inforow[0].strip()

        topic = None
        if headerdiv:
            topics = headerdiv.find_all('li', class_='breadcrumb-item')
            topic = topics[-1].text.strip() if topics else None

        return (author, topic)

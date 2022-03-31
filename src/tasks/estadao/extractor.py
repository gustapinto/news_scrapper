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
        extracted_data = [self.__parse_article(article) for article in articles]

        return extracted_data

    def __parse_article(self, article) -> tuple | None:
        if not article.h3 or not article.h3.a:
            return None

        title = article.h3.text.strip()
        url = article.h3.a.get('href')
        topic = article.h2.text.strip()
        photo = article.figure.a.img.get('data-src-desktop')

        '''
        TODO

        OBS: Essa obtenção de dados só funciona em alguns subsites do
        portal estadão, é preciso encapsular ela em uma função com uma
        strategy que obtém dados de diferentes maneiras a partir da
        url do portal
        '''
        r = get(url)
        soup = BeautifulSoup(r.text, features='html.parser')

        infodiv = soup.find('div', class_='n--noticia__state-title')

        author = infodiv.text.split(',')[0].strip() if infodiv else ''
        date = infodiv.text.split(',')[1].strip if infodiv else ''

        return (url, title, topic, photo, author, date)

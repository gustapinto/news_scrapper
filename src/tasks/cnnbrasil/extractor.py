from urllib.parse import unquote, urlparse

from requests import get
from bs4 import BeautifulSoup

from src.utils import flatten
from src.interfaces.webcrawler import Webcrawler


class CnnBrasilWebcrawler(Webcrawler):
    @property
    def url(self) -> str:
        return 'https://www.cnnbrasil.com.br/'

    def extract_data(self) -> list[dict]:
        html = get(self.url)
        soup = BeautifulSoup(html.text, features='html.parser')

        sections = soup.select('section[class*="home__grid--1-3 block--coringa block__type--block"]')

        lis = lambda section: section.ul.find_all('li')

        articles = flatten([lis(section) for section in sections])
        extracted_data = [self.__parse_article(article)
                          for article in articles if article]

        return extracted_data

    def __parse_article(self, article) -> dict:
        url = article.a.get('href')
        topic = self.__get_topic_from_url(url)
        photo = article.a.img.get('src') if article.a.img else None
        title = article.a.text.strip()
        hat = article.a.span.text.capitalize() if article.a.span else None

        author, author_url = self.__get_intern_article_data(url)

        return {
            'author': author,
            'author_url': author_url,
            'hat': hat,
            'newspaper': 'cnn',
            'photo': photo,
            'title': title,
            'topic': topic,
            'url': url,
        }

    def __get_topic_from_url(self, url: str) -> str:
        url_path = unquote(urlparse(url).path)
        url_path_parts = [p for p in url_path.split('/') if p]
        topic = url_path_parts[0]

        return topic

    def __get_intern_article_data(self, url: str) -> tuple:
        html = get(url)
        soup = BeautifulSoup(html.text, features='html.parser')

        author_group = soup.find('span', class_='author__group')

        if not author_group or not author_group.a:
            return (None, None)

        author = author_group.a.text
        author_url = author_group.a.get('href')

        return (author, author_url)

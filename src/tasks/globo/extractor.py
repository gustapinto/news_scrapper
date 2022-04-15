from urllib.parse import unquote, urlparse

from requests import get
from bs4 import BeautifulSoup

from src.interfaces.webcrawler import Webcrawler


class GloboWebcrawler(Webcrawler):
    @property
    def url(self) -> str:
        return 'https://g1.globo.com/'

    def extract_data(self) -> list[dict]:
        html = get(self.url)
        soup = BeautifulSoup(html.text, features='html.parser')

        articles = soup.find_all('div', class_='bastian-feed-item')
        extracted_data = [self.__parse_article(article)
                          for article in articles if article]

        return extracted_data

    def __parse_article(self, article) -> dict:
        hat = article.span.text
        title = article.a.text
        url = article.a.get('href')
        topic = self.__get_topic_from_url(url)
        photo = article.img.get('src') if article.img else None

        return {
            'hat': hat,
            'newspaper': 'globo',
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

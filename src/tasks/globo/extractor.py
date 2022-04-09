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
        topic = url.split(self.url)[1].split('/')[0]
        photo = article.img.get('src') if article.img else None

        return {
            'hat': hat,
            'newspaper': 'globo',
            'photo': photo,
            'title': title,
            'topic': topic,
            'url': url,
        }

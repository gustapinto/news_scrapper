from requests import get
from bs4 import BeautifulSoup

from src.utils import flatten
from src.interfaces.webcrawler import Webcrawler


class CnnBrasilWebcrawler(Webcrawler):
    @property
    def url(self) -> str:
        return 'https://www.cnnbrasil.com.br/'

    def extract_data(self) -> list:
        html = get(self.url)
        soup = BeautifulSoup(html.text, features='html.parser')

        sections = soup.select('section[class*="home__grid--1-3 block--coringa block__type--block"]')

        lis = lambda section: section.ul.find_all('li')

        articles = flatten([lis(section) for section in sections])

        return articles

from dagster import op

from src.interfaces.loader import DatabaseLoader
from src.interfaces.parser import Parser
from src.interfaces.webcrawler import Webcrawler


@op
def extract(extractor: Webcrawler) -> list[dict]:
    return extractor.extract_data()

@op
def parse(parser: Parser, data: list[dict]) -> list[dict]:
    return parser.parse_data(data)

@op
def load(loader: DatabaseLoader, data: list[dict]) -> None:
    return loader.load('news', data)

from dagster import op, job

from src.database.loaders.mongo import MongoLoader
from src.tasks.globo.extractor import GloboWebcrawler
from src.tasks.globo.parser import GloboParser


@job
def globo_job():
    @op
    def extract_globo() -> list[dict]:
        return GloboWebcrawler().extract_data()

    @op
    def parse_globo(data: list[dict]) -> list[dict]:
        return GloboParser().parse_data(data)

    @op
    def load_globo(data: list[dict]) -> None:
        MongoLoader().load('news', data)

    load_globo(parse_globo(extract_globo()))

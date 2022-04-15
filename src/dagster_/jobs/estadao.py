from dagster import op, job

from src.database.loaders.mongo import MongoClient
from src.tasks.estadao.extractor import EstadaoWebcrawler
from src.tasks.estadao.parser import EstadaoParser


@job
def estadao_job():
    @op
    def extract_estadao() -> list[dict]:
        return EstadaoWebcrawler().extract_data()

    @op
    def parse_estadao(data: list[dict]) -> list[dict]:
        return EstadaoParser().parse_data(data)

    @op
    def load_estadao(data: list[dict]) -> None:
        MongoClient().load('news', data)

    load_estadao(parse_estadao(extract_estadao()))

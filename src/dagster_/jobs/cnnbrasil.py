from dagster import op, job

from src.database.loaders.mongo import MongoLoader
from src.tasks.cnnbrasil.extractor import CnnBrasilWebcrawler
from src.tasks.cnnbrasil.parser import CnnBrasilParser


@job
def cnnbrasil_job():
    @op
    def extract_cnnbrasil() -> list[dict]:
        return CnnBrasilWebcrawler().extract_data()

    @op
    def parse_cnnbrasil(data: list[dict]) -> list[dict]:
        return CnnBrasilParser().parse_data(data)

    @op
    def load_cnnbrasil(data: list[dict]) -> None:
        MongoLoader().load('news', data)

    load_cnnbrasil(parse_cnnbrasil(extract_cnnbrasil()))

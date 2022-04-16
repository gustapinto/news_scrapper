from dagster import op, job, ScheduleDefinition

from src.database.loaders.mongo import MongoLoader
from src.tasks.estadao.extractor import EstadaoWebcrawler
from src.tasks.estadao.parser import EstadaoParser


@job
def estadao_job():
    @op
    def extract_estadao() -> list:
        return EstadaoWebcrawler().extract_data()

    @op
    def parse_estadao(data: list) -> list[dict]:
        return EstadaoParser().parse_data(data)

    @op
    def load_estadao(data: list[dict]) -> None:
        MongoLoader().load('news', data)

    load_estadao(parse_estadao(extract_estadao()))


estadao_job_schedule = ScheduleDefinition(job=estadao_job,
                                          cron_schedule='0 */6 * * *')

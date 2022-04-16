from dagster import repository

from src.dagster_.jobs.cnnbrasil import cnnbrasil_job_schedule
from src.dagster_.jobs.estadao import estadao_job_schedule
from src.dagster_.jobs.globo import globo_job_schedule


@repository
def news_repository():
    return [cnnbrasil_job_schedule, estadao_job_schedule,
            globo_job_schedule]

from dagster import repository

from src.dagster_.jobs.cnnbrasil import cnnbrasil_job
from src.dagster_.jobs.estadao import estadao_job
from src.dagster_.jobs.globo import globo_job


@repository
def news_repository():
    return [cnnbrasil_job, estadao_job, globo_job]

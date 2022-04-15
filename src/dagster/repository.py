from dagster import repository

from .jobs import estadao_job, globo_job, cnnbrasil_job


@repository
def news_repository():
    return [estadao_job, globo_job, cnnbrasil_job]

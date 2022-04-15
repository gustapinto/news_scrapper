from src.tasks.cnnbrasil.extractor import CnnBrasilWebcrawler
from src.tasks.cnnbrasil.parser import CnnBrasilParser
from src.tasks.estadao.extractor import EstadaoWebcrawler
from src.tasks.estadao.parser import EstadaoParser
from src.tasks.globo.extractor import GloboWebcrawler
from src.tasks.globo.parser import GloboParser
from .operations import extract, parse, load

from dagster import job


@job
def estadao_job():
    load(parse(EstadaoParser(), extract(EstadaoWebcrawler())))


@job
def globo_job():
    load(parse(GloboParser(), extract(GloboWebcrawler())))


@job
def cnnbrasil_job():
    load(parse(CnnBrasilParser(), extract(CnnBrasilWebcrawler())))

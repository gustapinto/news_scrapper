from src.interfaces.parser import Parser
from src.utils import remove_none_entries


class CnnBrasilParser(Parser):
    def parse_data(self, raw_data: list[dict]) -> list[dict]:
        return [remove_none_entries(d) for d in raw_data]

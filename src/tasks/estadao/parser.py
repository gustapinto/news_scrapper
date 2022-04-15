from src.interfaces.parser import Parser
from src.utils import remove_none_entries


class EstadaoParser(Parser):
    def parse_data(self, raw_data: list[dict]) -> list[dict]:
        cleared_list = remove_none_entries(raw_data)

        return [remove_none_entries(d) for d in cleared_list]

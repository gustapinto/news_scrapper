from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse_data(self, data: list) -> list:
        pass

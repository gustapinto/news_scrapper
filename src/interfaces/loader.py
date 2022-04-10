from abc import ABC, abstractmethod


class DatabaseLoader(ABC):
    @abstractmethod
    def connect(self, *args, **kwargs):
        pass

    @abstractmethod
    def load(self, data: list[dict]):
        pass

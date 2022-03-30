from abc import ABC, abstractmethod


class Webcrawler(ABC):
    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def extract_data(self, *args, **kwargs) -> list:
        pass

from abc import ABC, abstractmethod

class BaseReport(ABC):
    def __init__(self):
        self.result = {}

    @abstractmethod
    def generate(self, employees: list[dict]):
        pass

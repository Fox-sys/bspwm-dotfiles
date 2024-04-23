from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def info(self, message):
        raise NotImplementedError

    @abstractmethod
    def warning(self, message):
        raise NotImplementedError

    @abstractmethod
    def error(self, message):
        raise NotImplementedError

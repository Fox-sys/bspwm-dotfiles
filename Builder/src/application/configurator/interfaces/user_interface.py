from abc import ABC, abstractmethod


class IUserInterface(ABC):
    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError

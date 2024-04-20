from abc import abstractmethod
from src.application.configurator.interfaces.system_manipulators import IPackageInstaller
import os


class BaseInstaller(IPackageInstaller):
    @property
    @abstractmethod
    def packages(self) -> list[str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def install_command(self) -> str:
        raise NotImplementedError

    def install_packages(self) -> None:
        for package in self.packages:
            print(f'{self.install_command} {package}')

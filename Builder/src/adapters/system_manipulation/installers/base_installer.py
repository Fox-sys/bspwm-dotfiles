from abc import abstractmethod
from src.application.configurator.interfaces.system_manipulators import IPackageInstaller
import os


class BaseInstaller(IPackageInstaller):
    @property
    @abstractmethod
    def _packages(self) -> list[str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def _install_command(self) -> str:
        raise NotImplementedError

    def install_packages(self) -> None:
        for package in self._packages:
            print(f'{self._install_command} {package}')

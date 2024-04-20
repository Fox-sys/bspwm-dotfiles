from abc import ABC, abstractmethod


class IPackageInstaller(ABC):
    @abstractmethod
    def install_packages(self, package_list) -> None:
        ...


class IDriverInstaller(ABC):
    @abstractmethod
    def install_packages(self, packages):
        ...

    @abstractmethod
    def post_installing(self):
        ...

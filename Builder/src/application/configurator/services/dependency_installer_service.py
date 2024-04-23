from attr import frozen
from src.application.configurator.interfaces.system_manipulators import IPackageInstaller
from src.application.configurator.interfaces.logger import ILogger


@frozen
class DependencyInstallerService:
    pacman_installer: IPackageInstaller
    aur_installer: IPackageInstaller
    logger: ILogger

    def install_dependencies(self):
        self.logger.info('Setup pacman dependencies')
        self.pacman_installer.install_packages()
        self.logger.info('Setup Aur dependencies')
        self.aur_installer.install_packages()

from attr import frozen
from src.application.configurator.interfaces.system_manipulators import IPackageInstaller
from src.application.configurator.interfaces.logger import ILogger
from src.application.configurator import etc


@frozen
class DependencyInstallerService:
    pacman_installer: IPackageInstaller
    aur_installer: IPackageInstaller
    logger: ILogger

    def install_dependencies(self):
        self.logger.info('Setup pacman dependencies')
        self.pacman_installer.install_packages(etc.PACMAN_DEPENDENCIES)
        self.logger.info('Setup Aur dependencies')
        self.aur_installer.install_packages(etc.AUR_DEPENDENCIES)

from attr import frozen
from src.application.configurator.interfaces.system_manipulators import IDriverInstaller
from src.application.configurator.interfaces.logger import ILogger


@frozen
class DriverInstallService:
    driver_installer: IDriverInstaller
    logger: ILogger

    def install_drivers(self):
        self.logger.info(f'Устанавливаются драйвера {self.driver_installer.type}')
        self.driver_installer.install_packages()
        self.driver_installer.post_installing()

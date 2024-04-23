from attr import frozen
from src.application.configurator.interfaces.system_manipulators import IPostInstallConfigurator

from src.application.configurator.interfaces.logger import ILogger


@frozen
class PostInstallConfigurationService:
    logger: ILogger
    post_install_configurator: IPostInstallConfigurator

    def post_configuration(self):
        self.logger.info('Enabling services')
        self.post_install_configurator.enable_services()
        self.logger.info('Applying patches')
        self.post_install_configurator.apply_patches()

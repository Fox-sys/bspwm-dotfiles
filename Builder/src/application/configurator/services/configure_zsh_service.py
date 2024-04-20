from attr import frozen

from src.application.configurator.interfaces.logger import ILogger
from src.application.configurator.interfaces.system_manipulators import IZshConfigurator


@frozen
class ConfigureZshService:
    zsh_configurator: IZshConfigurator
    logger: ILogger

    def configure_oh_my_zsh_theme(self):
        self.logger.info('Setting up oh my zsh theme')
        self.zsh_configurator.configure_oh_my_zsh_theme()

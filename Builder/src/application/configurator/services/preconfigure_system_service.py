from attr import frozen

from src.application.configurator.interfaces.logger import ILogger

from src.application.configurator.interfaces.system_manipulators import IPreconfigurator


@frozen
class PreconfigureSystemService:
    preconfigurator: IPreconfigurator
    logger: ILogger

    def preconfigure(self):
        self.logger.info('Preconfiguring system')
        self.logger.info('Update arch db')
        self.preconfigurator.update_arch_db()
        self.logger.info('Enabling aur')
        self.preconfigurator.enable_aur()
        self.logger.info('Creating folders in home dir')
        self.preconfigurator.fill_home_dir()

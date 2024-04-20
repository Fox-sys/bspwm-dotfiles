from attr import frozen

from src.application.configurator.interfaces.logger import ILogger
from src.application.configurator.interfaces.system_manipulators import IComponentInstaller


@frozen
class ComponentInstallerService:
    component_installer: IComponentInstaller
    logger: ILogger

    def install_components(self):
        self.logger.info('Fill home directory')
        self.component_installer.fill_home_dir()
        self.logger.info('Scripts and binaries are installing')
        self.component_installer.install_binaries()
        self.logger.info('Themes are installing')
        self.component_installer.install_themes()
        self.logger.info('Fonts are installing')
        self.component_installer.install_fonts()
        self.logger.info('Configs are installing')
        self.component_installer.move_configs()
        self.logger.info('Images are installing')
        self.component_installer.move_images()
        self.logger.info('Others components are installing')
        self.component_installer.move_others()
        self.logger.info('SUCCESS')

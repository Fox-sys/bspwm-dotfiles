from src.application.configurator import services
from src.adapters.system_manipulation.preconfigure_system import Preconfigurator
from src.adapters.logger.logger import Logger
from src.adapters.system_manipulation.installers import PacmanInstaller, AurInstaller


def create_preconfigure_service() -> services.PreconfigureSystemService:
    return services.PreconfigureSystemService(preconfigurator=Preconfigurator(), logger=Logger())


def create_dependency_installer_service() -> services.DependencyInstallerService:
    return services.DependencyInstallerService(
        pacman_installer=PacmanInstaller(), aur_installer=AurInstaller(), logger=Logger()
    )

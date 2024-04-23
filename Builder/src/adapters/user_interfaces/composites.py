from typing import Type

from src.adapters.system_manipulation.component_installer import ComponentInstaller
from src.adapters.system_manipulation.installers.driver_installers.amd_free_driver_installer import \
    AMDFreeDriverInstaller
from src.adapters.system_manipulation.post_install_configurator import PostInstallConfigurator
from src.adapters.system_manipulation.zsh_configurator import ZshConfigurator
from src.application.configurator import services
from src.adapters.system_manipulation.preconfigure_system import Preconfigurator
from src.adapters.logger.logger import Logger
from src.adapters.system_manipulation.installers import PacmanInstaller, AurInstaller
from src.application.configurator.enums import DriverTypeEnum
from src.application.configurator.interfaces.system_manipulators import IDriverInstaller


def create_preconfigure_service() -> services.PreconfigureSystemService:
    return services.PreconfigureSystemService(preconfigurator=Preconfigurator(), logger=Logger())


def create_dependency_installer_service() -> services.DependencyInstallerService:
    return services.DependencyInstallerService(
        pacman_installer=PacmanInstaller(), aur_installer=AurInstaller(), logger=Logger()
    )


def create_driver_install_service(driver_type) -> services.DriverInstallService | None:
    driver_installer: Type[IDriverInstaller]
    match driver_type:
        case DriverTypeEnum.AMD_GPU_FREE:
            driver_installer = AMDFreeDriverInstaller
        case DriverTypeEnum.AMD_GPU_PRO:
            Logger().warning('Not implemented')
            return
        case DriverTypeEnum.NVIDIA_NVCX_AND_NVDX:
            Logger().warning('Not implemented')
            return
        case DriverTypeEnum.NVIDIA_MAXWELL_DKMS:
            Logger().warning('Not implemented')
            return
        case DriverTypeEnum.NVIDIA_MAXWELL:
            Logger().warning('Not implemented')
            return
        case DriverTypeEnum.NVIDIA_KEPLER:
            Logger().warning('Not implemented')
            return
        case DriverTypeEnum.NVIDIA_TESLA:
            Logger().warning('Not implemented')
            return
        case _:
            return

    return services.DriverInstallService(
        driver_installer=driver_installer(), logger=Logger()
    )


def create_component_installer_service() -> services.ComponentInstallerService:
    return services.ComponentInstallerService(
        logger=Logger(), component_installer=ComponentInstaller()
    )


def create_configure_zsh_service() -> services.ConfigureZshService:
    return services.ConfigureZshService(
        logger=Logger(), zsh_configurator=ZshConfigurator()
    )


def create_post_install_configuration_service() -> services.PostInstallConfigurationService:
    return services.PostInstallConfigurationService(
        logger=Logger(), post_install_configurator=PostInstallConfigurator()
    )

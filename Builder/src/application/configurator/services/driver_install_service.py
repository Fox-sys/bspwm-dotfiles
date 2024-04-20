from attr import frozen
from src.application.configurator.interfaces.system_manipulators import IDriverInstaller
from src.application.configurator.interfaces.logger import ILogger
from src.application.configurator import etc
from src.application.configurator.enums import DriverTypeEnum


@frozen
class DriverInstallService:
    driver_installer: IDriverInstaller
    logger: ILogger

    def install_drivers(self, driver_type: DriverTypeEnum):
        installing_packages = []
        match driver_type:
            case DriverTypeEnum.AMD_GPU_FREE:
                ...
            case DriverTypeEnum.AMD_GPU_PRO:
                ...
            case DriverTypeEnum.NVIDIA_KEPLER:
                ...
            case DriverTypeEnum.NVIDIA_MAXWELL:
                ...
            case DriverTypeEnum.NVIDIA_TESLA:
                ...
            case DriverTypeEnum.NVIDIA_MAXWELL_DKMS:
                ...
            case DriverTypeEnum.NVIDIA_NVCX_AND_NVDX:
                ...

        self.logger.info(f'Устанавливаются драйвера {driver_type}')
        self.driver_installer.install_packages(installing_packages)
        self.driver_installer.post_installing()

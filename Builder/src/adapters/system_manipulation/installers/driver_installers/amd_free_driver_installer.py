from src.adapters.system_manipulation import packages
from src.adapters.system_manipulation.installers.driver_installers.base_driver_installer import BaseDriverInstaller
from src.application.configurator.enums import DriverTypeEnum


class AMDFreeDriverInstaller(BaseDriverInstaller):
    @property
    def type(self) -> DriverTypeEnum:
        return DriverTypeEnum.AMD_GPU_FREE

    def _install_command(self) -> str:
        return 'sudo pacman -S'

    @property
    def _packages(self) -> list[str]:
        return packages.DRIVER_PACKAGES[self.type]

    def post_installing(self):
        ...

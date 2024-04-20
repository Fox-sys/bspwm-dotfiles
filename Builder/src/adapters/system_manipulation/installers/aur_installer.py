from src.adapters.system_manipulation.installers.base_installer import BaseInstaller
from src.adapters.system_manipulation.packages import AUR_DEPENDENCIES


class AurInstaller(BaseInstaller):
    @property
    def packages(self):
        return AUR_DEPENDENCIES

    @property
    def install_command(self) -> str:
        return 'yay -S'

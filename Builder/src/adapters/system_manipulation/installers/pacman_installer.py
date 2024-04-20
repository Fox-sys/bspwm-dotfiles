from src.adapters.system_manipulation.installers.base_installer import BaseInstaller
from src.adapters.system_manipulation.packages import PACMAN_DEPENDENCIES


class PacmanInstaller(BaseInstaller):
    @property
    def packages(self):
        return PACMAN_DEPENDENCIES

    @property
    def install_command(self) -> str:
        return 'sudo pacman -S'

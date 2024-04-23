from src.adapters.system_manipulation.installers.base_installer import BaseInstaller
from src.adapters.system_manipulation.packages import PACMAN_DEPENDENCIES


class PacmanInstaller(BaseInstaller):
    @property
    def _packages(self) -> list[str]:
        return PACMAN_DEPENDENCIES

    @property
    def _install_command(self) -> str:
        return 'sudo pacman -S --noconfirm'

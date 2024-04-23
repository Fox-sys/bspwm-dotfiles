import os

from src.adapters.system_manipulation.installers.base_installer import BaseInstaller
from src.adapters.system_manipulation.packages import AUR_DEPENDENCIES


class AurInstaller(BaseInstaller):
    @property
    def _packages(self) -> list[str]:
        return AUR_DEPENDENCIES

    @property
    def _install_command(self) -> str:
        return 'yay -S --noconfirm'

    def install_packages(self) -> None:
        os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
        os.system("cd /tmp/yay && makepkg -si")
        super().install_packages()

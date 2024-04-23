import os
from abc import abstractmethod, ABC

from src.adapters.system_manipulation.installers.base_installer import BaseInstaller
from src.application.configurator.interfaces.system_manipulators import IDriverInstaller


class BaseDriverInstaller(BaseInstaller, IDriverInstaller, ABC):
    def _prepare_multilib(self):
        os.system(r"sudo sed -i 's/^#\[multilib\]/[multilib]/' /etc/pacman.conf")
        os.system(
            r"sudo sed -i '/^\[multilib\]$/,/^\[/ s/^#\(Include = \/etc\/pacman\.d\/mirrorlist\)/\1/' /etc/pacman.conf")

    def _install_multilib(self):
        os.system("sudo pacman -Sl multilib")
        os.system("sudo pacman -Sy")

    def install_packages(self) -> None:
        self._prepare_multilib()
        self._install_multilib()
        super().install_packages()

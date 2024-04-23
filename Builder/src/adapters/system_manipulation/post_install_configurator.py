import os

from src.application.configurator.interfaces.system_manipulators import IPostInstallConfigurator


class PostInstallConfigurator(IPostInstallConfigurator):
    def enable_services(self):
        os.system("sudo systemctl enable NetworkManager")
        os.system("sudo systemctl enable bluetooth.service")
        os.system("sudo systemctl start bluetooth.service")

    def apply_patches(self):
        os.system("sudo ln -sf /usr/bin/alacritty /usr/bin/xterm")
        os.system("sudo chmod -R 700 ~/.config/*")

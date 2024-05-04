import os

from src.application.configurator.interfaces.system_manipulators import IPreconfigurator


class Preconfigurator(IPreconfigurator):
    def update_arch_db(self):
        os.system('sudo pacman -Suy')

    def enable_aur(self):
        os.system("git -C /tmp clone https://aur.archlinux.org/aura-bin.git")
        os.system("cd /tmp/aura-bin && makepkg -si")

    def fill_home_dir(self):
        os.system('mkdir ~/Downloads')
        os.system('mkdir ~/Desktop')
        os.system('mkdir ~/Documents')
        os.system('mkdir ~/Images')
        os.system('mkdir ~/Music')
        os.system('mkdir ~/Videos')

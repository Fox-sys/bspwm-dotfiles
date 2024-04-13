import os
import packages

from logger import Logger, LoggerStatus
from creators.software import AurBuilder, ZshBuilder
from creators.drivers import GraphicDrivers
from creators.patches import PatchSystemBugs
from creators.daemons import Daemons


# TODO: Implement error handling for package installation

class SystemConfiguration:
    def start(**kwargs):
        start_text = f"[+] Starting assembly. Options {kwargs}"
        Logger.add_record(start_text, status=LoggerStatus.SUCCESS)
        if kwargs['dotfiles']: SystemConfiguration._install_dotfiles()
        if kwargs['arch_db_update']: SystemConfiguration._update_arch_db()
        if kwargs['bspwn_deps']: SystemConfiguration._install_bspwn_deps()
        if kwargs['dev_deps']: SystemConfiguration._install_dev_deps()
        if kwargs['amd_gpu']: GraphicDrivers.build()
        if kwargs['default_zsh']: SystemConfiguration._default_zsh()
        if kwargs['configure_zsh']: ZshBuilder.build()
        # TODO: The process should not be repeated when reassembling,
        #  important components should only be updated with new ones
        Daemons.enable_all_daemons()
        PatchSystemBugs.enable_all_patches()

    @staticmethod
    def _install_dotfiles():
        SystemConfiguration.__create_default_folders()
        SystemConfiguration.__copy_bspwm_dotfiles()

    @staticmethod
    def _update_arch_db():
        Logger.add_record("[+] Updates Enabled", status=LoggerStatus.SUCCESS)
        os.system("sudo pacman -Sy")

    @staticmethod
    def _install_bspwn_deps():
        Logger.add_record("[+] Installed BSPWM Dependencies", status=LoggerStatus.SUCCESS)
        AurBuilder.build()
        SystemConfiguration.__install_pacman_package(packages.BASE_PACKAGES)
        SystemConfiguration.__install_aur_package(packages.AUR_PACKAGES)

    @staticmethod
    def _install_dev_deps():
        Logger.add_record("[+] Installed Dev Dependencies", status=LoggerStatus.SUCCESS)
        SystemConfiguration.__install_pacman_package(packages.DEV_PACKAGES)
        SystemConfiguration.__install_pacman_package(packages.GNOME_OFFICIAL_TOOLS)

    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_pacman_package(package_names: list):
        for package in package_names:
            os.system(f"sudo pacman -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)

    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_aur_package(package_names: list):
        for package in package_names:
            os.system(f"yay -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)

    @staticmethod
    def __create_default_folders():
        Logger.add_record("[+] Create default directories", status=LoggerStatus.SUCCESS)
        default_folders = "~/Videos ~/Documents ~/Downloads " + \
                          "~/Music ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")
        os.system("cp -r Images/ ~/")
        os.system("mkdir ~/.fonts")

    @staticmethod
    def __copy_bspwm_dotfiles():
        Logger.add_record("[+] Copy Dotfiles & GTK", status=LoggerStatus.SUCCESS)
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")
        os.system("cp -r fonts/* ~/.fonts")

    @staticmethod
    def _default_zsh():
        with open('~/.config/alacritty/alacritty.toml', 'r') as file:
            alacritty_conf = file.read()
        with open('~/.config/alacritty/alacritty.toml', 'w') as file:
            file.write(alacritty_conf.replace('/usr/bin/bash', '/usr/bin/zsh'))

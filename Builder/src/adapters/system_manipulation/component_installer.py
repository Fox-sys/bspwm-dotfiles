import os

from src.application.configurator.interfaces.system_manipulators import IComponentInstaller


class ComponentInstaller(IComponentInstaller):
    def fill_home_dir(self):
        os.system('mkdir ~/Videos')
        os.system('mkdir ~/Desktop')
        os.system('mkdir ~/Downloads')
        os.system('mkdir ~/Documents')
        os.system('mkdir ~/Images')
        os.system('mkdir ~/Music')
        os.system('mkdir ~/.fonts')
        os.system("mkdir -p ~/.config")

    def move_configs(self):
        os.system("cp -r config/* ~/.config/")

    def move_others(self):
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp xinitrc ~/.xinitrc")

    def install_binaries(self):
        os.system("cp -r bin/ ~/.local/")

    def move_fonts(self):
        os.system("cp -r fonts/* ~/.fonts")

    def install_themes(self):
        os.system("cp -r themes ~/.themes")

    def move_images(self):
        os.system("cp -r Images/* ~/Images")

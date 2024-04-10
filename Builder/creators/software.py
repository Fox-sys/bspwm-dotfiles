import os
from logger import Logger, LoggerStatus


class AurBuilder:
    @staticmethod
    def build():
        os.system("git -C /tmp clone https://aur.archlinux.org/yay.git")
        os.system("cd /tmp/yay && makepkg -si")


class ZshBuilder:
    @staticmethod
    def build():
        os.system("fc-cache -f -s")
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
        os.system(
            'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
        os.system(
            'git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
        os.system('cp .zshrc ~/.zshrc')
        os.system('fc-cache -f -v')

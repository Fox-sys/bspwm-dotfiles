import os

from src.application.configurator.interfaces.system_manipulators import IZshConfigurator


class ZshConfigurator(IZshConfigurator):
    def configure_oh_my_zsh_theme(self):
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
        os.system(
            'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
        os.system(
            'git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
        os.system('cp .zshrc ~/.zshrc')
        os.system('fc-cache -f -v')

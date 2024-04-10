import os
from creators.builder import SystemConfiguration


class UserInterface:
    @staticmethod
    def start():
        UserInterface.welcome_banner()
        install_params = UserInterface.get_params()
        SystemConfiguration.start(**install_params)

    @staticmethod
    def welcome_banner():
        os.system("sh Builder/assets/startup.sh")

    @staticmethod
    def is_verify_response(text) -> bool:
        if "y" in text.lower():
            return True
        else:
            return False

    @staticmethod
    def get_params():
        options = {}
        print(f"{len(options) + 1}) Install all dotfiles? [y/N]: ", end="")
        options["dotfiles"] = UserInterface.is_verify_response(input())

        print(f"{len(options) + 1}) Update Arch DataBase? [y/N] ", end="")
        options["arch_db_update"] = UserInterface.is_verify_response(input())

        print(f"{len(options) + 1}) Install BSPWM Dependencies? [y/N] ", end="")
        options["bspwn_deps"] = UserInterface.is_verify_response(input())

        print(f"{len(options) + 1}) Install Dev Dependencies? [y/N] ", end="")
        options["dev_deps"] = UserInterface.is_verify_response(input())

        print(f"{len(options) + 1}) Install AMD GPU Drivers? [y/N] ", end="")
        options["amd_gpu"] = UserInterface.is_verify_response(input())

        print(f"{len(options) + 1}) Configure zsh theme? [y/N]", end="")
        options["configure_zsh"] = UserInterface.is_verify_response(input())

        return options

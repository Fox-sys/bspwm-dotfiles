from src.application.configurator.interfaces.logger import ILogger
from src.application.configurator.enums import LoggerStatusEnum
from datetime import datetime
from os import path


class Logger(ILogger):
    def info(self, message):
        self._prepare_message(message, LoggerStatusEnum.INFO)

    def warning(self, message):
        self._prepare_message(message, LoggerStatusEnum.WARNING)

    def error(self, message):
        self._prepare_message(message, LoggerStatusEnum.ERROR)

    def _prepare_message(self, message, status: LoggerStatusEnum):
        text = f'[{status.value}]: {message} - {datetime.now().strftime("%H:%M:%S")}\n'
        self._print_message(text)
        self._save_to_file(text)

    def _print_message(self, message):
        print(message)

    def _save_to_file(self, message):
        with open(path.expanduser('~') + '/bspwm_install_logs.log', 'a') as file:
            file.write(message)

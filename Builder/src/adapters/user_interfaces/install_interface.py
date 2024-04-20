from src.adapters.user_interfaces.base_interface import BaseInterface


class InstallInterface(BaseInterface):
    def start(self) -> None:
        params = self._get_params()

    @property
    def _params(self) -> list[dict]:
        return [
            {'name': 'base_dependencies', 'question': 'Do you want to install base dependencies?'}
        ]

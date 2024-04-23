from src.adapters.user_interfaces.base_interface import BaseInterface
from src.application.configurator.enums import DriverTypeEnum


class DriverInstallInterface(BaseInterface):
    @property
    def _dicted_enum(self) -> dict:
        return {i: enum_key for i, enum_key in enumerate(DriverTypeEnum)}

    @property
    def _params(self) -> list[dict]:
        return [
            {'name': 'driver_type',
             'question': '\tВыберете драйвер для установки ' + ' | '
             .join([f'{i + 1} = {enum_key.value}' for i, enum_key in self._dicted_enum.items()])}]

    def start(self) -> dict:
        return self._get_params()

    def _verify_response(self, response: str) -> DriverTypeEnum | None:
        try:
            response = int(response)
        except ValueError:
            return
        if response in range(1, len(DriverTypeEnum) + 1):
            return self._dicted_enum[response - 1]

    @property
    def _input_format_string(self) -> str:
        return '{question}: '

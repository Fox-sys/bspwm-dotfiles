from abc import ABC, abstractmethod

from src.application.configurator.interfaces.user_interface import IUserInterface


class BaseInterface(IUserInterface, ABC):
    def _verify_response(self, response: str) -> bool:
        return response.lower() in ['y', 'yes']

    @property
    @abstractmethod
    def _params(self) -> list[dict]:
        raise NotImplementedError

    def _get_params(self) -> dict:
        results = {}
        for i, param in enumerate(self._params):
            results[param['name']] = self._verify_response(input(f"[{i + 1}] {param['question']} [y/N]: "))
        return results

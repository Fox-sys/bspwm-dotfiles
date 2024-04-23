from abc import ABC, abstractmethod

from src.application.configurator.interfaces.user_interface import IUserInterface


class BaseInterface(IUserInterface, ABC):
    def _verify_response(self, response: str) -> bool:
        return response.lower() in ['y', 'yes']

    @property
    @abstractmethod
    def _params(self) -> list[dict]:
        raise NotImplementedError

    @property
    def _input_format_string(self) -> str:
        return "[{question_number}] {question} [y/N]: "

    def _get_params(self) -> dict:
        results = {}
        for i, param in enumerate(self._params):
            results[param['name']] = self._verify_response(input(self._input_format_string.format(
                question_number=i + 1, question=param['question'])))
        return results

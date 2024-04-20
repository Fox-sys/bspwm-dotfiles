from src.adapters.user_interfaces.base_interface import BaseInterface
from src.adapters.user_interfaces import composites


class InstallInterface(BaseInterface):
    def start(self) -> None:
        params = self._get_params()
        self._configure_system(**params)

    @property
    def _params(self) -> list[dict]:
        return [
            {'name': 'install_dependencies', 'question': 'Do you want to install base dependencies?'}
        ]

    def _configure_system(self, install_dependencies: bool):
        self._preconfigure_system()
        if install_dependencies:
            self._install_dependencies()

    def _preconfigure_system(self):
        preconfiguration_service = composites.create_preconfigure_service()
        preconfiguration_service.preconfigure()

    def _install_dependencies(self):
        dependency_installer_service = composites.create_dependency_installer_service()
        dependency_installer_service.install_dependencies()

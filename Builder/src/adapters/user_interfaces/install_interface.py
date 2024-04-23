from src.adapters.user_interfaces.base_interface import BaseInterface
from src.adapters.user_interfaces import composites
from .driver_install_interface import DriverInstallInterface
from ..logger.logger import Logger


class InstallInterface(BaseInterface):
    def start(self) -> dict:
        params = self._get_params()
        self._configure_system(**params)
        return params

    @property
    def _params(self) -> list[dict]:
        return [
            {'name': 'install_dependencies', 'question': 'Do you want to install base dependencies?'},
            {'name': 'install_drivers', 'question': 'Do you want to install graphics driver?'},
            {'name': 'install_components', 'question': 'Do you want to install components?'},
            {'name': 'zsh_configure', 'question': 'Do you want to install powerlevel10k theme for zsh?'
                                                  '(when you see zsh, quit it and installation will continue)'},
        ]

    def _configure_system(self, install_dependencies: bool, install_drivers: bool, install_components: bool,
                          zsh_configure: bool):
        self._preconfigure_system()
        if install_dependencies:
            self._install_dependencies()
        if install_drivers:
            self._install_drivers()
        if install_components:
            self._install_components()
        if zsh_configure:
            self._configure_zsh()
        self._post_install_configuration()

    def _preconfigure_system(self):
        preconfiguration_service = composites.create_preconfigure_service()
        preconfiguration_service.preconfigure()

    def _install_dependencies(self):
        dependency_installer_service = composites.create_dependency_installer_service()
        dependency_installer_service.install_dependencies()

    def _install_drivers(self):
        failures = 0
        install_driver_interface = DriverInstallInterface()
        while not (driver_type := install_driver_interface.start()['driver_type']) and failures < 3:
            failures += 1
        if failures == 3:
            Logger().error('Too much tries. Quiting...')
        driver_installer_service = composites.create_driver_install_service(driver_type)
        if driver_installer_service:
            driver_installer_service.install_drivers()

    def _install_components(self):
        component_installer_service = composites.create_component_installer_service()
        component_installer_service.install_components()

    def _configure_zsh(self):
        configure_zsh_service = composites.create_configure_zsh_service()
        configure_zsh_service.configure_oh_my_zsh_theme()

    def _post_install_configuration(self):
        post_install_configuration_service = composites.create_post_install_configuration_service()
        post_install_configuration_service.post_configuration()

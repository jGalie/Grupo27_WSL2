# Documentación y antecedentes consultados

## Documentación oficial de Microsoft

- [Acerca de Windows Subsystem for Linux](https://learn.microsoft.com/es-es/windows/wsl/about).
- [Comparación WSL1 / WSL2](https://learn.microsoft.com/es-es/windows/wsl/compare-versions).
- [Trabajo con sistemas de archivos Windows y Linux](https://learn.microsoft.com/es-es/windows/wsl/filesystems).
- [Configuración avanzada de WSL](https://learn.microsoft.com/es-es/windows/wsl/wsl-config).
- [Acceso a aplicaciones de red con WSL](https://learn.microsoft.com/es-es/windows/wsl/networking).
- [Conectar dispositivos USB](https://learn.microsoft.com/es-es/windows/wsl/connect-usb).
- [Uso de `systemd` con WSL](https://learn.microsoft.com/es-es/windows/wsl/systemd).
- [Comandos básicos de WSL](https://learn.microsoft.com/es-es/windows/wsl/basic-commands).
- [Anuncio original de WSL2, 2019](https://devblogs.microsoft.com/commandline/announcing-wsl-2/).

## Reportes concretos de la comunidad citados en el artículo

- [`loop` — particiones de dispositivos no visibles, WSL #11170](https://github.com/microsoft/WSL/issues/11170). Es un antecedente sobre particiones, no una demostración de que todas las operaciones `loop` fallen.
- [KVM — virtualización anidada no expuesta en ciertos entornos AMD, WSL #41917](https://github.com/microsoft/WSL/issues/41917). Es un reporte contextual, no un diagnóstico de causa del equipo del grupo.
- [USB/IP — error de conexión en modo mirrored, usbipd-win #882](https://github.com/dorssel/usbipd-win/issues/882). Describe un escenario específico, no una incompatibilidad general.

La bibliografía completa y sus fechas de consulta constan en [`informe.pdf`](informe.pdf). Las fuentes documentales son antecedentes y sustento teórico; las conclusiones experimentales se basan en las pruebas del grupo.

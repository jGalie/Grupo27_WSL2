# Laboratorio 05. Persistencia de servicios

**Propósito:** examinar si tener un servicio habilitado mediante `systemd` mantiene la distribución WSL2 en ejecución al cerrar su última sesión interactiva.

En Ubuntu se verificó el estado de Nginx:

```bash
systemctl is-enabled nginx
systemctl is-active nginx
```

Los comandos devolvieron `enabled` y `active`. Después se cerró la última sesión con `exit` y, desde PowerShell, se consultó repetidamente `wsl --list --verbose`.

**Resultado:** se observó la transición de `Running` a `Stopped` aproximadamente cuatro segundos después de cerrar la sesión. Ese intervalo describe la medición puntual, no una duración universal.

**Interpretación:** administrar un servicio mediante `systemd` dentro de Ubuntu no equivale a garantizar que la instancia WSL2 permanezca activa de forma autónoma.

**Evidencia:** [Fig. 23](../evidencias/persistencia/fig-23.png).

**Referencia:** [Microsoft: `systemd` con WSL](https://learn.microsoft.com/es-es/windows/wsl/systemd).

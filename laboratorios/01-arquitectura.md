# Laboratorio 01. Arquitectura y kernel

**Propósito:** identificar la versión de WSL, la distribución, el kernel Linux y el gestor de inicialización del entorno ensayado.

Desde PowerShell se ejecutaron:

```powershell
wsl --version
wsl --status
wsl --list --verbose
```

Desde Ubuntu:

```bash
cat /etc/os-release
uname -r
cat /proc/version
systemd-detect-virt
ps -p 1 -o pid,comm,args
```

**Resultado:** WSL 3.0.3.0; Ubuntu 22.04.5 LTS sobre WSL2; kernel `6.18.54.1-microsoft-standard-WSL2`; virtualización reconocida como WSL y `systemd` como PID 1. Es consistente con una máquina virtual ligera que ejecuta un kernel Linux real, administrada por Windows.

**Evidencias:** [Fig. 1](../evidencias/arquitectura/fig-01.png), [Fig. 2](../evidencias/arquitectura/fig-02.png), [Fig. 3](../evidencias/arquitectura/fig-03.png).

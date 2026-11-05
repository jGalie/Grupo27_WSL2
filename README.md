# Análisis de la arquitectura, conectividad y limitaciones de WSL2

**Investigación experimental | Redes de Datos | FaCENA - Universidad Nacional del Nordeste (UNNE) | 2026**

**Autores:** Leonardo Oscar Canteros · Facundo Nicolás Fernandez · Julieta Itatí Gauna · Juan Agustín Ojeda.

## Investigación

Windows Subsystem for Linux 2 (WSL2) permite ejecutar un kernel Linux real mediante una máquina virtual ligera administrada por Windows. El grupo estudió **hasta qué punto permite trabajar con herramientas Linux** y qué operaciones dependen de la integración entre ambos sistemas.

El trabajo se organizó en cinco experimentos: arquitectura y kernel, conectividad (NAT y mirrored), acceso a archivos, hardware y dispositivos físicos, y persistencia de servicios. Además, se desarrolló una herramienta de diagnóstico en Python 3 con **25 comprobaciones**. Estas comprobaciones no equivalen a 25 experimentos funcionales.

## Entorno experimental

| Componente | Entorno evaluado |
| --- | --- |
| Sistema anfitrión | Windows 11 |
| WSL | 3.0.3.0; distribución bajo WSL2 |
| Distribución | Ubuntu 22.04.5 LTS |
| Kernel | `6.18.54.1-microsoft-standard-WSL2` |
| CPU | AMD Ryzen 5 5625U |
| RAM | 16 GB |
| Red | Equipo principal y otra computadora de la misma LAN |

## Resultados obtenidos

| Laboratorio | Evidencia y resultado |
| --- | --- |
| Arquitectura | Kernel Linux real; `systemd` como PID 1. |
| Red | Acceso a Nginx en NAT usando `portproxy` y firewall de Windows; en mirrored sin `portproxy`, con regla del firewall de Hyper-V. |
| Archivos | SHA-256 idéntico en las dos copias; filtrado CSV: **4,66 s en `/home` y 10,71 s en `/mnt/c`**, cinco ejecuciones por ubicación. |
| `loop` | `CONFIG_BLK_DEV_LOOP=y` y asociación/lectura efectiva mediante `losetup` y `dd`. |
| KVM | Soporte modular configurado; `/dev/kvm` y `svm` no expuestos en el entorno AMD examinado. No se identificó la causa. |
| USB | Dispositivo físico detectado en Ubuntu luego de conectar mediante `usbipd-win`; desconexión comprobada. |
| Persistencia | Nginx `enabled` y `active`; Ubuntu pasó a `Stopped` después de cerrar la última sesión. |

**Alcance:** son observaciones de la configuración evaluada. No demuestran incompatibilidades generales ni comparan Windows nativo con Linux nativo.

## Estructura del repositorio

```text
investigacion-wsl2/
├── README.md
├── .gitignore
├── docs/
│   └── investigacion/
│       ├── informe.pdf
│       ├── presentacion.pdf
│       ├── README.md
│       └── referencias.md
├── scripts/
│   ├── diagnostico_wsl2_v6_1.py
│   ├── filtrar_vuelos.py
│   └── README.md
├── laboratorios/
│   ├── 01-arquitectura.md
│   ├── 02-conectividad.md
│   ├── 03-archivos.md
│   ├── 04-hardware.md
│   └── 05-persistencia.md
├── evidencias/
│   ├── README.md
│   ├── arquitectura/
│   ├── conectividad/
│   ├── archivos/
│   ├── hardware/
│   └── persistencia/
└── datos/
    └── README.md
```

## Documentación y código

- **[Artículo de investigación](docs/investigacion/informe.pdf)** (PDF presentado por el grupo).
- **[Presentación de seis diapositivas](docs/investigacion/presentacion.pdf)** (PDF presentado por el grupo).
- **[Referencias documentales y antecedentes comunitarios](docs/investigacion/referencias.md)**.
- **[Procedimientos de los cinco laboratorios](laboratorios/01-arquitectura.md)** y resto de archivos de [`laboratorios/`](laboratorios/).
- **[Capturas individuales de las 23 figuras](evidencias/README.md)**, extraídas del informe sin alterar el contenido.
- **[Programa de diagnóstico](scripts/diagnostico_wsl2_v6_1.py)** y **[script de filtrado de vuelos](scripts/filtrar_vuelos.py)**.
- **[Descripción del conjunto de datos](datos/README.md)**.

## Ejecución de las herramientas

En una distribución Ubuntu sobre WSL2, desde la raíz del repositorio:

```bash
python3 scripts/diagnostico_wsl2_v6_1.py
python3 scripts/filtrar_vuelos.py /ruta/al/vuelos_enero_2025.csv
```

La primera herramienta registra consultas y evaluaciones sin alterar la configuración del sistema; escribe únicamente archivos de evidencia en `~/resultados_wsl2/`. La segunda cuenta las filas cuyo campo `Origin` coincide con `JFK`. Para el procedimiento completo y las condiciones de los ensayos, consultar [`scripts/README.md`](scripts/README.md) y [`laboratorios/03-archivos.md`](laboratorios/03-archivos.md).

El CSV experimental de aproximadamente **243 MB** no forma parte del repositorio por su tamaño. Los resultados medidos están documentados en el informe y las evidencias incluidas.

## Conclusión

La investigación mostró que WSL2 integra herramientas y servicios Linux con Windows, pero que el acceso a redes, archivos, dispositivos y ciertos recursos de virtualización depende de las condiciones concretas del sistema. El diagnóstico automatizado ayudó a diferenciar **soporte configurado, recurso expuesto y funcionamiento efectivo**, complementado con pruebas manuales donde correspondía.

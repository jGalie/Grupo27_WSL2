# Scripts empleados en la investigación

## `diagnostico_wsl2_v6_1.py`

Programa original de Python 3 utilizado para **25 comprobaciones de diagnóstico** agrupadas en módulos del kernel, KVM y USB. Utiliza `subprocess`, consultas al sistema de archivos y evaluaciones derivadas. Exporta `resumen.csv`, `metadatos.json` y archivos de texto individualizados bajo `~/resultados_wsl2/FECHA_HORA/`.

**Ejecución desde Ubuntu/WSL2**:

```bash
python3 scripts/diagnostico_wsl2_v6_1.py
```

**Interpretación:** `CONFIG_BLK_DEV_LOOP=y` indica integración de soporte; `/dev/kvm` ausente indica recurso no expuesto en ese momento; `modprobe -n -v` es una simulación de carga y `lsusb` informa enumeración. Ninguno de esos indicadores sustituye una prueba funcional. El script no necesita `sudo` ni cambia la configuración del sistema; solamente guarda registros de sus consultas. Algunas consultas a KVM son específicas de AMD, conforme al entorno ensayado.

## `filtrar_vuelos.py`

Script original utilizado en el laboratorio del CSV. Se recuperó del código compartido durante el desarrollo de la investigación y se conserva con su algoritmo original: abre el archivo con `utf-8-sig`, recorre los registros con `csv.DictReader`, cuenta las filas cuyo campo `Origin` es `JFK` e imprime el total.

```bash
python3 scripts/filtrar_vuelos.py /ruta/al/vuelos_enero_2025.csv
```

El CSV empleado en el estudio produjo **8.327 vuelos con origen JFK**. Para medir tiempos se ejecutó este programa cinco veces sobre cada copia del mismo CSV, usando `/usr/bin/time` en Ubuntu/WSL2. Ejemplo de ejecución individual:

```bash
/usr/bin/time -f 'Tiempo: %e segundos' python3 scripts/filtrar_vuelos.py /ruta/al/vuelos_enero_2025.csv
```

Los promedios observados fueron **4,66 s en `/home`** y **10,71 s en `/mnt/c`**; son mediciones propias del entorno documentado, no resultados que el script garantice en otras máquinas.

Los scripts utilizan la biblioteca estándar de Python. Para `diagnostico_wsl2_v6_1.py`, las utilidades de Linux consultadas deben estar instaladas para que cada comprobación sea informativa.

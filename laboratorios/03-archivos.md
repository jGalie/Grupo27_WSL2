# Laboratorio 03. Sistemas de archivos y rendimiento

**Propósito:** comparar la integridad de un mismo archivo, su tiempo de procesamiento y el efecto de permisos entre `/home` (sistema Linux) y `/mnt/c` (unidad de Windows montada).

**Archivo:** `vuelos_enero_2025.csv`, 243.177.378 bytes y 539.748 líneas, con 8.327 registros cuyo `Origin` es `JFK`.

**Procedimiento ejecutado:** copiar el CSV entre ubicaciones; comparar `sha256sum`; ejecutar el mismo [`filtrar_vuelos.py`](../scripts/filtrar_vuelos.py) cinco veces desde cada ruta; obtener tiempos con `/usr/bin/time`; comparar `chmod 600` sobre copias temporales.

```bash
# Ejemplo de medición individual: ejecutado dentro de WSL2
/usr/bin/time -f 'Tiempo: %e segundos' python3 scripts/filtrar_vuelos.py /ruta/al/vuelos_enero_2025.csv
```

**Resultados:** los SHA-256 coincidieron. El procesamiento promedió 4,66 s desde `/home` y 10,71 s desde `/mnt/c` (aproximadamente 2,3 veces más tiempo en el ensayo realizado). `chmod 600` produjo `rw-------` en `/home`, mientras que la copia sobre `/mnt/c` mantuvo `rwxrwxrwx` bajo la configuración de montaje del laboratorio.

**Interpretación:** las rutas Linux y Windows tienen diferentes mecanismos de acceso y manejo de permisos dentro de WSL2. No se compararon sistemas operativos nativos entre sí.

**Evidencias:** [Fig. 10](../evidencias/archivos/fig-10.png), [11](../evidencias/archivos/fig-11.png), [12](../evidencias/archivos/fig-12.png), [13](../evidencias/archivos/fig-13.png).

**Referencia:** [Microsoft: sistemas de archivos](https://learn.microsoft.com/es-es/windows/wsl/filesystems).

# Conjunto de datos: vuelos de enero de 2025

En el laboratorio de archivos se utilizó `vuelos_enero_2025.csv` con las siguientes características verificadas en el informe:

| Característica | Valor |
| --- | ---: |
| Tamaño | 243.177.378 bytes |
| Líneas, incluido encabezado | 539.748 |
| Registros con `Origin == "JFK"` | 8.327 |
| Copias analizadas | Linux (`/home`) y unidad Windows (`/mnt/c`) |
| Integridad | Igualdad de sumas SHA-256 |
| Mediciones | 5 ejecuciones por ubicación |
| Tiempo medio en `/home` | 4,66 s |
| Tiempo medio en `/mnt/c` | 10,71 s |

El archivo CSV **no se distribuye en Git** porque supera el límite ordinario de tamaño de GitHub por archivo (100 MB). Los valores medidos se conservaron en el [artículo](../docs/investigacion/informe.pdf) y en las [capturas de los experimentos](../evidencias/README.md).

El script de filtrado utilizado es [`scripts/filtrar_vuelos.py`](../scripts/filtrar_vuelos.py). Requiere un CSV con encabezado que incluya la columna `Origin`. Para reproducir la comparación de archivos, se deben utilizar copias idénticas del conjunto de datos en una ruta Linux y otra en `/mnt/c`; esta condición se comprueba mediante `sha256sum`.

La diferencia de tiempos describe **acceso a dos ubicaciones desde el mismo Ubuntu sobre WSL2**; no es una prueba comparativa de Windows nativo versus Linux nativo.

# Procesador de datos Titanic con Docker

Script de Python que limpia el dataset Titanic y calcula estadísticas, empaquetado en una imagen Docker.

## Qué hace
1. Lee `train.csv` (Titanic, Kaggle).
2. Elimina duplicados y la columna `Cabin` (más del 70 % vacía).
3. Rellena las edades vacías con la mediana y elimina filas sin `Embarked`.
4. Guarda el CSV limpio y un CSV de estadísticas.

## Imagen en Docker Hub
https://hub.docker.com/r/angelino16/procesador-datos (etiqueta `1.0.0`)

## Datos de entrada
Descarga `train.csv` desde la competición "Titanic - Machine Learning from Disaster" en Kaggle y colócalo en una carpeta `entrada/`.

## Ejecutar
Crea las carpetas `entrada` (con `train.csv`) y `salida`, y desde la carpeta que las contiene ejecuta:

**Windows (cmd):**
```
docker run --rm -v "%cd%\entrada:/data/input" -v "%cd%\salida:/data/output" angelino16/procesador-datos:1.0.0
```

**Linux / macOS:**
```
docker run --rm -v "$(pwd)/entrada:/data/input" -v "$(pwd)/salida:/data/output" angelino16/procesador-datos:1.0.0
```

## Construir la imagen localmente
```
docker build -t angelino16/procesador-datos:1.0.0 .
```

## Variables de entorno
| Variable | Descripción | Valor por defecto |
|---|---|---|
| `INPUT_PATH` | Ruta del CSV de entrada | `/data/input/train.csv` |
| `OUTPUT_PATH` | Ruta del CSV limpio | `/data/output/titanic_limpio.csv` |
| `STATS_PATH` | Ruta del CSV de estadísticas | `/data/output/estadisticas.csv` |

Ejemplo cambiando un valor: agrega `-e OUTPUT_PATH=/data/output/otro.csv` al comando `docker run`.

## Volúmenes
| Ruta en el contenedor | Uso |
|---|---|
| `/data/input` | Entrada (aquí debe estar `train.csv`) |
| `/data/output` | Salida (se generan los CSV) |

## Puertos
No aplica (el contenedor no expone puertos).

## Salida esperada
```
Filas iniciales: 891
Edades vacías rellenadas con la mediana: 177
Filas después de limpiar: 889
Tasa de supervivencia: 38.25 %
Archivo limpio guardado en: /data/output/titanic_limpio.csv
Estadísticas guardadas en: /data/output/estadisticas.csv

Estadísticas:
          Age    Fare  Pclass  Survived
count  889.00  889.00  889.00    889.00
mean    29.32   32.10    2.31      0.38
std     12.98   49.70    0.83      0.49
min      0.42    0.00    1.00      0.00
25%     22.00    7.90    2.00      0.00
50%     28.00   14.45    3.00      0.00
75%     35.00   31.00    3.00      1.00
max     80.00  512.33    3.00      1.00
```

## Evidencia de publicación
Captura de la etiqueta `1.0.0` en Docker Hub: `evidencia/dockerhub-tags.png`
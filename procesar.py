import os
import sys

import pandas as pd

INPUT_PATH = os.getenv("INPUT_PATH", "entrada/train.csv")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "salida/titanic_limpio.csv")
STATS_PATH = os.getenv("STATS_PATH", "salida/estadisticas.csv")


def main():
    if not os.path.exists(INPUT_PATH):
        print(f"ERROR: no se encontró el archivo de entrada: {INPUT_PATH}")
        sys.exit(1)

    df = pd.read_csv(INPUT_PATH)
    filas_iniciales = len(df)
    nulos_age = int(df["Age"].isna().sum())

    # 1. Quitar duplicados
    df = df.drop_duplicates()

    # 2. Eliminar la columna Cabin
    df = df.drop(columns=["Cabin"])

    # 3. Rellenar edades vacías con la mediana
    df["Age"] = df["Age"].fillna(df["Age"].median())

    # 4. Eliminar filas sin puerto de embarque
    df = df.dropna(subset=["Embarked"])

    # 5. Normalizar texto
    df["Sex"] = df["Sex"].str.strip().str.title()
    df["Name"] = df["Name"].str.strip()

    estadisticas = df[["Age", "Fare", "Pclass", "Survived"]].describe().round(2)
    tasa_supervivencia = round(df["Survived"].mean() * 100, 2)

    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    os.makedirs(os.path.dirname(STATS_PATH) or ".", exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)
    estadisticas.to_csv(STATS_PATH)

    print(f"Filas iniciales: {filas_iniciales}")
    print(f"Edades vacías rellenadas con la mediana: {nulos_age}")
    print(f"Filas después de limpiar: {len(df)}")
    print(f"Tasa de supervivencia: {tasa_supervivencia} %")
    print(f"Archivo limpio guardado en: {OUTPUT_PATH}")
    print(f"Estadísticas guardadas en: {STATS_PATH}")
    print("\nEstadísticas:")
    print(estadisticas)


if __name__ == "__main__":
    main()
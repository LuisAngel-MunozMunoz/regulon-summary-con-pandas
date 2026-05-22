from pathlib import Path
import pandas as pd


def ensure_output_dir(output_file: str) -> None:
    output_path = Path(output_file)

    if output_path.parent != Path("."):
        output_path.parent.mkdir(parents=True, exist_ok=True)


def write_summary(regulon: pd.DataFrame, output_file: str) -> None:
    ensure_output_dir(output_file)
    ...


def write_sif(interactions: pd.DataFrame, output_file: str) -> None:
    ensure_output_dir(output_file)

    # Crear un DataFrame con TF, effect y gene
    sif = 

    # Guardar el DataFrame en formato SIF (tab-separado, sin encabezado)
    ...

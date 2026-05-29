from pathlib import Path
import pandas as pd


def ensure_output_dir(output_file: str) -> None:
    output_path = Path(output_file)

    if output_path.parent != Path("."):
        output_path.parent.mkdir(parents=True, exist_ok=True)


def write_summary(regulon: pd.DataFrame, output_file: str) -> None:
    ensure_output_dir(output_file)
    regulon.to_csv(output_file, sep="\t", index=False)


def write_sif(interactions: pd.DataFrame, output_file: str) -> None:
    ensure_output_dir(output_file)

    sif = interactions[["TF", "effect", "gene"]]
    sif.to_csv(output_file, sep="\t", index=False, header=False)

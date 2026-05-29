import pandas as pd

VALID_EFFECTS = {"+", "-", "-+"}


def load_interactions(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename, sep="\t", comment="#")

    df = df.rename(
        columns={
            "2)regulatorName": "TF",
            "5)geneName": "gene",
            "6)function": "effect",
        }
    )

    required_columns = ["TF", "gene", "effect"]
    df = df[required_columns]

    df = df.dropna(subset=required_columns)
    df = df[df["effect"].isin(VALID_EFFECTS)]

    return df

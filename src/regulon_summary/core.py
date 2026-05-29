import pandas as pd


def classify_regulator(row: pd.Series) -> str:
    if row["activados"] > 0 and row["reprimidos"] == 0:
        return "activador"

    if row["activados"] == 0 and row["reprimidos"] > 0:
        return "represor"

    if row["activados"] > 0 and row["reprimidos"] > 0:
        return "dual"

    return "unknown"


def build_regulon(interactions: pd.DataFrame) -> pd.DataFrame:
    df = interactions.copy()

    df["is_activated"] = df["effect"].isin(["+", "-+"])
    df["is_repressed"] = df["effect"].isin(["-", "-+"])

    regulon = (
        df.groupby("TF")
        .agg(
            total_genes=("gene", "nunique"),
            activados=("is_activated", "sum"),
            reprimidos=("is_repressed", "sum"),
            genes=("gene", lambda values: ",".join(sorted(set(values)))),
        )
        .reset_index()
    )

    regulon["type"] = regulon.apply(classify_regulator, axis=1)

    return regulon

import pandas as pd


def filter_by_min_genes(regulon: pd.DataFrame, min_genes: int) -> pd.DataFrame:
    return ...


def filter_by_type(regulon: pd.DataFrame, regulator_type: str) -> pd.DataFrame:
    if regulator_type == "all":
        return ...

    return ...


def filter_interactions_by_regulon(
    interactions: pd.DataFrame,
    regulon: pd.DataFrame,
) -> pd.DataFrame:
    valid_tfs = set(regulon["TF"])

    return ...

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

    # Agregar columnas para indicar si la interacción es de activación o represión
    ... = 
    ... = 

    # Agrupar por TF y calcular el número total de genes regulados, activados, reprimidos y la lista de genes
    regulon = 

    # Clasificar cada regulador como activador, represor o dual en una nueva columna
    ... = 

    return regulon

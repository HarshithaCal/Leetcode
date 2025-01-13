import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df = students.dropna(subset=["name"], inplace=False)
    #axis = 1 - columns or axis = "columns"

    ###Keep only the rows with at least 2 non-NA values.
    # df.dropna(thresh=2)

    #### in which columns to look for missing values.
    # df.dropna(subset=['name', 'toy'])

    return df
    
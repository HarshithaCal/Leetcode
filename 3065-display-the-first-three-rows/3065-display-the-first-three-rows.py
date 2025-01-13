import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # return employees.head(3)

    # pd.iloc:
    # Integer-based indexing: It uses integer positions to access rows and columns.
    # Syntax: df.iloc[row_index, column_index]
    return employees.iloc[0:3,:]

    # pd.loc:
    # Label-based indexing: It uses labels (row and column names) to access data.
    # Syntax: df.loc[row_label, column_label]
    # return employees.loc[:2]
    
    
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
   #axis = 0 - vertically - default
   #axis = 0 - horizontally
    
    return pd.concat([df1, df2], ignore_index=True, axis=0)
    
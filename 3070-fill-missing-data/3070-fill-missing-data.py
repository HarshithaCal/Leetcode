import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # products["quantity"]= products["quantity"].fillna(0)
    products.fillna({"quantity":0}, inplace = True)
    return products
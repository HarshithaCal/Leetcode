import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    #unpivoting- melt
    df = pd.melt(products, id_vars='product_id', value_vars=['store1', "store2", "store3"])
    print(df.columns)
    df =  df.dropna(subset="value").rename(columns={"variable":"store", "value":"price"})
    return df

    
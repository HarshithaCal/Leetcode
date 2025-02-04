import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # df =  pd.merge(customers, orders, left_on='id', right_on = "customerId", how = 'left') ### like SQL
    # df = df[df["customerId"].isna()][["name"]]
    # df = df.rename(columns = {"name":"Customers"})
    # return df

    df=customers[~customers['id'].isin(orders['customerId'])]
    df=df[['name']].rename(columns={'name':'Customers'})
    return df

    

    
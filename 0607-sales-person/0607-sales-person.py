import pandas as pd 

def func(group):
    if (group != "RED").all():
        return True
    return False
    
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
 
    df = sales_person.merge(orders, left_on="sales_id", right_on="sales_id", how="left")
    df = df.merge(company, left_on="com_id", right_on="com_id", how="left")
    grouped = df.groupby(by="name_x")["name_y"].apply(func)
    
    # 4. Extract the names of salespeople who never sold to 'RED'
    not_red_sales = grouped[grouped].index 
    
    result = sales_person[sales_person["name"].isin(not_red_sales)][["name"]]
    return result

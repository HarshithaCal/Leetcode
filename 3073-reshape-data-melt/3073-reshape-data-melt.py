import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2',"quarter_3", "quarter_4"])
    df = df.rename(columns={"variable": "quarter", "value": "sales"})


    #or 
    # df = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return df
    
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # ?customers.drop_duplicates()
    # help(pd.DataFrame.drop_duplicates)
    return customers.drop_duplicates(subset=['email'])
    
    
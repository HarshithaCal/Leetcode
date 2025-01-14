import pandas as pd
import re


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].apply(func)]

def func(mail: str) -> bool:
    pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$"
    return bool(re.match(pattern, mail))

    
    
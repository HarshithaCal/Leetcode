import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["corrected"] = users["name"].apply(lambda x: x[0].upper() + x[1:].lower())
    return users[["user_id", "corrected"]].rename(columns = {"corrected":"name"}).sort_values("user_id", ascending = True)
    
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = person.duplicated(subset=["email"])
    result = person[duplicates][["email"]].drop_duplicates().rename(columns={"email":"Email"})
    return result
    
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(["actor_id", "director_id"]).size().reset_index()
    res = grouped[grouped[0]>2]
    return res[["actor_id", "director_id"]]
    # return df
    
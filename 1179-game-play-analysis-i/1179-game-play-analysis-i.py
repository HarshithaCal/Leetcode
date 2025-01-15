import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby(["player_id"], as_index=False).agg(min)
    # result["rank"] = result["event_date"].rank()
    return result[["player_id", "event_date"]].rename(columns = {"event_date": "first_login"})
    
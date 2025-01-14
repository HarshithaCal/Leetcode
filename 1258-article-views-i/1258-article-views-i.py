import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # views= views.drop_duplicates()   ###### doesn't work as there can be same person viewing the articles on different days.
    df = views[views.author_id == views.viewer_id].sort_values(by="author_id", ascending=True)[[ "author_id"]].rename(columns = {"author_id":"id"})
    df = df.drop_duplicates()
    return df
    
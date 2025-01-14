import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets["content"].str.len() > 15][["tweet_id"]]
    # df = tweets[len(tweets["content"]) > 15][["tweet_id"]] #len(tweets(["content"])) - doesn't work on each element seperately
    return df
    
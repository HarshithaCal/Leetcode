import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # works - df = tweets[tweets["content"].str.len() > 15][["tweet_id"]]
    
    # doesn't work -  df = tweets[len(tweets["content"]) > 15][["tweet_id"]] #len(tweets(["content"])) - doesn't work on each element seperately
    
    tweets["content_length"] = tweets["content"].apply(lambda row: len(row) > 15)
    return tweets[tweets["content_length"]][["tweet_id"]]
    
    
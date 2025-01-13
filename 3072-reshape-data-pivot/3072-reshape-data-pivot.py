import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot(index=["month"], columns = ["city"], values="temperature")
    # pivoted_df = weather.pivot_table(index='month', columns='city', values='temperature', aggfunc='mean')
    return weather

    


    
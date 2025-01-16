import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby(["class"])["student"].nunique().reset_index("class")
    result = result[result["student"]>4]
    return result[["class"]]
    
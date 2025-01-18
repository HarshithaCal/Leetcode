import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    res = employee.groupby(by="managerId").size().reset_index()
    res = res[res[0]>= 5]

    ##Merge this res with the employee to get the manager name
    res = res.merge(employee[["id", "name"]], left_on= "managerId", right_on= "id", how="inner")
    return res[["name"]]
    
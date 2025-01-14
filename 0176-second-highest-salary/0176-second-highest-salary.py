import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary")
    employee = employee.sort_values(by="salary", ascending=False)
    if employee.shape[0] < 2:
        return pd.DataFrame({"SecondHighestSalary":[None]})
    return pd.DataFrame({"SecondHighestSalary":[employee.iloc[1]["salary"]]})
    
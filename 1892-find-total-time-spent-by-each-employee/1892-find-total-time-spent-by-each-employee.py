import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["event_day", "emp_id"], as_index=False)["total_time"].sum()
    return employees.rename(columns = {"event_day":"day"})
    
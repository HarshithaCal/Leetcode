import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on="departmentId", right_on="id")
    df["rank"] = df.groupby("name_y")["salary"].rank(method="dense", ascending=False)
    df = df[df["rank"] == 1][["name_y","name_x", "salary"]].rename(columns= {"name_y":"Department", "name_x":"Employee", "salary":"Salary"})
    return df

    
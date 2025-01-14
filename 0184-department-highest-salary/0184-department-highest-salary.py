import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on="departmentId", right_on="id")
    df["rank"] = df.groupby("name_y")["salary"].rank(method="dense", ascending=False)
    df = df[df["rank"] == 1][["name_y","name_x", "salary"]].rename(columns= {"name_y":"Department", "name_x":"Employee", "salary":"Salary"})
    return df

##### Approach 2:
    # join_tbl = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id', how = 'left')
    # max_salary = join_tbl.groupby('name_y')['salary'].transform('max')
    # res = join_tbl[join_tbl.salary == max_salary]
    # return(res[['name_y', 'name_x', 'salary']].rename(columns = {'name_y' : 'Department', 'name_x' : 'Employee', 'salary' : 'Salary'}))

    
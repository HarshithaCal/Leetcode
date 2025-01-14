import pandas as pd

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    employee = employee.drop_duplicates(subset="salary")
    
    employee = employee.sort_values(by="salary", ascending=False)
    
    if N > len(employee) or N <= 0:
        return pd.DataFrame({"getNthHighestSalary(" + str(N) + ")": [None]})

    nth_highest = employee.iloc[N-1]["salary"]

    return pd.DataFrame({"getNthHighestSalary(" + str(N) + ")": [nth_highest]})

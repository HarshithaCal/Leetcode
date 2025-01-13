import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    ### [] - creates a new column if not present
    employees["bonus"] = 2*employees.salary
    ###!!!!!!!! this . doesn't create a new column if it is not present 
    ####    so this ** doesn't work **
    # employees.bonus = 2*employees.salary
    return employees
    
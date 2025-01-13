import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    columns = ["student_id", "first_name", "last_name", "age_in_years"]
    students.columns = columns
    return students
    
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:

    students.rename(
        columns={'id':'student_id',
        'first':'first_name',
        'last':'last_name',
        'age':'age_in_years'},
        inplace=True)

    return students

    # columns = ["student_id", "first_name", "last_name", "age_in_years"]
    # students.columns = columns
    # return students
    
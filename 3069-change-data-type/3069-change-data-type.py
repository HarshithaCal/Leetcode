import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # print(students.dtypes)
    convert_dict = {'grade': int}
    # Convert columns using the dictionary
    students = students.astype(convert_dict)
    return students

    
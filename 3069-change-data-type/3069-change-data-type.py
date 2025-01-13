import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # print(students.dtypes)

    # #########good for multiple columns 
    # convert_dict = {'grade': int}
    # # Convert columns using the dictionary
    # students = students.astype(convert_dict)

    ####### for single col:
    students['grade'] = students['grade'].astype(int)
    return students

    
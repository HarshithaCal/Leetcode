import pandas as pd
import re


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["mail"].apply(func)]

def func(mail: str) -> bool:
    pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$"
    return bool(re.match(pattern, mail))

# def check(mail):
#         if (mail[0].isalpha()) and ('@' in mail) and (mail[mail.index('@'):] == '@leetcode.com'):
#             for i in mail[:mail.index('@')]:
#                 if not (i.isalnum() or (i in ['_','.','-'])):
#                     return False
#             return True
#         else:
#             return False
#     return users[users['mail'].apply(lambda x:check(x))]


######Another approach
    # result_df = users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com')]
    # return result_df

    
    
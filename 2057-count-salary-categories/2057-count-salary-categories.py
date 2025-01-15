import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Count accounts for each category
    low_salary_count = accounts[accounts.income < 20000].shape[0]
    average_salary_count = accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0]
    high_salary_count = accounts[accounts.income > 50000].shape[0]
    
    # Create the result DataFrame
    result = pd.DataFrame({
        "category": ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count": [low_salary_count, average_salary_count, high_salary_count]
    })
    
    return result
    
    
# 2882. Drop Duplicate Rows
# Problem link: https://leetcode.com/problems/drop-duplicate-rows/description/
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers
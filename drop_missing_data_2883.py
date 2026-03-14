# 2883. Drop Missing Data
# Problem link: https://leetcode.com/problems/drop-missing-data/description/
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students
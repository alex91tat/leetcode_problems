# 2886. Change Data Type
# Problem link: https://leetcode.com/problems/change-data-type/description/
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade': int})
    return students
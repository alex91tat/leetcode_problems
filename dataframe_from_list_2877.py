# 2877. Create a DataFrame from List
# Problem link: https://leetcode.com/problems/create-a-dataframe-from-list/description/
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df
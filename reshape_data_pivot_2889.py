# 2889. Reshape Data: Pivot
# Problem link: https://leetcode.com/problems/reshape-data-pivot/description/
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    ans = weather.pivot(index='month', columns='city', values='temperature')
    return ans  
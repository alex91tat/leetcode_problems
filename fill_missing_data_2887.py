# 2887. Fill Missing Data
# Problem link: https://leetcode.com/problems/fill-missing-data/description/
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products
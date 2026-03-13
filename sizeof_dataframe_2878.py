# 2878. Get the Size of a DataFrame
# Problem link: https://leetcode.com/problems/get-the-size-of-a-dataframe/description/
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players), len(players.columns)]

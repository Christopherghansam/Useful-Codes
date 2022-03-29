import numpy as np
import pandas as pd
df1 = pd.DataFrame({'lkey': ['faa', 'baa', 'bzz', 'faa'],
                    'value': [2, 3, 5, 7]})
df2 = pd.DataFrame({'rkey': ['faa', 'baa', 'bzz', 'faa'],
                    'value': [7, 8, 9, 10]})
X = df1.merge(df2, left_on='lkey', right_on='rkey')
print(X)
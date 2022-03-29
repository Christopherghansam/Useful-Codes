import pandas as pd
import numpy as np
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(dict)
df = df.replace(np.nan, 'False')
df = df.replace([100, 90, 95, 30, 45, 56, 40, 80, 98], 'True')
print(df)

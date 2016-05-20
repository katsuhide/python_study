#import liblaries
import pandas as pd
import numpy as np

## Create a Index
dates = pd.date_range("20140101", periods=6)
print(dates)

## Create a DataFrame
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))
print(df)

df2 = pd.DataFrame({ 'A': 1.,
                     'B': pd.Timestamp('20130102'),
                     'C': pd.Series(1, index = list(range(4)), dtype = 'float32'),
                     'D': np.array([3] * 4, dtype = 'int32'),
                     'E': pd.Categorical(["test", "train", "test", "train"]),
                     'F': 'foo'  })
print(df2)

# print date type
print(df2.dtypes)

# print data info
print(df.index)
print(df.columns)
print(df.values)

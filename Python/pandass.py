# import pandas as pd 
# import numpy as np

# arr = np.arange(12).reshape(3,4)  # 3*4 = 12 elements
# df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])
# print(df)

# data = {
#     'Name': ['Amit', 'Raj', 'Priya'],
#     'Age': [25, 30, 22],
#     'City': ['Delhi', 'Mumbai', 'Pune']
# }
# df = pd.DataFrame(data)
# print(df)


# data = [
#     {'Name': 'Amit', 'Age': 25},
#     {'Name': 'Raj', 'Age': 30}
# ]
# df = pd.DataFrame(data)
# print(df)


# data = {
#     'Name': ['Amit', 'Raj', 'Priya'],
#     'Age': [25, 30, 22],
#     'City': ['Delhi', 'Mumbai', 'Pune']
# }
# df = pd.DataFrame(data)
# print(df)


# print(df.shape)   # (rows, columns)
# print(df.columns) # column names
# print(df.index)   # row indexes
# print(df.dtypes)  # data types of columns


# print(df['Name'])        # single column
# print(df[['Name','City']]) # multiple columns
# print(df.iloc[2])        # row by index (positional)
# print(df.loc[1])         # row by label (index name)


# print(df.head())     # first 5 rows
# print(df.tail())     # last 5 rows
# print(df.describe()) # stats summary (numerical cols)
# print(df.info())     # metadata

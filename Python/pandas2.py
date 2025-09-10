import pandas as pd
import numpy as np
from io import StringIO


# Create a DataFrame
df = pd.read_csv("/Users/amityadav/Desktop/AIML/Python/sample_data.csv")
print(df)
print(type(df))


import pandas as pd
from io import StringIO

csv_data = """Name,Age,City,Salary
Amit,25,Delhi,50000
Raj,30,Mumbai,60000
Priya,22,Pune,55000
"""

# Treat the string as a file
df = pd.read_csv(StringIO(csv_data), usecols=['Name', 'City'])
print(df)

import pandas as pd
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "sales_data.csv"
)

df = pd.read_csv(file_path)

print(df.head())
print("\nTotal Records:", len(df))
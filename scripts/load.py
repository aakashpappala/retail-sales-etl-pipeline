import pandas as pd
import os
from sqlalchemy import create_engine

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "cleaned_sales.csv"
)

df = pd.read_csv(file_path)

engine = create_engine(
    "postgresql://postgres:Aakash@localhost:5432/retail_db"
)

df.to_sql(
    "sales",
    engine,
    if_exists="append",
    index=False
)

print("Data Loaded Successfully")
import pandas as pd
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "sales_data.csv"
)

df = pd.read_csv(file_path)

# Remove duplicates
df = df.drop_duplicates()

# Create total_amount column
df["total_amount"] = df["quantity"] * df["price"]

# Save cleaned file
output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "cleaned_sales.csv"
)

df.to_csv(output_path, index=False)

print("Transformation Completed")
print(df.head())
import pandas as pd

# Read CSV file
df = pd.read_csv("employee_data.csv")

# Add bonus column
df["bonus"] = df["salary"] * 0.10

# Save transformed data
df.to_csv("processed_employee_data.csv", index=False)

print("ETL Process Completed Successfully")
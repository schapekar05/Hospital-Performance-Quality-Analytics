import pandas as pd
import os

# Read the hospital data
df = pd.read_csv("Hospital_General_Information_2.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()
df.columns = df.columns.str.replace(" ", "_", regex=False)
df.columns = df.columns.str.replace("/", "_", regex=False)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert rating to numbers
df["hospital_overall_rating"] = pd.to_numeric(
    df["hospital_overall_rating"], errors="coerce"
)

# Save the cleaned file
os.makedirs("output", exist_ok=True)
df.to_csv("output/cleaned_hospitals.csv", index=False)

print("Data cleaning completed.")
print("Total hospitals:", len(df))

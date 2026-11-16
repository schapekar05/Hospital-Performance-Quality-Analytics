import pandas as pd
import os

# Read the hospital data
df = pd.read_csv("Hospital_General_Information_2.csv", dtype={"Facility ID": "string"})

# Clean column names
df.columns = df.columns.str.strip().str.lower()
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("/", "_")

# Remove extra spaces from text
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# Replace blank cells with missing values
df = df.replace("", pd.NA)

# Remove empty rows and duplicate records
df = df.dropna(how="all")
df = df.drop_duplicates()

# Clean facility IDs and hospital ratings
df["facility_id"] = df["facility_id"].astype("string").str.strip()
df["hospital_overall_rating"] = pd.to_numeric(
    df["hospital_overall_rating"], errors="coerce"
)

# Save the cleaned data
os.makedirs("output", exist_ok=True)
df.to_csv("output/cleaned_hospitals.csv", index=False)

print("Data cleaning completed.")
print("Total hospitals:", len(df))

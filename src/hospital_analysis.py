import pandas as pd
from pathlib import Path

# Load the hospital data
df = pd.read_csv("Hospital_General_Information_2.csv")

# Clean column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace("/", "_", regex=False)
)

# Clean text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# Remove blank and duplicate rows
df = df.replace(r"^\s*$", pd.NA, regex=True)
df = df.dropna(how="all")
df = df.drop_duplicates()

# Set correct data types
df["facility_id"] = df["facility_id"].astype("string")
df["hospital_overall_rating"] = pd.to_numeric(
    df["hospital_overall_rating"], errors="coerce"
)

# Create output folder
output = Path("output")
output.mkdir(exist_ok=True)

# Save cleaned data for Tableau
df.to_csv(output / "cleaned_hospitals.csv", index=False)

# Hospital count by state
df["state"].value_counts().to_csv(output / "hospitals_by_state.csv")

# Hospital rating distribution
df["hospital_overall_rating"].value_counts().sort_index().to_csv(
    output / "rating_distribution.csv"
)

# Missing values report
missing = df.isna().sum().reset_index()
missing.columns = ["column", "missing_count"]
missing.to_csv(output / "missing_values_report.csv", index=False)

print("Analysis completed.")
print("Total hospitals:", len(df))
print("Total columns:", len(df.columns))
print("Cleaned data and summary files saved in the output folder.")

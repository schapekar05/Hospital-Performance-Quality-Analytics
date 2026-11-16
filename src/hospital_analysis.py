from pathlib import Path
import pandas as pd

# Project folders
project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "Hospital_General_Information_2.csv"
output_folder = project_folder / "output"
output_folder.mkdir(exist_ok=True)

# Check that the source file exists
if not input_file.exists():
    raise FileNotFoundError(
        "Hospital_General_Information_2.csv was not found in the project folder."
    )

# Read the original data and keep facility IDs as text
df = pd.read_csv(input_file, dtype={"Facility ID": "string"})

# Keep the original row count for the data quality summary
original_rows = len(df)

# Clean column names without using regular expressions
clean_columns = []
for column in df.columns:
    column = column.strip().lower()
    column = column.replace(" ", "_")
    column = column.replace("/", "_")
    clean_columns.append(column)

df.columns = clean_columns

# Remove extra spaces from text columns
for column in df.select_dtypes(include=["object", "string"]).columns:
    df[column] = df[column].str.strip()

# Convert empty text cells into missing values
df = df.replace("", pd.NA)

# Remove completely empty rows and duplicate records
df = df.dropna(how="all")
rows_after_empty_removal = len(df)

df = df.drop_duplicates()
cleaned_rows = len(df)

# Convert hospital rating to a number
if "hospital_overall_rating" in df.columns:
    df["hospital_overall_rating"] = pd.to_numeric(
        df["hospital_overall_rating"], errors="coerce"
    )

# Save the cleaned dataset
cleaned_file = output_folder / "cleaned_hospitals.csv"
df.to_csv(cleaned_file, index=False)

# Create a summary of hospitals by state
if "state" in df.columns:
    state_summary = (
        df.groupby("state", dropna=False)
        .size()
        .reset_index(name="hospital_count")
        .sort_values("hospital_count", ascending=False)
    )
    state_summary.to_csv(output_folder / "hospitals_by_state.csv", index=False)

# Create a summary of hospital ratings
if "hospital_overall_rating" in df.columns:
    rating_summary = (
        df["hospital_overall_rating"]
        .value_counts(dropna=False)
        .sort_index()
        .reset_index()
    )
    rating_summary.columns = ["hospital_overall_rating", "hospital_count"]
    rating_summary.to_csv(output_folder / "rating_distribution.csv", index=False)

# Create a summary by hospital type
if "hospital_type" in df.columns:
    type_summary = (
        df.groupby("hospital_type", dropna=False)
        .size()
        .reset_index(name="hospital_count")
        .sort_values("hospital_count", ascending=False)
    )
    type_summary.to_csv(output_folder / "hospitals_by_type.csv", index=False)

# Create a summary by hospital ownership
if "hospital_ownership" in df.columns:
    ownership_summary = (
        df.groupby("hospital_ownership", dropna=False)
        .size()
        .reset_index(name="hospital_count")
        .sort_values("hospital_count", ascending=False)
    )
    ownership_summary.to_csv(
        output_folder / "hospitals_by_ownership.csv", index=False
    )

# Create a missing values report
missing_report = pd.DataFrame({
    "column_name": df.columns,
    "missing_count": df.isna().sum().values,
    "missing_percentage": (
        df.isna().sum().values / len(df) * 100 if len(df) > 0 else 0
    )
})
missing_report = missing_report.sort_values(
    "missing_count", ascending=False
)
missing_report.to_csv(output_folder / "missing_values_report.csv", index=False)

# Check for duplicate facility IDs
if "facility_id" in df.columns:
    duplicate_ids = df[
        df["facility_id"].notna()
        & df["facility_id"].duplicated(keep=False)
    ].sort_values("facility_id")
    duplicate_ids.to_csv(
        output_folder / "duplicate_facility_ids.csv", index=False
    )

# Save a small project summary
summary = pd.DataFrame({
    "metric": [
        "Rows in original file",
        "Rows after removing empty rows",
        "Rows in cleaned file",
        "Duplicate rows removed",
        "Columns in cleaned file"
    ],
    "value": [
        original_rows,
        rows_after_empty_removal,
        cleaned_rows,
        rows_after_empty_removal - cleaned_rows,
        len(df.columns)
    ]
})
summary.to_csv(output_folder / "data_summary.csv", index=False)

print("Data cleaning and analysis completed.")
print("Original rows:", original_rows)
print("Cleaned rows:", cleaned_rows)
print("Columns:", len(df.columns))
print("Output folder:", output_folder)

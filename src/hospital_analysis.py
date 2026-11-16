from pathlib import Path
import pandas as pd

# Read the CMS file from the main project folder
input_file = Path("Hospital_General_Information_2.csv")
output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

df = pd.read_csv(input_file, dtype={"facility_id": "string"})

# Make column names consistent
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace("/", "_", regex=False)
)

# Clean text values
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

df = df.replace(r"^\s*$", pd.NA, regex=True)
df = df.dropna(how="all").drop_duplicates()

# Keep hospital IDs as text and convert rating to a number
if "facility_id" in df.columns:
    df["facility_id"] = df["facility_id"].astype("string").str.strip()

if "hospital_overall_rating" in df.columns:
    df["hospital_overall_rating"] = pd.to_numeric(
        df["hospital_overall_rating"], errors="coerce"
    )

# Save the cleaned dataset
df.to_csv(output_folder / "cleaned_hospitals.csv", index=False)

print("\nHOSPITAL PERFORMANCE & QUALITY ANALYTICS")
print("-----------------------------------------")
print("Total hospitals:", len(df))
print("Total columns:", len(df.columns))
print("Duplicate rows removed:", duplicates_removed)

# Hospitals by state
if "state" in df.columns:
    state_summary = (
        df.groupby("state", dropna=False)
        .size()
        .reset_index(name="hospital_count")
        .sort_values("hospital_count", ascending=False)
    )
    state_summary.to_csv(output_folder / "hospitals_by_state.csv", index=False)
    print("\nTop 10 states:")
    print(state_summary.head(10).to_string(index=False))

# Overall hospital ratings
if "hospital_overall_rating" in df.columns:
    rating_summary = (
        df["hospital_overall_rating"]
        .value_counts(dropna=False)
        .sort_index()
        .reset_index()
    )
    rating_summary.columns = ["overall_rating", "hospital_count"]
    rating_summary.to_csv(output_folder / "rating_distribution.csv", index=False)
    print("\nRating distribution:")
    print(rating_summary.to_string(index=False))

# Hospital type and ownership
for column in ["hospital_type", "hospital_ownership", "emergency_services"]:
    if column in df.columns:
        summary = (
            df[column].fillna("Not reported")
            .value_counts()
            .rename_axis(column)
            .reset_index(name="hospital_count")
        )
        summary.to_csv(output_folder / f"{column}_summary.csv", index=False)

# Missing values report
missing = pd.DataFrame({
    "column": df.columns,
    "missing_count": df.isna().sum().values,
    "missing_percent": (df.isna().mean().values * 100).round(2)
})
missing.to_csv(output_folder / "missing_values_report.csv", index=False)

print("\nAnalysis complete. Check the output folder for CSV reports.")

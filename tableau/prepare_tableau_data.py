import pandas as pd
from pathlib import Path

INPUT_FILE = "Hospital_General_Information_2.csv"
OUTPUT_DIR = Path("tableau_data")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(INPUT_FILE, dtype={"facility_id": "string"})
df.columns = df.columns.str.strip().str.lower()
df = df.replace(r"^\\s*$", pd.NA, regex=True)
df["facility_id"] = df["facility_id"].astype("string").str.strip()
df = df.dropna(how="all").drop_duplicates()

numeric_columns = [
    "hospital_overall_rating",
    "mort_group_measure_count", "count_of_facility_mort_measures",
    "count_of_mort_measures_better", "count_of_mort_measures_no_different",
    "count_of_mort_measures_worse", "safety_group_measure_count",
    "count_of_facility_safety_measures", "count_of_safety_measures_better",
    "count_of_safety_measures_no_different", "count_of_safety_measures_worse",
    "readm_group_measure_count", "count_of_facility_readm_measures",
    "count_of_readm_measures_better", "count_of_readm_measures_no_different",
    "count_of_readm_measures_worse", "pt_exp_group_measure_count",
    "count_of_facility_pt_exp_measures", "te_group_measure_count",
    "count_of_facility_te_measures"
]
for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_csv(OUTPUT_DIR / "cms_hospitals_clean.csv", index=False)

quality = pd.DataFrame({
    "column": df.columns,
    "non_null_count": df.notna().sum().values,
    "missing_count": df.isna().sum().values,
    "missing_percent": (df.isna().mean().values * 100).round(2)
})
quality.to_csv(OUTPUT_DIR / "field_completeness.csv", index=False)

if "state" in df.columns:
    df.groupby("state", dropna=False).agg(
        hospital_count=("facility_id", "nunique")
    ).reset_index().to_csv(OUTPUT_DIR / "hospitals_by_state.csv", index=False)

if "hospital_overall_rating" in df.columns:
    rated = df.dropna(subset=["hospital_overall_rating"])
    rating = rated.groupby("hospital_overall_rating").agg(
        hospital_count=("facility_id", "nunique")
    ).reset_index()
    rating["rated_hospital_denominator"] = rated["facility_id"].nunique()
    rating["percent_of_rated_hospitals"] = (
        rating["hospital_count"] / rating["rated_hospital_denominator"] * 100
    ).round(2)
    rating.to_csv(OUTPUT_DIR / "rating_distribution.csv", index=False)

for field, filename in [
    ("hospital_type", "hospital_type_mix.csv"),
    ("hospital_ownership", "hospital_ownership_mix.csv"),
    ("emergency_services", "emergency_services_mix.csv")
]:
    if field in df.columns:
        summary = df.groupby(field, dropna=False).agg(
            hospital_count=("facility_id", "nunique")
        ).reset_index()
        summary["all_hospital_denominator"] = df["facility_id"].nunique()
        summary["percent_of_hospitals"] = (
            summary["hospital_count"] / summary["all_hospital_denominator"] * 100
        ).round(2)
        summary.to_csv(OUTPUT_DIR / filename, index=False)

print("Tableau preparation complete. Rows:", len(df), "Columns:", len(df.columns))
print("Output folder:", OUTPUT_DIR.resolve())

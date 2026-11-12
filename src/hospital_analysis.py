import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create a folder for reports and charts
Path("output").mkdir(exist_ok=True)

# 1. Load the CMS hospital dataset
file_path = "Hospital_General_Information_2.csv"
df = pd.read_csv(file_path)

print("\nHOSPITAL PERFORMANCE & QUALITY ANALYTICS")
print("----------------------------------------")

# 2. Explore the dataset
print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nFirst 5 records:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

# 3. Check data quality
print("\nMissing values by column:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

missing_report = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values,
    "Missing Percentage": (df.isnull().mean().values * 100).round(2)
})

missing_report.to_csv("output/missing_values_report.csv", index=False)

# 4. Basic data cleaning
clean_df = df.copy()

clean_df.columns = clean_df.columns.str.strip()

for column in clean_df.select_dtypes(include="object").columns:
    clean_df[column] = clean_df[column].str.strip()

clean_df = clean_df.replace(r"^\s*$", pd.NA, regex=True)
clean_df = clean_df.dropna(how="all")
clean_df = clean_df.drop_duplicates()

print("\nRows before cleaning:", len(df))
print("Rows after cleaning:", len(clean_df))
print("Duplicate rows removed:", len(df) - len(df.drop_duplicates()))

clean_df.to_csv("output/cleaned_hospital_data.csv", index=False)

# 5. Hospital count by state
if "State" in clean_df.columns:
    state_counts = clean_df["State"].value_counts().reset_index()
    state_counts.columns = ["State", "Hospital Count"]

    print("\nHospitals by state (top 10):")
    print(state_counts.head(10))

    state_counts.to_csv("output/hospitals_by_state.csv", index=False)

    state_counts.head(10).plot(
        x="State",
        y="Hospital Count",
        kind="bar",
        legend=False,
        title="Top 10 States by Hospital Count"
    )
    plt.ylabel("Number of Hospitals")
    plt.tight_layout()
    plt.savefig("output/hospitals_by_state.png")
    plt.close()
else:
    print("\nState column not found; state analysis skipped.")

# 6. Hospital type distribution
if "Hospital Type" in clean_df.columns:
    type_counts = clean_df["Hospital Type"].value_counts()

    print("\nHospital type distribution:")
    print(type_counts)

    type_counts.to_csv("output/hospital_type_distribution.csv")

    type_counts.plot(kind="bar", title="Hospital Type Distribution")
    plt.xlabel("Hospital Type")
    plt.ylabel("Number of Hospitals")
    plt.tight_layout()
    plt.savefig("output/hospital_type_distribution.png")
    plt.close()
else:
    print("\nHospital Type column not found; type analysis skipped.")

# 7. Hospital ownership distribution
if "Hospital Ownership" in clean_df.columns:
    ownership_counts = clean_df["Hospital Ownership"].value_counts()

    print("\nHospital ownership distribution:")
    print(ownership_counts)

    ownership_counts.to_csv("output/hospital_ownership.csv")

    ownership_counts.plot(kind="bar", title="Hospital Ownership Distribution")
    plt.xlabel("Hospital Ownership")
    plt.ylabel("Number of Hospitals")
    plt.tight_layout()
    plt.savefig("output/hospital_ownership.png")
    plt.close()
else:
    print("\nHospital Ownership column not found; ownership analysis skipped.")

# 8. Overall hospital rating distribution
if "Hospital overall rating" in clean_df.columns:
    rating_counts = clean_df["Hospital overall rating"].value_counts()

    print("\nHospital overall rating distribution:")
    print(rating_counts)

    rating_counts.to_csv("output/hospital_rating_distribution.csv")

    rating_counts.plot(kind="bar", title="Hospital Overall Rating Distribution")
    plt.xlabel("Overall Rating")
    plt.ylabel("Number of Hospitals")
    plt.tight_layout()
    plt.savefig("output/hospital_rating_distribution.png")
    plt.close()
else:
    print("\nHospital overall rating column not found; rating analysis skipped.")

# 9. Final summary
print("\nPROJECT SUMMARY")
print("----------------")
print("Original rows:", len(df))
print("Cleaned rows:", len(clean_df))
print("Columns:", len(clean_df.columns))
print("\nAnalysis finished. Check the output folder for reports and charts.")

# Hospital Performance & Quality Analytics

A practical data analysis project using the U.S. Centers for Medicare & Medicaid Services (CMS) Hospital General Information dataset.

**Tools:** Python, pandas, SQL and Tableau

## Objective

Analyze hospital profiles across the United States, explore hospital ratings and ownership, review emergency-service availability, and assess the completeness and consistency of the source data.

## Dataset

- Source: [CMS Hospital General Information](https://data.cms.gov/provider-data/dataset/xubh-q36u)
- Dataset ID: `xubh-q36u`
- Source CSV included: `Hospital_General_Information_2.csv`
- The dataset contains hospital-level information, not patient-level records.

## Project structure

```
Hospital-Performance-Quality-Analytics/
├── Hospital_General_Information_2.csv
├── README.md
├── requirements.txt
├── src/
│   └── hospital_analysis.py
├── sql/
│   ├── README.md
│   └── hospital_analysis.sql
├── tableau/
│   ├── README.md
│   ├── TABLEAU_DASHBOARD_SPEC.md
│   ├── dashboard_guide.md
│   └── screenshots/
│       └── README.md
└── output/                 # created when the Python script runs
```

## 1. Python: data cleaning and analysis

Python is used to prepare the CMS file and create analysis-ready CSV outputs.

### Install

Run these commands from the main project folder:

```bash
python3 -m pip install -r requirements.txt
```

### Run

```bash
python3 src/hospital_analysis.py
```

### What the script does

- Checks that the source CSV exists.
- Standardizes column names.
- Removes extra spaces from text values.
- Converts empty text cells to missing values.
- Removes completely empty rows and duplicate records.
- Converts the overall hospital rating to a numeric field.
- Creates summaries by state, hospital rating, hospital type and ownership.
- Reports missing values and duplicate facility IDs.
- Saves a data summary and cleaned dataset.

### Files created in output/

- `cleaned_hospitals.csv`
- `hospitals_by_state.csv`
- `rating_distribution.csv`
- `hospitals_by_type.csv`
- `hospitals_by_ownership.csv`
- `missing_values_report.csv`
- `duplicate_facility_ids.csv`
- `data_summary.csv`

Some summary files are created only when the corresponding source column is present. The original CMS CSV is not overwritten.

## 2. SQL: business analysis

Import `output/cleaned_hospitals.csv` into your database as a table named `hospitals`. Keep `facility_id` as text and `hospital_overall_rating` numeric. Then run the queries in `sql/hospital_analysis.sql`.

The queries cover hospital counts, state distribution, hospital type, ownership, ratings, emergency services, missing ratings and duplicate facility IDs.

## 3. Tableau: dashboards

Connect Tableau to `output/cleaned_hospitals.csv` and build the dashboards described in `tableau/TABLEAU_DASHBOARD_SPEC.md`.

The planned dashboards are:
1. Hospital Overview
2. Hospital Ratings
3. Hospital Services
4. Data Quality

Add screenshots to `tableau/screenshots/` only after building and checking the dashboards in Tableau. The repository currently contains guidance, not completed Tableau screenshots.

## Data considerations

- Treat `facility_id` as an identifier, not a measure.
- Keep hospitals without an overall rating visible as a separate category.
- Show counts with percentages and clearly state the denominator.
- Check CMS definitions and reporting periods before comparing quality measures.
- This is descriptive analysis; it does not establish cause and effect.
- Review the source data dictionary before interpreting individual fields.

## Reproducibility

The source CSV is retained unchanged. Run the Python script to regenerate the cleaned dataset and summary files in the local `output/` folder. Generated outputs are not committed to the repository by default.

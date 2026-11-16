# Hospital Performance & Quality Analysis

A practical data analysis project using the U.S. Centers for Medicare & Medicaid Services (CMS) Hospital General Information dataset.

**Tools:** Python, pandas, Matplotlib and SQL

## Objective
Explore hospital profiles across the United States, compare hospital ratings and ownership categories, review emergency-service availability, and check data completeness.

## Dataset
- Source: [CMS Hospital General Information](https://data.cms.gov/provider-data/dataset/xubh-q36u)
- Dataset ID: `xubh-q36u`
- CSV included: `Hospital_General_Information_2.csv`
- This is hospital-level information, not patient-level data.

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
└── output/                 # created when Python script runs
    ├── cleaned_hospitals.csv
    ├── hospitals_by_state.csv
    ├── rating_distribution.csv
    ├── missing_values_report.csv
    └── charts/
```

## Python analysis

Install the libraries:

```bash
pip3 install -r requirements.txt
```

Run from the main project folder:

```bash
python3 src/hospital_analysis.py
```

The script:
- Reads and cleans the CMS CSV.
- Standardizes column names and removes duplicate rows.
- Converts the overall rating to a numeric field.
- Summarizes hospitals by state, rating, type and ownership.
- Checks missing values.
- Exports cleaned data, summary CSV files and simple charts.

Charts are saved in `output/charts/`. They are generated from the dataset when the script is run.

## SQL analysis

Import the CMS CSV into a database table named `hospitals`, keeping `facility_id` as text. Run `sql/hospital_analysis.sql`.

The queries cover hospital counts, state distribution, hospital type, ownership, ratings, emergency services and duplicate IDs.

## Data considerations
- Treat `facility_id` as an identifier, not a measure.
- Keep hospitals without an overall rating separate from rated hospitals.
- Show counts alongside percentages and state the denominator.
- Check CMS definitions and reporting periods before comparing quality measures.
- The analysis is descriptive and does not establish cause and effect.

## Project outputs
The CSV reports and charts are generated locally and are not committed to the repository. Run the script to reproduce them using the included dataset.

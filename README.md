# Hospital Performance & Quality Analytics

An independent Data Analyst portfolio project using the U.S. Centers for Medicare & Medicaid Services (CMS) Hospital General Information dataset.

**Tools:** Python, SQL, Tableau, Excel/CSV

## Business objective
Explore the U.S. hospital landscape and understand how hospital ratings, ownership, hospital type and emergency-service availability vary across states. Review the completeness of the published data before interpreting results.

## Dataset
- Source: [CMS Hospital General Information](https://data.cms.gov/provider-data/dataset/xubh-q36u)
- Dataset ID: `xubh-q36u`
- File in this repository: `Hospital_General_Information_2.csv`
- The dataset contains hospital-level information. It is not patient-level data.

## Project structure
```
Hospital-Performance-Quality-Analytics/
├── Hospital_General_Information_2.csv
├── README.md
├── requirements.txt
├── src/
│   └── hospital_analysis.py
├── output/
│   └── generated CSV reports (created when the script runs)
├── sql/
│   ├── README.md
│   └── hospital_analysis.sql
├── tableau/
│   ├── README.md
│   ├── TABLEAU_DASHBOARD_SPEC.md
│   ├── dashboard_guide.md
│   └── dashboard_overview.svg
└── docs/
    └── tableau_plan.md
```

## 1. Python analysis

Install the required library:

```bash
pip install -r requirements.txt
```

Run the script from the repository's main folder:

```bash
python src/hospital_analysis.py
```

The script:
- Loads the CMS CSV and standardizes column names.
- Removes blank rows and duplicate records.
- Keeps facility IDs as text.
- Converts hospital ratings to numeric values.
- Creates a cleaned CSV, state summary, rating summary, category summaries and missing-values report in the `output/` folder.

## 2. SQL analysis

Open `sql/hospital_analysis.sql` in SQLite, DB Browser for SQLite, MySQL or another SQL editor. Import the CMS CSV into a table named `hospitals` first. Keep `facility_id` as text.

The queries cover hospital counts, state distribution, hospital ownership, ratings, emergency services, missing values and duplicate facility IDs.

## 3. Tableau dashboard

Connect Tableau to the cleaned file `output/cleaned_hospitals.csv` after running the Python script.

Follow the [Tableau Dashboard Guide](tableau/dashboard_guide.md) and [Tableau Dashboard Specification](tableau/TABLEAU_DASHBOARD_SPEC.md) to build:
- Executive overview and KPI cards
- Hospital ratings and rating distribution
- Hospital type and ownership
- State-level hospital distribution
- Data completeness

The SVG in the Tableau folder is a layout preview, not a populated Tableau workbook. Publish a Tableau workbook only after building and validating the charts with the actual CSV.

## Important data notes
- Treat `facility_id` as a text identifier, not a numeric measure.
- Show the denominator when displaying percentages.
- Keep missing or not-reported ratings separate from actual rating values.
- Check CMS definitions and reporting periods before comparing quality measures.
- This is descriptive analysis; it does not establish that ownership or location causes a hospital to perform better or worse.

## Project status
Python code, SQL queries and Tableau dashboard instructions are provided. Run the Python script and build the Tableau workbook to generate and validate the final results.

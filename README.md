# Hospital Performance & Quality Analytics

An independent analytics project using publicly available, hospital-level data
published by the U.S. Centers for Medicare & Medicaid Services (CMS).

**Tools:** Python, SQL, Tableau

The project examines hospital profiles, quality-rating coverage, and variation
across geography, hospital type, and ownership. It is an independent portfolio
analysis, not commissioned by CMS or any hospital.

## Data source
- CMS Hospital General Information: https://data.cms.gov/provider-data/dataset/xubh-q36u
- CMS Provider Data: https://data.cms.gov/provider-data/datasets?theme%5B0%5D=Hospitals

Download the CSV from the official CMS dataset page and place it at:
data/raw/Hospital_General_Information_2.csv

The raw source file is not committed here by default. Follow the dataset's
current terms and repository size limits before publishing a copy.

## Repository layout
- data/raw/ — original CMS extract (local; not tracked by default)
- src/profile_cms_data.py — schema and data-quality profiling
- outputs/ — generated profiling reports (local)
- sql/ — SQL workflow and analysis queries
- docs/ — dashboard plan and methodology notes

## Run the first data check
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python src/profile_cms_data.py --input data/raw/Hospital_General_Information_2.csv

The script creates outputs/data_profile.json with actual row count, columns,
data types, likely identifiers, and duplicate count; and
outputs/missingness_report.csv with missing counts and percentages.

Provider identifiers are read as strings to preserve leading zeroes. The script
does not hard-code presumed row or column counts.

## Analysis plan
1. Validate schema, identifiers, duplicates, and missingness.
2. Clean and standardize fields while retaining an auditable raw extract.
3. Build SQL quality checks and descriptive aggregations from the observed schema.
4. Develop Tableau views for hospital profiles, rating distributions, and
   geographic/ownership comparisons where coverage supports them.
5. Document definitions, reporting periods, denominators, extraction date,
   and limitations.

## Interpretation notes
CMS hospital-level measures may have different reporting periods, denominators,
and eligibility rules. Do not compare measures without checking their definitions
in the relevant CMS data dictionary. This project is descriptive and does not
establish causal relationships or measure individual patient outcomes.

## Current status
Project setup and initial profiling script are in place. Empirical findings,
SQL outputs, and Tableau dashboards will be added only after validating the
actual CMS extract. No findings or performance figures are fabricated.

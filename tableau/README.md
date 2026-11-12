# Tableau assets — Hospital Performance & Quality Analytics

These project-specific assets follow the dashboard plan in `docs/tableau_plan.md`.

## Files
- [Dashboard specification](TABLEAU_DASHBOARD_SPEC.md): four dashboards, filters, KPI definitions, denominators and interpretation rules.
- [Data preparation script](prepare_tableau_data.py): prepares the CMS extract and exports Tableau-ready CSVs.
- [Dashboard layout preview](dashboard_overview.svg): visual wireframe with no invented metrics.

## Run the data preparation script
Keep `Hospital_General_Information_2.csv` in the same folder as the script, then run:

```bash
pip3 install pandas
python3 prepare_tableau_data.py
```

Connect Tableau to `tableau_data/cms_hospitals_clean.csv`.

## Data source
CMS Hospital General Information, dataset ID `xubh-q36u`:
https://data.cms.gov/provider-data/dataset/xubh-q36u

## Important status
This repository contains the dashboard design and data-preparation workflow, not a finished populated Tableau workbook. The CSV stored in the repository could not be read by the GitHub file connector during this build, so the actual extract has not been validated and no metrics or workbook results are being claimed. Build/publish the Tableau workbook after connecting the real CMS CSV and checking its fields.

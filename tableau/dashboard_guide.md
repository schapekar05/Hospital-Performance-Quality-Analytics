# Tableau Build Guide

## 1. Prepare the data
1. Run `python3 src/hospital_analysis.py` from the repository root.
2. In Tableau, connect to Text File.
3. Select `output/cleaned_hospitals.csv`.
4. Confirm `facility_id` is a string and `hospital_overall_rating` is numeric.
5. Check field names and data types before creating worksheets.

## 2. Build the worksheets
Create worksheets for:
- Hospital count by state
- Hospital count by hospital type
- Hospital ownership
- Overall rating distribution
- Rating mix by state
- Emergency services
- Missing values by field

Create KPI sheets for total hospitals, states covered, hospitals with a rating and rating coverage.

## 3. Assemble dashboards
Create four dashboards using the worksheet groups described in [TABLEAU_DASHBOARD_SPEC.md](TABLEAU_DASHBOARD_SPEC.md). Add relevant filters and make sure the charts respond to those filters.

## 4. Export screenshots
After checking the dashboard numbers against the Python summaries:
1. Open each dashboard in Tableau.
2. Export or capture the dashboard as a PNG.
3. Save the images in `tableau/screenshots/` using the filenames listed in [README.md](README.md).
4. Add the PNG files to GitHub.

Do not describe a dashboard as completed until it has been built and validated in Tableau.

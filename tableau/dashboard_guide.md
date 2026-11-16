# Tableau Dashboard Guide

## Data connection
1. Run `python src/hospital_analysis.py` from the repository root.
2. Open Tableau Public or Tableau Desktop.
3. Connect to Text File and select `output/cleaned_hospitals.csv`.
4. Confirm `facility_id` is a string and `hospital_overall_rating` is numeric.
5. Use the data pane to check the field names before building charts.

## Dashboard 1 — Hospital Overview
**KPI cards**
- Total hospitals: COUNTD(facility_id)
- States covered: COUNTD(state)
- Hospitals with rating: count of non-null hospital_overall_rating
- Rating coverage: hospitals with rating / total hospitals

**Visuals**
- Horizontal bar: hospital count by state (sort descending)
- Donut chart: hospital ownership mix
- Bar chart: hospitals by hospital type

## Dashboard 2 — Hospital Ratings
**Visuals**
- Bar chart: number of hospitals by overall rating (1–5)
- 100% stacked bar: rating distribution by state
- Highlight table: state against overall rating

**Important:** Keep null/not-rated hospitals separate. Rating percentages should use rated hospitals as the denominator, not all hospitals.

## Dashboard 3 — Hospital Services & Profile
**Visuals**
- Bar chart: hospitals by hospital type
- Stacked bar: emergency services (Yes / No / Not reported)
- Bar chart: ownership category by hospital count
- Filled map: hospital count by state (only if Tableau recognizes the state field correctly)

## Dashboard 4 — Data Quality
**Visuals**
- Bar chart: missing values by field
- KPI: total records
- KPI: duplicate facility IDs
- Table: fields, missing count and missing percentage

Use the Python-generated `output/missing_values_report.csv` for the completeness chart.

## Filters to add to all relevant dashboards
- State
- Hospital type
- Hospital ownership
- Emergency services

## Suggested layout
Place KPI cards across the top, two or three charts in the middle, and filters in a narrow side panel. Use consistent labels, readable tooltips and a clear title.

## Calculated fields
Create these calculated fields in Tableau:

**Rating Available**
```
IF ISNULL([hospital_overall_rating]) THEN "Not rated"
ELSE "Rated"
END
```

**Rating Coverage**
```
COUNTD(
    IF NOT ISNULL([hospital_overall_rating])
    THEN [facility_id]
    END
)
/
COUNTD([facility_id])
```

Format Rating Coverage as a percentage.

## Validation
- Compare Tableau's total hospital count with the Python output.
- Confirm that rating counts exclude null ratings.
- Display counts with percentages.
- Show the CMS dataset source and extraction date on the dashboard.
- Do not interpret descriptive patterns as causes of hospital performance.

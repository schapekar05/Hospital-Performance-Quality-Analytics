# Tableau Dashboard Specification

This is the planned dashboard structure for the CMS Hospital General Information dataset.

## Dashboard 1 — Hospital Overview
- KPI: total hospitals (distinct facility IDs)
- KPI: states covered
- KPI: hospitals with an overall rating
- Bar chart: hospital count by state
- Bar chart: hospital count by hospital type
- Donut chart: hospital ownership mix

## Dashboard 2 — Hospital Ratings
- Bar chart: hospitals by overall rating (1–5)
- Stacked bar chart: rating mix by state
- Highlight table: state and overall rating
- Keep hospitals without a reported rating separate from rated hospitals.

## Dashboard 3 — Hospital Services
- Bar chart: hospitals by hospital type
- Stacked bar chart: emergency services (Yes / No / Not reported)
- Bar chart: hospitals by ownership
- Optional state map showing hospital counts, after checking geographic roles.

## Dashboard 4 — Data Quality
- KPI: total records
- KPI: duplicate facility IDs
- Bar chart: missing values by field
- Table: field name, missing count and missing percentage

## Filters
Use state, hospital type, hospital ownership and emergency services where relevant.

## Validation
- Treat facility IDs as text.
- Use distinct facility IDs for hospital counts.
- Calculate rating percentages using rated hospitals as the denominator.
- Keep missing ratings separate from actual rating values.
- Display counts alongside percentages and include the CMS data source.

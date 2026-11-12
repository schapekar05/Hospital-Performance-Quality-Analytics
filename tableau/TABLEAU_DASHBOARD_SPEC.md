# Tableau Dashboard Build — Hospital Performance & Quality Analytics

This dashboard specification follows `docs/tableau_plan.md` and the CMS Hospital General Information dataset (dataset ID `xubh-q36u`).

## Data source and scope
- Source: CMS Hospital General Information (hospital-level aggregate/general information).
- Dataset page: https://data.cms.gov/provider-data/dataset/xubh-q36u
- Catalog schema: 38 columns, including `facility_id`, `facility_name`, `state`, `hospital_type`, `hospital_ownership`, `emergency_services`, `hospital_overall_rating`, and CMS group-measure fields.
- Treat `facility_id` as a text dimension/key, never as a measure.
- Display CMS release/last-modified date and the extract download date.
- This is not patient-level data.

## Dashboard 1 — Executive Overview
KPI tiles: distinct hospitals, states covered, hospitals with an overall rating, rating coverage.
Charts: hospital count by state; overall rating distribution with rated-hospital denominator; ownership mix.

## Dashboard 2 — Hospital Ratings
- Overall rating distribution (1–5 plus null/not rated separately).
- Rating mix by state (100% stacked bars; show rated denominator).
- Filters: State, Hospital Type, Hospital Ownership, Emergency Services.
- Do not rank individual hospitals or imply causality.

## Dashboard 3 — Hospital Profile
- Hospital count by hospital type.
- Hospital count by ownership.
- Emergency services yes/no/unknown mix.
- Optional state map only if Tableau recognizes state values as a geographic role.

## Dashboard 4 — Data Coverage
Show non-null count, missing count and missing percentage by field.
Measure-group coverage fields: `count_of_facility_mort_measures`, `count_of_facility_safety_measures`, `count_of_facility_readm_measures`, `count_of_facility_pt_exp_measures`, `count_of_facility_te_measures`.
Keep null, zero and footnoted/not-applicable values distinct.

## Global filters
`state`, `hospital_type`, `hospital_ownership`, `emergency_services` (if present).

## Denominators and interpretation
- Rating coverage denominator = all distinct hospitals in the filtered extract.
- Rating distribution denominator = hospitals with non-null overall rating in the filtered extract.
- Category percentages must show count and denominator.
- Do not combine measures across incompatible reporting periods.
- Descriptive association is not causation.

## Build sequence
1. Run `prepare_tableau_data.py` beside the CMS CSV.
2. Connect Tableau to `tableau_data/cms_hospitals_clean.csv`.
3. Build the four dashboards above.
4. Verify field names against the actual CSV before publishing.

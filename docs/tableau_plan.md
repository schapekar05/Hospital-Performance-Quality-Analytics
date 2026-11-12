# Tableau dashboard plan

Build the workbook from the validated, cleaned CMS hospital-level extract.

## Proposed views
1. Executive overview: hospital count, state coverage, rating coverage, ownership mix.
2. Hospital ratings: rating distribution and state comparisons.
3. Hospital profile: hospital type and ownership breakdown.
4. Data coverage: missingness by field and measure availability.

## Filters
- State
- Hospital type
- Hospital ownership
- Emergency services, if present in the extract

## Build standards
- Use provider ID as a text key, not a numeric measure.
- Display the reporting period and CMS extraction date.
- Show denominators beside percentages.
- Exclude null or not-applicable values from measure denominators.
- Do not imply descriptive associations are causal.
- Do not rank hospitals on measures with incompatible reporting periods or coverage.

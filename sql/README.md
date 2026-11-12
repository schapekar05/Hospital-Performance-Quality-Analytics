# SQL analysis workflow

The SQL layer will be built after the downloaded CMS CSV has been profiled.

Planned work:
1. Load the validated extract into a staging table.
2. Check provider-ID uniqueness, nulls, and duplicate records.
3. Aggregate hospital counts by state, ownership, and hospital type.
4. Analyze overall rating distributions only where populated.
5. Compare quality measures only after confirming their definitions and reporting periods.

Use the exact column names and types observed in outputs/data_profile.json.
Keep provider identifiers as text. Do not assume different measures share a
reporting period, denominator, or interpretation. No placeholder performance
figures are reported.

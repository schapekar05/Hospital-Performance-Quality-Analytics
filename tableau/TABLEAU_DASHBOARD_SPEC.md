# Tableau Dashboard Specification

This file describes the charts to build in Tableau. It is a build guide, not a finished workbook.

## 1. Hospital Overview
- KPI: total hospitals (distinct facility_id)
- KPI: states covered (distinct state)
- KPI: hospitals with an overall rating
- KPI: rating coverage
- Bar chart: hospital count by state
- Donut: hospital ownership mix
- Bar chart: hospital count by hospital type

## 2. Hospital Ratings
- Bar chart: overall rating distribution (1–5)
- 100% stacked bars: rating mix by state
- Highlight table: state and rating
- Keep unrated hospitals separate from rated hospitals.

## 3. Hospital Services & Profile
- Bar chart: hospital type
- Stacked bar: emergency services
- Bar chart: hospital ownership
- Filled map: hospital count by state, after validating geographic roles.

## 4. Data Quality
- Bar chart: missing values by column
- KPI: duplicate facility IDs
- Table: field name, missing count, missing percentage
- KPI: total records

## Filters
State, hospital type, hospital ownership and emergency services.

## Design
Use a clean healthcare-style layout, consistent chart titles, readable labels, informative tooltips and visible data-source notes. Put KPI cards at the top and filters to the side.

## Data interpretation
Use distinct facility IDs for hospital counts. Rating distribution uses rated hospitals as its denominator; rating coverage uses all hospitals. Do not imply causation or compare measure groups without checking CMS definitions and reporting periods.

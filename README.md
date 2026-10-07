# Austrian Energy Data Engine

A data engineering and analytics project using real Austrian electricity-market data from the [Open Power System Data (OPSD)](https://open-power-system-data.org/) time-series dataset.

The goal is to build a reproducible pipeline that transforms raw hourly energy data into a clean, queryable dataset for analysis. The project covers **Python-based data cleaning, PostgreSQL data engineering, SQL analytics, and Power BI visualization**.

## Current Progress

The raw dataset contains 50,401 hourly observations across 300 columns. The project currently focuses on **six selected columns: one timestamp and five Austrian energy variables**:

* `timestamp_utc` — UTC observation timestamp
* `actual_load_mw` — actual electricity demand
* `forecast_load_mw` — forecast electricity demand
* `day_ahead_price_eur` — day-ahead electricity price
* `solar_actual_mw` — actual solar generation
* `wind_actual_mw` — actual onshore wind generation

So far, I have:

* Explored the structure and quality of the raw dataset
* Isolated the relevant Austrian data
* Investigated missing-value patterns and data availability
* Built the initial Python data-cleaning pipeline
* Standardized column names and timestamps
* Investigated the structure of gaps in the solar and wind time series

The project is currently in the **data cleaning and validation stage**. Missing values are being investigated before deciding how they should be handled rather than applying automatic imputation.

## Planned Pipeline

```text
Raw Energy Data
      ↓
Python Cleaning & Validation
      ↓
Processed Dataset
      ↓
PostgreSQL
      ↓
SQL Analysis
      ↓
Power BI Dashboard
```

The final analysis will investigate Austrian electricity demand, renewable generation, load forecasting, and electricity prices where sufficient data is available.

## Tech Stack

**Python · Pandas · NumPy · PostgreSQL · SQL · Power BI · Git**

## Status

🚧 **Work in progress** — data exploration and cleaning underway.

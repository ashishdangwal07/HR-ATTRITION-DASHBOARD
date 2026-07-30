# HR Attrition Dashboard

## Executive Summary
This repository presents a professional HR attrition analysis based on 1,470 employee records. The project identifies the primary drivers of employee turnover and translates the findings into clear, business-ready insights for HR and leadership teams.

## Why This Project Matters
Attrition affects workforce stability, recruiting cost, and team performance. This analysis explores department-level risk, role-specific turnover, compensation patterns, and workload-related factors to support stronger retention strategies.

## Key Insights
- Overall attrition rate: 16.1%
- Highest-risk department: Sales at approximately 20.6%
- Elevated turnover also appears in Human Resources at about 19.0%
- Research & Development remains comparatively more stable at about 13.8%
- Employees who leave earn less on average than those who stay
- Overtime is strongly associated with higher turnover risk

## What’s Included
- Raw employee dataset for analysis
- Cleaned Excel workbook for structured review
- Power BI dashboard package for visualization
- Executive summary for business stakeholders

## Repository Files
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) — concise executive summary of the analysis
- [HR_CLEANED_DATA.xlsx](HR_CLEANED_DATA.xlsx) — cleaned Excel workbook
- [HR_Attrition_Dashboard_pbix.zip](HR_Attrition_Dashboard_pbix.zip) — Power BI dashboard file
- [WA_Fn-UseC_-HR-Employee-Attrition.csv](WA_Fn-UseC_-HR-Employee-Attrition.csv) — raw dataset

## Recommended Actions
1. Review compensation and retention practices in Sales and HR.
2. Reduce excessive overtime in high-risk teams.
3. Investigate role-specific turnover concerns, especially for Sales Representatives and Laboratory Technicians.
4. Monitor attrition trends regularly using the dashboard to evaluate progress.

## Tools and Workflow
- Data preparation and exploratory analysis
- Excel-based cleaning and review
- Power BI for dashboard visualization
- Markdown documentation for clear project communication

## Run the Analysis
From the project folder, run:
- `python analysis.py` to generate the summary report
- `python -m unittest discover -s tests -v` to run the automated checks

The analysis output is written to the outputs folder as a text report.

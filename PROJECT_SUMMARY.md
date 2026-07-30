# HR Attrition Dashboard Project

## Overview
This project analyzes employee attrition using a structured HR dataset containing 1,470 employee records. The objective is to identify the strongest patterns behind turnover and present the findings in a format that is useful for both business leaders and HR stakeholders.

## Business Objective
The analysis helps answer the following questions:
- Which departments experience the highest attrition?
- Which job roles are most at risk of turnover?
- How do compensation and workload influence employee exits?
- What practical recommendations can reduce turnover?

## Dataset
- Source file: WA_Fn-UseC_-HR-Employee-Attrition.csv
- Records analyzed: 1,470
- Key attributes include department, role, monthly income, overtime status, age, and attrition outcome

## Key Insights
- Overall attrition rate: 16.1%
- Highest-risk department: Sales (20.6% attrition)
- Elevated turnover also appears in Human Resources (19.0%)
- Research & Development is comparatively more stable (13.8%)
- Employees who leave earn less on average than those who stay
- Overtime is strongly associated with higher turnover risk

## Recommended Actions
1. Review compensation and reward practices in Sales and HR.
2. Reduce excessive overtime pressure in high-risk teams.
3. Investigate role-specific retention concerns, especially for Sales Representatives and Laboratory Technicians.
4. Use the Power BI dashboard to monitor turnover trends over time.

## Project Files
- README.md — main project overview and narrative summary
- analysis.py — reproducible analysis workflow
- tests/test_analysis.py — automated verification checks
- HR_CLEANED_DATA.xlsx — cleaned Excel workbook
- HR_Attrition_Dashboard_pbix.zip — Power BI dashboard file
- WA_Fn-UseC_-HR-Employee-Attrition.csv — raw dataset

## Run Instructions
- Run `python analysis.py` to produce the summary report
- Run `python -m unittest discover -s tests -v` to verify the analysis

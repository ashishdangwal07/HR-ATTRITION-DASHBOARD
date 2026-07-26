# HR Attrition Analysis
## What This Is

Looked at 1,470 employees to figure out why people are leaving. Company losing about 237 people per year - that's 16%. Wanted to see which departments are bleeding people, which roles have it worst, and if it's money or just bad management.

## The Data

1,470 employee records. 237 quit. Looked at department, role, salary, age, how long they've been here, if they work overtime, job satisfaction scores. Basic HR stuff.

## What I Found

Sales department loses people the fastest - about 1 in 5 quit. HR loses about 1 in 5 too. R&D is more stable, only losing like 14% which is still high but better.

People who leave are younger (average 33 vs 37 for people who stay). They're paid less too - leaving employees made around 4.7L while stayers made 6.8L. Overtime kills it - if you're working extra hours, way more likely to bounce.

Lab Techs leave a lot. Sales Reps even more. 

The pattern is clear - pay people more and don't kill them with overtime, they stay. Seems obvious but the numbers back it up.

## Files

**hr_attrition_dashboard_reference.html** - Open this in browser. It's the Power BI dashboard. All the charts and filters are there.

**HR_CLEANED_DATA.xlsx** - Cleaned data with pivot tables. Department breakdown, salary analysis, all that.

**WA_Fn-UseC_-HR-Employee-Attrition.csv** - Raw data file. 1,470 rows.

**HR_Attrition_Dashboard_pbix.zip** - Actual Power BI file if you want to mess with it. Has all 9 charts, slicers for department/gender/overtime.

## How I Built This

Pulled the CSV into Python, used Pandas to group by department, role, salary ranges. Calculated percentages. Then built it all out in Power BI - made KPI cards, some bar charts showing which roles are risky, line chart to see the age trend, pie chart for gender split.

## Real Talk

Sales is the problem department. Either fix compensation there or fix the work culture because you're losing 1 out of every 5 people. R&D has it figured out somehow - way lower attrition. So either copy what they're doing or just pay Sales people more.

Overtime is evil for retention. People working extra hours are way more likely to leave. That's worth fixing.

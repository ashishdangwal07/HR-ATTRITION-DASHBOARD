import csv
import os
from collections import Counter
from statistics import mean


def load_dataset(path):
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader)


def compute_summary(rows):
    total_employees = len(rows)
    attrition_rate = round(sum(1 for row in rows if row["Attrition"] == "Yes") / total_employees * 100, 2)

    department_counts = Counter(row["Department"] for row in rows)
    department_attrition = Counter(row["Department"] for row in rows if row["Attrition"] == "Yes")
    department_rates = {
        dept: round(department_attrition[dept] / department_counts[dept] * 100, 1)
        for dept in department_counts
    }

    role_counts = Counter(row["JobRole"] for row in rows)
    role_attrition = Counter(row["JobRole"] for row in rows if row["Attrition"] == "Yes")
    top_roles = [
        (role, round(role_attrition[role] / role_counts[role] * 100, 1))
        for role in role_counts
    ]
    top_roles = sorted(top_roles, key=lambda item: item[1], reverse=True)[:5]

    monthly_income_leavers = [float(row["MonthlyIncome"]) for row in rows if row["Attrition"] == "Yes"]
    monthly_income_stayers = [float(row["MonthlyIncome"]) for row in rows if row["Attrition"] == "No"]

    overtime_leavers = sum(1 for row in rows if row["OverTime"] == "Yes" and row["Attrition"] == "Yes")
    overtime_total = sum(1 for row in rows if row["OverTime"] == "Yes")
    overtime_attrition_rate = round(overtime_leavers / overtime_total * 100, 1) if overtime_total else 0.0

    return {
        "total_employees": total_employees,
        "attrition_rate": attrition_rate,
        "department_attrition": department_rates,
        "top_roles": top_roles,
        "avg_income_leavers": round(mean(monthly_income_leavers), 2),
        "avg_income_stayers": round(mean(monthly_income_stayers), 2),
        "overtime_attrition_rate": overtime_attrition_rate,
    }


def write_summary(summary, output_path="outputs/attrition_summary.txt"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write("HR Attrition Summary\n")
        handle.write("=" * 24 + "\n")
        handle.write(f"Total Employees: {summary['total_employees']}\n")
        handle.write(f"Overall Attrition Rate: {summary['attrition_rate']}%\n")
        handle.write("Department Attrition Rates:\n")
        for department, rate in summary["department_attrition"].items():
            handle.write(f"- {department}: {rate}%\n")
        handle.write("Top Risk Roles:\n")
        for role, rate in summary["top_roles"]:
            handle.write(f"- {role}: {rate}%\n")
        handle.write(f"Avg Income (Leavers): {summary['avg_income_leavers']}\n")
        handle.write(f"Avg Income (Stayers): {summary['avg_income_stayers']}\n")
        handle.write(f"Overtime Attrition Rate: {summary['overtime_attrition_rate']}%\n")
    return output_path


def main():
    data_path = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
    rows = load_dataset(data_path)
    summary = compute_summary(rows)
    print("HR Attrition Summary")
    print("=" * 24)
    print(f"Total Employees: {summary['total_employees']}")
    print(f"Overall Attrition Rate: {summary['attrition_rate']}%")
    print("Department Attrition Rates:")
    for department, rate in summary["department_attrition"].items():
        print(f"- {department}: {rate}%")
    print("Top Risk Roles:")
    for role, rate in summary["top_roles"]:
        print(f"- {role}: {rate}%")
    print(f"Avg Income (Leavers): {summary['avg_income_leavers']}")
    print(f"Avg Income (Stayers): {summary['avg_income_stayers']}")
    print(f"Overtime Attrition Rate: {summary['overtime_attrition_rate']}%")

    output_path = write_summary(summary)
    print(f"Report saved to {output_path}")


if __name__ == "__main__":
    main()

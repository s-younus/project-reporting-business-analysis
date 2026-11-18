"""Offline practice case. Python 3 standard library only. Run from any directory."""
import csv
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AS_OF = "2026-11-17"

def read(name):
    with (ROOT / "data" / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def classify(rows, project_ids):
    """Keep first occurrence of an ID; flag every later occurrence for review."""
    seen, accepted, issues = set(), [], []
    for row in rows:
        reason = None
        if row["expense_id"] in seen:
            reason = "Duplicate expense ID"
        elif not row["project_id"]:
            reason = "Missing project ID"
        elif row["project_id"] not in project_ids:
            reason = "Unknown project ID"
        elif int(row["amount_cents"]) <= 0:
            reason = "Nonpositive amount"
        elif row["status"] != "Approved":
            reason = "Not approved"
        elif row["expense_date"] > AS_OF:
            reason = "After reporting date"
        seen.add(row["expense_id"])
        if reason:
            issues.append(dict(row, reason=reason))
        else:
            accepted.append(row)
    return accepted, issues

def write_csv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def run():
    projects, raw = read("projects.csv"), read("expenses.csv")
    valid, issues = classify(raw, {p["project_id"] for p in projects})
    out = ROOT / "output"
    out.mkdir(exist_ok=True)
    db = sqlite3.connect(out / "reporting.sqlite")
    db.row_factory = sqlite3.Row
    db.executescript((ROOT / "schema.sql").read_text())
    db.executemany("INSERT INTO projects VALUES (?,?,?,?,?,?,?)", [
        (p["project_id"], p["project_name"], p["manager"], int(p["budget_cents"]),
         p["due_date"], p["status"], p["completion_date"] or None) for p in projects])
    db.executemany("INSERT INTO expenses VALUES (?,?,?,?,?)", [
        (r["expense_id"],r["project_id"],int(r["amount_cents"]),r["expense_date"],r["status"]) for r in valid])
    report = [dict(r) for r in db.execute((ROOT / "analysis.sql").read_text(), {"as_of": AS_OF})]
    db.commit()
    db.close()
    write_csv(out / "project_report.csv", report, list(report[0]))
    write_csv(out / "data_quality_issues.csv", issues, list(raw[0]) + ["reason"])
    metrics = {
        "as_of": AS_OF, "raw_expense_rows": len(raw), "accepted_rows": len(valid),
        "excluded_rows": len(issues), "budget_cents": sum(r["budget_cents"] for r in report),
        "actual_cents": sum(r["actual_cents"] for r in report),
        "over_budget_projects": sum(r["over_budget"] for r in report),
        "overdue_projects": sum(r["overdue"] for r in report)
    }
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2))
    template = (ROOT / "dashboard_template.html").read_text()
    (ROOT / "dashboard.html").write_text(template.replace("__PROJECT_DATA__", json.dumps(report)).replace("__METRICS__", json.dumps(metrics)))
    return report, issues, metrics

if __name__ == "__main__":
    print(json.dumps(run()[2], indent=2))

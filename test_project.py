"""Executable data and business-rule verification; not stakeholder UAT approval."""
import json
from run_project import run, classify

report, issues, metrics = run()
p = {r["project_id"]: r for r in report}
checks = [
 ("T01", "P001 actual equals CAD 12000", p["P001"]["actual_cents"] == 1200000),
 ("T02", "P001 variance equals CAD 2000", p["P001"]["variance_cents"] == 200000),
 ("T03", "Over budget project count is 2", metrics["over_budget_projects"] == 2),
 ("T04", "Overdue project count is 2", metrics["overdue_projects"] == 2),
 ("T05", "Due today is not overdue", p["P004"]["overdue"] == 0),
 ("T06", "Completed project is not overdue", p["P003"]["overdue"] == 0),
 ("T07", "Zero expense project is retained", p["P006"]["actual_cents"] == 0),
 ("T08", "Exactly at budget is not over budget", p["P004"]["over_budget"] == 0),
 ("T09", "Total actual is CAD 55000", metrics["actual_cents"] == 5500000),
 ("T10", "Raw rows reconcile to accepted and excluded", metrics["raw_expense_rows"] == 13 and metrics["accepted_rows"] == 7 and metrics["excluded_rows"] == 6),
]
for n, reason in enumerate(["Duplicate expense ID","Missing project ID","Unknown project ID","Nonpositive amount","Not approved","After reporting date"], 11):
    checks.append((f"T{n:02}", reason + " quarantined", sum(r["reason"] == reason for r in issues) == 1))
# Demonstrate the LEFT JOIN regression and verify the correction.
checks.append(("T17", "All six master projects retained", len(report) == 6))
results = [{"id": i, "check": d, "result": "PASS" if ok else "FAIL"} for i,d,ok in checks]
from run_project import ROOT
(ROOT / "output" / "test_results.json").write_text(json.dumps(results, indent=2))
for r in results:
    print(r["id"], r["result"], r["check"])
assert all(ok for _,_,ok in checks), "A business-rule test failed"

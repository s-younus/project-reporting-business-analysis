# Project Reporting System Enhancement

An AI-assisted independent Business Systems Analyst practice case using fictional stakeholders and synthetic project data. This is a working learning package, not evidence of paid client delivery or stakeholder approval.

## Start here

1. Extract the complete ZIP into a folder.
2. Open **dashboard.html** in a browser. It works offline without installing anything.
3. Read **docs/CASE_STUDY.md** for the business problem, requirements, stories, rules, system impacts, and delivery plan.
4. Read **docs/LEARNING_GUIDE.md** and complete the exercises yourself.
5. To reproduce the outputs, install or use an existing Python 3 interpreter, open a terminal in this folder, and run:

   python run_project.py

   python test_project.py

The scripts use only the Python standard library. They rebuild the SQLite database, CSV reports, dashboard, metrics, and test results from the included CSV sources. Existing generated outputs are overwritten. No network access is required.

## Package contents

| File | Purpose |
| --- | --- |
| data/projects.csv | Six fictional master projects |
| data/expenses.csv | Thirteen synthetic expense rows with six intentional exceptions |
| docs/CASE_STUDY.md | Business analysis portfolio documentation |
| docs/LEARNING_GUIDE.md | Guided practice and interview preparation |
| docs/DATA_DICTIONARY.md | Fields, formats, and data quality rules |
| docs/MANUAL_UAT.csv | Dashboard acceptance checks awaiting your execution |
| docs/BACKLOG.csv | Importable practice backlog; not a configured Jira board |
| schema.sql | SQLite table definitions |
| analysis.sql | Aggregation and business-rule logic |
| run_project.py | Reproducible data validation and reporting |
| test_project.py | Executable business-rule checks |
| dashboard.html | Generated interactive offline dashboard |
| output/project_report.csv | Clean project-level report |
| output/data_quality_issues.csv | Excluded records and reasons |
| output/reporting.sqlite | Generated analysis database |
| output/metrics.json | Computed reporting totals |
| output/test_results.json | Actual automated execution results |

## Expected results

As of November 17, 2026: CAD 70,000 total budget; CAD 55,000 eligible spending; two over-budget projects; two overdue projects. Seven of thirteen expense rows are accepted. Six are excluded for review. These are dataset results, not business improvements.


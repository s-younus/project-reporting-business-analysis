# Data dictionary

All records are synthetic. Currency is CAD. Reporting date is November 17, 2026. Dates use YYYY-MM-DD; monetary fields store integer cents.

| File | Field | Meaning and constraint |
| --- | --- | --- |
| projects.csv | project_id | Unique project key, required |
| projects.csv | project_name | Descriptive name, required |
| projects.csv | manager | Fictional manager name, required |
| projects.csv | budget_cents | Approved budget in CAD cents, positive integer |
| projects.csv | due_date | Planned completion date |
| projects.csv | status | Descriptive current label |
| projects.csv | completion_date | Actual completion date; blank if not completed |
| expenses.csv | expense_id | Source transaction identifier; repeated values trigger review |
| expenses.csv | project_id | Reference to project master |
| expenses.csv | amount_cents | Positive CAD cents; zero and negative excluded in this prototype |
| expenses.csv | expense_date | Date expense was recorded |
| expenses.csv | status | Approved is eligible; other statuses excluded |
| project_report.csv | actual_cents | Sum of accepted approved spending through reporting date |
| project_report.csv | variance_cents | Actual minus budget; positive means overspend |
| project_report.csv | over_budget | 1 when actual exceeds budget, otherwise 0 |
| project_report.csv | overdue | 1 when due date passed and not completed by reporting date |
| data_quality_issues.csv | reason | First applicable exclusion reason |

Project names come from the master table rather than being joined as text. This avoids relying on inconsistent name spellings in transactional data.

Duplicate handling uses file order, not a timestamp or a latest-version rule. Conflicting duplicates need source-owner review. This is a deliberate prototype limitation.

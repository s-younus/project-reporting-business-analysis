# Project Reporting System Enhancement

## Purpose and context

This independent practice case demonstrates how a Business Systems Analyst can translate a reporting problem into requirements, implementation rules, and validation evidence. All company details, stakeholders, interviews, and decisions below are simulated. Documentation and code were generated with AI assistance; the learner should review and adapt them.

A fictional mechanical and electrical contractor combines project and expense spreadsheets into a weekly management report. Duplicate expenses and invalid project references can distort totals. The proposed pilot validates incoming data and provides a project dashboard that flags spending and schedule concerns.

## Problem and business objective

Managers need consistent budget and expense totals and a clear view of overdue work. The pilot must reconcile every input expense row to an accepted or excluded result and calculate project flags using documented rules. No baseline preparation-time measurement exists, so efficiency gains cannot be claimed.

## Scope

Included: six synthetic projects, thirteen expense rows, approved spending, project-level variance, overdue flags, a review file, manager and attention filters, and reproducible SQL analysis.

Excluded: accounting writeback, invoice payment, authentication, live APIs, scheduled refresh, enterprise deployment, budget revisions, taxes, multiple currencies, credits/refunds, and predictive analytics. Those exclusions keep this a small prototype.

## Stakeholders and simulated discovery

| Role | Discovery question | Assumed answer for this case |
| --- | --- | --- |
| Project manager | What decisions must the report support? | Identify projects requiring budget or schedule review |
| Finance | What counts as actual spending? | Approved positive expenses dated on or before the reporting date |
| Finance | How is a duplicate identified? | Repeated expense ID; retain the first occurrence and review later rows |
| Reporting analyst | What happens to invalid rows? | Exclude them from totals and export the original values with a reason |
| Management | How is overdue defined? | Due date has passed and project was not completed by the reporting date |
| Technical team | Where does the pilot run? | Local CSV inputs, Python validation, SQLite analysis, offline HTML output |

These are explicit assumptions, not actual interview findings. In a real project the analyst would confirm them with stakeholders before implementation.

## Business requirements

| ID | Requirement | Priority | Evidence |
| --- | --- | --- | --- |
| BR01 | Show consistent budget and actual costs for every project | Must | Report CSV and totals checks |
| BR02 | Identify over-budget and overdue projects | Must | Flag checks and dashboard |
| BR03 | Account for every incoming expense row | Must | Accepted/excluded reconciliation and issue CSV |
| BR04 | Let managers narrow the view to relevant projects | Should | Manual dashboard UAT |
| BR05 | Make calculations reproducible and understandable | Must | SQL, data dictionary, test output |

## Functional requirements and traceability

| ID | Functional requirement | Business link | Story | Test |
| --- | --- | --- | --- | --- |
| FR01 | Aggregate valid approved expenses per project through reporting date | BR01 | US01 | T01 T09 |
| FR02 | Retain projects with no accepted expenses and show zero actual | BR01 | US01 | T07 T17 |
| FR03 | Calculate variance as actual minus budget | BR01 | US02 | T02 |
| FR04 | Flag over budget only when actual exceeds budget | BR02 | US02 | T03 T08 |
| FR05 | Flag overdue using due date and completion date as of report date | BR02 | US03 | T04 T05 T06 |
| FR06 | Quarantine invalid and out-of-scope expenses with one primary reason | BR03 | US04 | T10 T11 T12 T13 T14 T15 T16 |
| FR07 | Filter table and KPI cards by manager and attention status | BR04 | US05 | U01 U02 U03 U04 |
| FR08 | Display reporting date and dataset-wide quality counts | BR05 | US04 | U05 |

## User stories and acceptance criteria

### US01 View project spending

As a project manager, I want budget and eligible actual spending for each project so that I can review cost performance.

- Given P001 has eligible expenses of CAD 7,000 and CAD 5,000, when reporting runs, then actual spending is CAD 12,000.
- Given P006 has no expenses, then it remains visible with actual spending of CAD 0.
- Budget and actual values are displayed in CAD.

### US02 Identify overspending

As a project manager, I want a variance and budget flag so that I can identify overspending.

- Given budget CAD 10,000 and actual CAD 12,000, then variance is positive CAD 2,000 and the project is flagged.
- Given budget and actual both CAD 8,000, then variance is zero and the project is not flagged.
- With all projects selected, exactly two projects are over budget.

### US03 Identify overdue work

As a manager, I want overdue projects highlighted so that I can investigate schedule issues.

- Given due date November 10 and no completion date, then the project is overdue on November 17.
- Given due date November 17, then the project is not overdue on November 17.
- Given completion date October 30 and due date October 31, then the project is not overdue on November 17.

### US04 Review excluded expenses

As a reporting analyst, I want excluded rows with reasons so that I can investigate data issues before correcting the source.

- Thirteen source rows reconcile to seven accepted and six excluded rows.
- Each excluded row retains its source fields and one primary reason.
- Excluded records never contribute to actual spending.
- Review-file corrections do not update the source automatically.

### US05 Filter the report

As a project manager, I want to filter projects so that I can focus on the work I manage.

- Selecting Aisha Khan shows P001 and P003, budget CAD 25,000, actual CAD 26,000, one over-budget and one overdue project.
- Selecting Over budget as well shows only P001, budget CAD 10,000 and actual CAD 12,000.
- Reset returns all six projects and all-project KPI values.
- A selection with no matches displays a clear message and zero KPI values.

## Business rules

| ID | Rule |
| --- | --- |
| R01 | Reporting date is fixed at 2026-11-17 for reproducibility |
| R02 | All monetary source values are integer CAD cents, avoiding floating-point aggregation errors |
| R03 | Each project has a unique ID and positive budget |
| R04 | First expense ID occurrence wins; subsequent occurrences are excluded even if the first row is invalid |
| R05 | Validation order is duplicate ID, missing project ID, unknown project ID, nonpositive amount, approval, reporting date |
| R06 | Only the first applicable exclusion reason is recorded for a row |
| R07 | Approved expenses on or before the reporting date are eligible after other checks pass |
| R08 | Actual equals sum of eligible amounts; variance equals actual minus budget |
| R09 | Over budget means actual strictly greater than budget |
| R10 | Overdue means due date strictly before reporting date and completion is absent or after reporting date |
| R11 | Project status is descriptive; completion date determines whether completion occurred by the reporting date |
| R12 | All dashboard KPI cards use the same selected project subset as the table |

The prototype assumes valid ISO dates, integer amounts, and valid project master data. Malformed files fail the run rather than being silently repaired. A production ingestion process would need schema validation, audit history, ownership, and exception escalation.

## Current and proposed process

Current simulated process: collect spreadsheets, manually combine entries, inspect totals, correct visible errors, distribute a static report.

Proposed process: preserve source CSVs, validate each expense, export excluded rows for review, load accepted data into SQLite, aggregate by project with a LEFT JOIN, generate a dashboard and report, execute checks, review exceptions with the source owner.

## System interactions and impact analysis

| Component | Change | Dependency or impact | Mitigation |
| --- | --- | --- | --- |
| Project master CSV | Supplies IDs, budgets, managers and dates | Invalid master data affects every downstream result | Check master uniqueness and formats before extending dataset |
| Expense CSV | Supplies cost records | Duplicate IDs and approval timing affect totals | Document first-occurrence rule and preserve source order |
| Validation layer | Accepts or excludes rows | Finance needs visibility of excluded amounts | Export original rows and reason |
| SQLite | Stores accepted expenses and master projects | INNER JOIN would omit zero-expense projects | Use LEFT JOIN and zero-expense regression check |
| Dashboard and report | Presents calculated KPIs | Inconsistent filter behavior could mislead managers | Update cards and table from the same subset |
| Finance review | Resolves exceptions | Corrections must occur in source, followed by rerun | No automatic writeback |

Data flows in one direction from CSV files to validation, SQLite aggregation, and reporting outputs. The exception file branches from validation. No APIs or microservices are implemented.

## Delivery plan and priorities

Practice iteration 1: confirm scope and assumed rules; inspect source data; implement validation and basic reporting; execute automated checks.

Practice iteration 2: generate dashboard; run manual acceptance checks; resolve findings; document handover. These are proposed learning iterations, not completed Agile ceremonies.

Dependencies: US01 relies on project and expense inputs and validation; US02 and US03 rely on US01; US05 relies on the generated report. US04 must be ready before trusting totals.

The CSV backlog contains stories with priorities and statuses. Import it into a practice tracker if desired, mapping Summary, Description, Issue Type, and Priority. Import behavior depends on the target tracker; a CSV is not evidence of professional Jira use.

## Defect analysis example

DEF01 is an illustrative regression exercise, not a real historical production defect.

- Trigger: replace LEFT JOIN with INNER JOIN in a copy of analysis.sql and rerun.
- Expected: all six master projects appear, including P006 with zero actual.
- Faulty result: P006 disappears; total project count falls to five.
- Root cause: INNER JOIN requires a matching accepted expense.
- Correction: restore LEFT JOIN with COALESCE.
- Verification: T07 and T17 pass after the correction. Preserve your own before-and-after evidence if you execute the exercise.

## Validation and approvals

Executed automated checks are recorded in output/test_results.json. They validate data reconciliation, exclusions, totals, flags, and boundary cases. Manual dashboard checks are provided in MANUAL_UAT.csv and start as Not run. Automated checks do not imply human UAT approval.

Business owner approval: not obtained, simulated case. Finance rule approval: not obtained. Production release: not applicable. No signatures or approvals are fabricated.

## AI assistance and review

AI helped draft requirements, code, sample data, and tests. The package was executed to check numerical outputs. Before portfolio use, the learner should compare every rule with its SQL or Python implementation, manually test dashboard filters, and record any changes. Only synthetic data is included. No claim of real financial-services compliance is made.

## Findings and limitations

The dataset demonstrates CAD 70,000 budget and CAD 55,000 eligible actual spending. P001 and P005 are over budget and overdue. Six expenses require review or are outside the reporting scope. These are synthetic observations.

This prototype does not prove enterprise security, real stakeholder facilitation, production integration, or five years of systems analysis experience. It can support a practical discussion of requirements, traceability, data quality, SQL, and testing.

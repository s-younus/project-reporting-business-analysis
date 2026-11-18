# Learning and portfolio guide

## First session

Open dashboard.html. Find P001 and explain why CAD 12,000 actual against CAD 10,000 budget creates a positive CAD 2,000 variance. Select Aisha Khan and confirm that the cards change along with the table. Read US01 and US02 in CASE_STUDY.md and connect each acceptance criterion to a displayed value.

## Second session

Open both source CSV files in Excel. Treat amount_cents as cents: divide by 100 when displaying CAD. Identify the six intentionally excluded expense rows before opening output/data_quality_issues.csv. Explain why the duplicate E002 would inflate spending by CAD 5,000 if included. Explain why an approved future expense is excluded from this reporting date.

## Third session

Read analysis.sql line by line. Explain SELECT, LEFT JOIN, GROUP BY, SUM, COALESCE, and CASE using the dataset. Run the project and tests if Python is available. Open output/test_results.json and check that all 17 checks passed.

## Fourth session

Execute each row in MANUAL_UAT.csv and change its Status and Actual result using your own observation. Do not mark tests passed without executing them. Try manager Leena Shah and Over budget together: P005 should be the only project shown.

## Fifth session

Make a copy of the project folder. Add a new valid approved expense of CAD 500 to P002 using a new expense ID, amount_cents 50000, and an expense date before the reporting date. Predict the new total before running: P002 actual becomes CAD 8,500 and all-project actual becomes CAD 55,500. Existing tests T09 and T10 should fail because they describe the original fixture. Explain the failures, update expectations in your copy, and record the change.

## Sixth session

Add a user story for filtering by project ID. Write acceptance criteria for one match, reset, and no matches before changing the dashboard. This feature is not implemented in the starter. Record design choices and tests after completing it.

## Seventh session

Use BACKLOG.csv to practice managing work. Add a dependency and acceptance criteria to each story. Create a practice tracker board if you choose. Keep screenshots or exports only after doing the work yourself.

## CV wording

Before personal review, call this an AI-assisted practice project in progress.

After you have run, understood, manually validated, and adapted it, a truthful project entry could be:

**Project Reporting System Enhancement — Independent AI-assisted Case Study**

- Reviewed and refined business requirements, five user stories, acceptance criteria, and traceability for a simulated project reporting solution.
- Validated a SQL and Python reporting workflow using synthetic data, including duplicate detection, exception reporting, budget variance, and overdue flags.
- Executed 17 automated business-rule checks and documented dashboard acceptance results.

Use the third bullet only after you personally execute both the automated and manual checks. Add your actual extensions and tools, and be ready to distinguish starter content from your contributions. Do not claim production benefits or list this under paid employment.

## Interview practice

1. How does a business requirement differ from a user story and an acceptance criterion?
2. Why is a LEFT JOIN needed?
3. What happens if two records share an expense ID but have different amounts?
4. Why is due today not overdue?
5. How would a changed approval rule affect validation, SQL, tests, and documentation?
6. What would need to change before using this with real enterprise data?
7. Which parts did AI help create, and how did you verify them?

Your first concrete task is to open the dashboard and explain P001 in your own words.

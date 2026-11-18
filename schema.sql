DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS projects;
CREATE TABLE projects (
 project_id TEXT PRIMARY KEY, project_name TEXT NOT NULL, manager TEXT NOT NULL,
 budget_cents INTEGER NOT NULL CHECK(budget_cents > 0),
 due_date TEXT NOT NULL, status TEXT NOT NULL, completion_date TEXT
);
CREATE TABLE expenses (
 expense_id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES projects(project_id),
 amount_cents INTEGER NOT NULL CHECK(amount_cents > 0),
 expense_date TEXT NOT NULL, status TEXT NOT NULL
);

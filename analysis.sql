-- Actual cost is approved spending on or before :as_of.
-- A LEFT JOIN retains projects with no eligible expenses.
SELECT p.project_id, p.project_name, p.manager, p.budget_cents,
 COALESCE(SUM(e.amount_cents),0) AS actual_cents,
 COALESCE(SUM(e.amount_cents),0)-p.budget_cents AS variance_cents,
 CASE WHEN COALESCE(SUM(e.amount_cents),0)>p.budget_cents THEN 1 ELSE 0 END AS over_budget,
 p.due_date, p.status,
 CASE WHEN p.due_date < :as_of AND
 (p.completion_date IS NULL OR p.completion_date > :as_of) THEN 1 ELSE 0 END AS overdue
FROM projects p LEFT JOIN expenses e ON p.project_id=e.project_id
 AND e.status='Approved' AND e.expense_date<=:as_of
GROUP BY p.project_id,p.project_name,p.manager,p.budget_cents,p.due_date,p.status,p.completion_date
ORDER BY p.project_id;

CREATE TABLE IF NOT EXISTS automation_employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    salary DECIMAL(12,2) NOT NULL
);

DELETE FROM automation_employees;

INSERT INTO automation_employees
    (employee_id, employee_name, department, salary)
VALUES
    (101, 'John Smith', 'IT', 85000.00),
    (102, 'Jane Doe', 'Finance', 95000.00),
    (103, 'Michael Brown', 'HR', 75000.00);

# 06 - SQL

## Module Goal

This module documents my **fundamental** level in SQL and in the basic concepts of relational database management systems (RDBMS). The goal is not to cover advanced topics, but to demonstrate that I understand the essential vocabulary, the logic behind the most common queries, and how data is organized across related tables.

---

## What is SQL?

**SQL (Structured Query Language)** is the standard language used to communicate with relational databases. It allows you to:

- Query data (`SELECT`)
- Insert new data (`INSERT`)
- Update existing data (`UPDATE`)
- Delete data (`DELETE`)
- Define and modify table structure (`CREATE`, `ALTER`, `DROP`)

SQL is not a general-purpose programming language: it is a **declarative** language, meaning you specify *what* data you want to retrieve or modify, not *how* to do it step by step.

---

## What is an RDBMS?

A **RDBMS (Relational Database Management System)** is a system that stores data in **tables** related to each other through keys. Common examples: MySQL, PostgreSQL, SQL Server, SQLite.

Main characteristics of a relational model:

- Data is organized into **tables** (rows and columns).
- Each **row** represents a unique record.
- Each **column** represents an attribute or field of the record.
- Tables are related to each other through **primary keys** and **foreign keys**.
- The system ensures **data integrity** through constraints.

---

## Basic Concepts

### Table
A structure that stores data organized in rows and columns, similar to a spreadsheet but with defined rules and data types.

### Primary Key
A column (or set of columns) that uniquely identifies each row in a table. It cannot be duplicated or left empty.

### Foreign Key
A column that references the primary key of another table, allowing relationships to be established between them.

### Common Data Types
- `INT` — integer numbers
- `VARCHAR(n)` — variable-length text
- `DATE` / `DATETIME` — dates
- `BOOLEAN` — true or false
- `FLOAT` / `DECIMAL` — decimal numbers

### Relationships Between Tables
- **One-to-one (1:1)**
- **One-to-many (1:N)**
- **Many-to-many (N:M)** — resolved with an intermediate (junction) table

---

## Basic SQL Commands

### Querying data
```sql
SELECT * FROM customers;

SELECT name, email FROM customers
WHERE city = 'Malaga';
```

### Inserting data
```sql
INSERT INTO customers (name, email, city)
VALUES ('Ana Perez', 'ana@example.com', 'Malaga');
```

### Updating data
```sql
UPDATE customers
SET city = 'Seville'
WHERE id = 1;
```

### Deleting data
```sql
DELETE FROM customers
WHERE id = 1;
```

### Creating a table
```sql
CREATE TABLE customers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  city VARCHAR(50)
);
```

---

## Basic Clauses and Operators

| Clause / Operator | Function |
|---|---|
| `WHERE` | Filters rows based on a condition |
| `ORDER BY` | Sorts the results |
| `GROUP BY` | Groups rows with common values |
| `HAVING` | Filters already grouped results |
| `LIMIT` | Limits the number of results |
| `AND` / `OR` / `NOT` | Combines logical conditions |
| `LIKE` | Text pattern matching |
| `IN` | Checks if a value is within a list |
| `BETWEEN` | Checks if a value is within a range |

---

## Basic JOIN

`JOIN` clauses allow combining data from multiple related tables.

```sql
SELECT orders.id, customers.name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id;
```

- **INNER JOIN**: returns only matching rows in both tables.
- **LEFT JOIN**: returns all rows from the left table, even without a match.
- **RIGHT JOIN**: returns all rows from the right table, even without a match.

---

## Aggregate Functions

- `COUNT()` — counts rows
- `SUM()` — sums values
- `AVG()` — calculates the average
- `MIN()` / `MAX()` — minimum and maximum value

```sql
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city;
```

---

## Current Level

This module reflects a **fundamental** level: I understand the logic of relational tables, I can write basic queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), I understand what primary/foreign keys are, and I can describe key RDBMS concepts. I do not yet master advanced queries, complex subqueries, performance optimization, or database administration.

## Next Steps

- Practice subqueries
- Deepen knowledge of different `JOIN` types
- Learn about indexes and their impact on performance
- Practice with a real database (PostgreSQL or MySQL)

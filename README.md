# Intelligent Resource Allocation & Utilization Tracker (IRAUT)

## About

This project is a Python-based application designed to track employee utilization and recommend suitable resources for projects.  
It focuses on solving real-world problems like underutilization, overloading, and inefficient resource allocation in IT service companies.

---

## Features

- Add employee details (skill, experience, utilization)
- Add project requirements
- Analyze employee utilization
- Recommend best-fit employee for a project
- Prevent over-allocation
- MySQL-based data storage
- Allocation report generation

---

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- Object-Oriented Programming (OOP)

---

## Project Structure

```
src/
 ├── employee.py
 ├── project.py
 ├── file_manager.py
 ├── resource_allocator.py
 └── main.py

data/
 ├── employees.txt
 └── projects.txt

reports/
 └── utilization_report.txt
```

---

## How to Run

1. Start MySQL server and create a database named `iraut_db`
2. Update MySQL credentials in `file_manager.py`
3. Install the required package:
   ```
   pip install mysql-connector-python
   ```
4. Run the application:
   ```
   python src/main.py
   ```

---

## What I Learned

- Designing modular Python applications
- Integrating Python with MySQL
- Writing business logic instead of only CRUD operations
- Handling real-world resource allocation scenarios

---

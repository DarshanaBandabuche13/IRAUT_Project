# Intelligent-Resource-Allocation-Engine

## About

The Intelligent-Resource-Allocation-Engine is a Python-based application designed to address a common real-world problem in IT service companies — inefficient resource utilization.

Instead of only storing employee data, this system analyzes employee utilization and intelligently recommends the most suitable employee for a project while preventing over-allocation.

The project focuses on decision-making logic, not just basic CRUD operations.

---

## Features

* Add employee details dynamically at runtime
* Add project requirements
* Analyze employee utilization (Underutilized / Optimal / Overloaded)
* Intelligent resource recommendation based on skill, experience, and utilization
* Prevent over-allocation (utilization ≤ 100%)
* Dynamic report generation
* Clean separation of business logic and data handling

---

## Technologies Used

* Python
* File Handling
* Object-Oriented Programming (OOP)
* Business Logic & Decision Making
* Exception Handling
* Modular Design

---

## Project Structure

```
Intelligent-Resource-Allocation-Engine/
│
├── data/
│   ├── employees.txt        # Runtime-generated employee data
│   └── projects.txt         # Runtime-generated project data
│
├── reports/
│   └── utilization_report.txt   # Auto-generated report at runtime
│
├── src/
│   ├── employee.py
│   ├── project.py
│   ├── file_manager.py
│   ├── resource_allocator.py
│   └── main.py
│
└── README.md
```

---

## How to Run the Project

1. Clone the repository:

   ```
   git clone https://github.com/DarshanaBandabuche13/IRAUT_Project.git
   ```

2. Navigate to the project directory:

   ```
   cd Intelligent-Resource-Allocation-Engine
   ```

3. Run the application:

   ```
   python src/main.py
   ```

4. Use the menu-driven interface to:

   * Add employees
   * Add projects
   * Analyze utilization
   * Generate allocation recommendations

> Note: All data and reports are generated dynamically at runtime.

---

## 📊 Sample Output (Demo)

```
----------------------------------------
Employee ID   : 101
Employee Name : Sample Employee
Project ID    : P201
Skill         : Java
Utilization   : 50%
Status        : OPTIMAL
Decision      : ASSIGNED
Reason        : Skill match + Experience OK + Low utilization
----------------------------------------
```

> ⚠️ This is sample output shown for demonstration purposes. Actual output is generated dynamically at runtime.

---

## What I Learned

* Designing modular Python applications
* Implementing business logic beyond CRUD operations
* Handling real-world allocation constraints
* File-based persistence and report generation
* Writing clean, maintainable, and scalable code


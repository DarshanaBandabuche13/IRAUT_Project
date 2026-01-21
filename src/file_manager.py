import mysql.connector
from employee import Employee
from project import Project


class FileManager:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",        # change if needed
            password="1234",    # change if needed
            database="iraut_db"
        )
        self.cursor = self.conn.cursor()

    def save_employee(self, employee):
        query = """
        INSERT INTO employees (emp_id, name, skill, experience, utilization)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            employee.emp_id,
            employee.name,
            employee.skill,
            employee.experience,
            employee.utilization
        )
        self.cursor.execute(query, values)
        self.conn.commit()

    def load_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()

        employees = []
        for row in rows:
            employees.append(Employee(row[0], row[1], row[2], row[3], row[4]))
        return employees

    def save_project(self, project):
        query = """
        INSERT INTO projects (project_id, skill_required, min_experience, allocation_required)
        VALUES (%s, %s, %s, %s)
        """
        values = (
            project.project_id,
            project.skill_required,
            project.min_experience,
            project.allocation_required
        )
        self.cursor.execute(query, values)
        self.conn.commit()

    def load_projects(self):
        self.cursor.execute("SELECT * FROM projects")
        rows = self.cursor.fetchall()

        projects = []
        for row in rows:
            projects.append(Project(row[0], row[1], row[2], row[3]))
        return projects

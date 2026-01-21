from employee import Employee
from project import Project
from file_manager import FileManager
from resource_allocator import ResourceAllocator

fm = FileManager()
allocator = ResourceAllocator()


def add_employee():
    try:
        emp = Employee(
            input("Employee ID: "),
            input("Name: "),
            input("Skill: "),
            int(input("Experience (years): ")),
            int(input("Current Utilization (%): "))
        )
        fm.save_employee(emp)
        print("✅ Employee added successfully")
    except Exception:
        print("❌ Employee ID already exists or DB error")


def add_project():
    try:
        proj = Project(
            input("Project ID: "),
            input("Skill Required: "),
            int(input("Minimum Experience: ")),
            int(input("Allocation Required (%): "))
        )
        fm.save_project(proj)
        print("✅ Project added successfully")
    except Exception:
        print("❌ Project ID already exists or DB error")


def analyze_utilization():
    employees = fm.load_employees()
    if not employees:
        print("No employee data available")
        return

    print("\nEmployee Utilization Report")
    print("-" * 35)
    for emp in employees:
        status = allocator.analyze_utilization(emp)
        print(f"{emp.emp_id} | {emp.name} | {emp.utilization}% | {status}")


def recommend_resource():
    employees = fm.load_employees()
    projects = fm.load_projects()

    if not employees or not projects:
        print("Insufficient data to recommend resource")
        return

    project = projects[-1]  # latest project
    emp, reason = allocator.recommend_employee(employees, project)

    if emp:
        print("\n✅ Recommended Employee")
        print(f"Name    : {emp.name}")
        print(f"Project : {project.project_id}")
        print(f"Reason  : {reason}")

        # 📄 REPORT GENERATION
        with open("reports/utilization_report.txt", "a") as file:
            file.write("----------------------------------------\n")
            file.write(f"Employee ID   : {emp.emp_id}\n")
            file.write(f"Employee Name : {emp.name}\n")
            file.write(f"Project ID    : {project.project_id}\n")
            file.write(f"Skill         : {emp.skill}\n")
            file.write(f"Utilization   : {emp.utilization}%\n")
            file.write(f"Status        : {allocator.analyze_utilization(emp)}\n")
            file.write("Decision      : ASSIGNED\n")
            file.write(f"Reason        : {reason}\n")
            file.write("----------------------------------------\n\n")
    else:
        print(reason)


def main():
    while True:
        print("\n--- Intelligent Resource Allocation & Utilization Tracker ---")
        print("1. Add Employee")
        print("2. Add Project")
        print("3. View Utilization Report")
        print("4. Recommend Resource")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            add_project()
        elif choice == "3":
            analyze_utilization()
        elif choice == "4":
            recommend_resource()
        elif choice == "5":
            print("Exiting system")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()

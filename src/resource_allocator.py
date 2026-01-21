class ResourceAllocator:

    def analyze_utilization(self, employee):
        """
        Classifies employee based on utilization percentage
        """
        if employee.utilization < 50:
            return "UNDERUTILIZED"
        elif employee.utilization <= 80:
            return "OPTIMAL"
        else:
            return "RISK"

    def recommend_employee(self, employees, project):
        """
        Recommends the best employee for a given project
        based on skill, experience, and utilization
        """
        eligible_employees = []

        for emp in employees:
            if (
                emp.skill.lower() == project.skill_required.lower()
                and emp.experience >= project.min_experience
                and emp.utilization + project.allocation_required <= 100
            ):
                eligible_employees.append(emp)

        if not eligible_employees:
            return None, "No suitable employee found"

        # Prefer employee with lowest utilization
        eligible_employees.sort(key=lambda e: e.utilization)
        best_employee = eligible_employees[0]

        reason = (
            f"Skill match + Experience OK + "
            f"Low utilization ({best_employee.utilization}%)"
        )

        return best_employee, reason



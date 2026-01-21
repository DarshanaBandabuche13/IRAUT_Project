class Employee:
    def __init__(self, emp_id, name, skill, experience, utilization):
        self.emp_id = emp_id
        self.name = name
        self.skill = skill
        self.experience = experience
        self.utilization = utilization  # percentage (0–100)

    def to_record(self):
        """
        Converts employee object to string format
        for file storage.
        """
        return f"{self.emp_id},{self.name},{self.skill},{self.experience},{self.utilization}\n"




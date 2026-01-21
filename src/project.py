class Project:
    def __init__(self, project_id, skill_required, min_experience, allocation_required):
        self.project_id = project_id
        self.skill_required = skill_required
        self.min_experience = min_experience
        self.allocation_required = allocation_required  # percentage

    def to_record(self):
        """
        Converts project object to string format
        for file storage.
        """
        return f"{self.project_id},{self.skill_required},{self.min_experience},{self.allocation_required}\n"



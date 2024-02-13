from models.constants.job_title import JobTitle
from models.employee import Employee


class Supervisor(Employee):
    def __init__(self, username: str, password: str, job_title: JobTitle, is_admin: bool = False):
        super().__init__(username, password, job_title, is_admin)
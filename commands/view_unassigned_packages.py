from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.validators.validation_helpers import validate_login
from models.constants.job_title import JobTitle


class ViewUnassignedPackages(BaseCommand):
    def __init__(self, params: list, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        validate_login(self.app_data, requires_login=True)

        logged_in_user = self.app_data.logged_in_user


        if logged_in_user.job_title == JobTitle.SUPERVISOR or logged_in_user.job_title == JobTitle.MANAGER:
            return self.app_data.view_unassigned_packages()
        else:
            raise ValueError("Only supervisors and managers are allowed to execute this command.")

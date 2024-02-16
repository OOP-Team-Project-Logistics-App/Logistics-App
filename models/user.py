from models.constants.job_title import JobTitle


class User:
    USERNAME_LEN_MIN = 3
    USERNAME_LEN_MAX = 16
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'
    def __init__(self, username: str, password: str, job_title: JobTitle):
        self.username = username
        self.password = password
        self._job_title = job_title
        self._is_employee = None
        self._is_supervisor = None
        self._is_manager = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, name):
        if self.USERNAME_LEN_MIN <= len(name) <= self.USERNAME_LEN_MAX:
            if name.isalnum():
                self._username = name
            else:
                raise ValueError(self.USERNAME_INVALID_SYMBOLS)
        else:
            raise ValueError(self.USERNAME_LEN_ERR)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not (5 <= len(value) <= 30):
            raise ValueError("Password must be between 5 and 30 characters long.")
        if not all(char.isalnum() or char in "@*-_" for char in value):
            raise ValueError("Password contains invalid symbols.")
        self._password = value

    @property
    def job_title(self):
        return self._job_title
    
    @property
    def is_employee(self):
        return self._is_employee == JobTitle.EMPLOYEE
    
    @property
    def is_supervisor(self):
        return self._is_supervisor == JobTitle.SUPERVISOR
    
    @property
    def is_manager(self):
        return self._is_manager == JobTitle.MANAGER
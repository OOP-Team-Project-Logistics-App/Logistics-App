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
    def password(self, passw):
        special_symbols = {'@', '*', '-', '_'}
        if self.PASSWORD_LEN_MIN <= len(passw) <= self.PASSWORD_LEN_MAX:
            if passw.isalnum():
                self._password = passw
            elif any(char in special_symbols for char in passw):
                self._password = passw
            else:
                raise ValueError(self.PASSWORD_INVALID_SYMBOLS)
        else:
            raise ValueError(self.PASSWORD_LEN_ERR)

    @property
    def job_title(self):
        return self._job_title
    
    # @property
    # def is_employee(self):
    #     if self._is_employee == JobTitle.EMPLOYEE:
    #         return True
    #     else:
    #         return False
    #
    # @property
    # def is_supervisor(self):
    #     if self._is_supervisor == JobTitle.SUPERVISOR:
    #         return True
    #     else:
    #         return False
    #
    # @property
    # def is_manager(self):
    #     if self._is_manager == JobTitle.MANAGER:
    #         return True
    #     else:
    #         return False


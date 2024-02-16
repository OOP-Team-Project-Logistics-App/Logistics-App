from models.constants.job_title import JobTitle


class User:
    def __init__(self, username: str, password: str, job_title: JobTitle):
        self.username = username
        self.password = password
        self._job_title = job_title

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not 3 <= len(value) <= 16:
            raise ValueError("Username must be between 3 and 16 characters long!")
        if not value.isalnum():
            raise ValueError("Username contains invalid symbols!")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not (6 <= len(value) <= 20):
            raise ValueError("Password must be between 6 and 20 characters long!")
        if not all(char.isalnum() or char in "@*-_" for char in value):
            raise ValueError("Password contains invalid symbols!")
        self._password = value

    @property
    def job_title(self):
        return self._job_title
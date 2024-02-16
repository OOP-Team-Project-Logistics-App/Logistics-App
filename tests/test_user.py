import unittest
from models.constants.job_title import JobTitle
from models.user import User


class User_Should(unittest.TestCase):
    
    def setUp(self):
        self.user = User("TestUser", "test123@*_-", JobTitle.EMPLOYEE)

    def test_initializer_whenPropertiesAreValid(self):
        self.assertEqual("TestUser", self.user.username)
        self.assertEqual("test123@*_-", self.user.password)
        self.assertEqual(JobTitle.EMPLOYEE, self.user.job_title)

    def test_initializer_raisesError_whenUsernameTooShort(self):
        with self.assertRaises(ValueError):
            self.user.username = "a"

    def test_initializer_raisesError_whenUsernameTooLong(self):
        with self.assertRaises(ValueError):
            self.user.username = "a" * 21

    def test_initializer_raisesError_whenUsernameInvalidSymbol(self):
        with self.assertRaises(ValueError):
            self.user.username = "invalid_user"

    def test_initializer_raisesError_whenPasswordTooShort(self):
        with self.assertRaises(ValueError):
            self.user.password = "short"

    def test_initializer_raisesError_whenPasswordTooLong(self):
        with self.assertRaises(ValueError):
            self.user.password = "a" * 21

    def test_initializer_raisesError_whenPasswordInvalidSymbol(self):
        with self.assertRaises(ValueError):
            self.user.password = "invalid_$ymbol"
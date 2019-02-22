from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from . import database


class UserModel:
    """
    The v2 user model.
    """


    def __init__(self, username, email, password,
                 firstname, lastname, phone, passportUrl, isPolitician, othername, token=None):
        """
            Constructor of the user class
            New user objects are created with this method
        """
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.phone = phone
        self.password = self.encrypt_password_on_signup(password)
        self.passportUrl = passportUrl
        self.isPolitician = isPolitician
        self.othername = othername
        # self.isAdmin= isAdmin
        self.token= token

    def save_user(self):
        """
        Add a new user to the users table
        """
        save_user_query = """
        INSERT INTO users(username, firstname, lastname, phone, email, password, passportUrl, isPolitician, othername, isAdmin) VALUES(
            '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'
        )""".format(self.username, self.firstname, self.lastname, self.phone, self.email, self.password, self.passportUrl, self.isPolitician, self.othername, False)
        
        database.query_data_from_db(save_user_query)

    def encrypt_password_on_signup(self, password):
        """
            hash password on sign up
        """
        hashed_password = generate_password_hash(str(password))
        return hashed_password

    @staticmethod
    def get_user_by_mail(email):
        select_user_by_email = """
        SELECT id, username, password FROM users
        WHERE users.email = '{}'""".format(email)

        return database.select_data_from_db(select_user_by_email)

    @staticmethod
    def check_if_password_n_hash_match(password_hash, password):
        return check_password_hash(password_hash, str(password))
    def logout(self):
            query = """
        INSERT INTO blacklist (token) VALUES ('{}')
        """.format(self.token)

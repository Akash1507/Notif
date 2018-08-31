import uuid
from src.common.utils import Utils
from src.common.database import Database
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self.id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.name)

    def is_login_valid(email, password):
        user_data = Database.find_one("users", {'email': email})
        if user_data is None:
            raise UserErrors.UserNotExistError("Your User Does not exist!")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your Password was Wrong!")
        return True

    @staticmethod
    def register_user(email, password):
        user_data = Database.find_one("users", {'email': email})

        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError("User is already registered")
        if not Utils.email_is_valid():
            raise UserErrors.InvalidEmailError("Email is Invalid")

        User(email, Utils.hashed_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users",self.json)

    def json(self):
        return {
            "_id" : self.id,
            "email" : self.email,
            "password" : self.password
        }

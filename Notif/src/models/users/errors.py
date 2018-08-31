
class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserError):
    pass

class IncorrectpasswordError(UserError):
    pass

class UserAlreadyRegisteredError():
    pass

class InvalidEmailError():
    pass
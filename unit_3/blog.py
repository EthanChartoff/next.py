import string

class UsernameContainsIllegalCharacterException(Exception): 
    """ 
    Exception raised when the username contains an illegal character.
    """
    LEGAL_CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    def __init__(self, illegal_chars=''):
        super().__init__()
        self.illegal_chars = illegal_chars

    def __str__(self):
        return f"The username contains the following illegal character(s): {self.illegal_chars}"

    @staticmethod
    def check_username(username):
        """
        check if the username contains an illegal character. 
        if it contains an illegal character, save all the illegal characters and their position in the username
        """
        illegal_chars = ''
        for i, char in enumerate(username):
            if char not in UsernameContainsIllegalCharacterException.LEGAL_CHARACTERS:
                illegal_chars += f"illegal char {char} at position {i}"
        if illegal_chars:
            raise UsernameContainsIllegalCharacterException(illegal_chars)            

class UsernameTooShortException(Exception):
    """
    Exception raised when the username is too short.
    """
    MIN_LENGTH = 3
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "The username is too short."
    
    @staticmethod
    def check_username(username):
        if len(username) < UsernameTooShortException.MIN_LENGTH:
            raise UsernameTooShortException

class UsernameTooLongException(Exception):
    """
    Exception raised when the username is too long.
    """
    MAX_LENGTH = 16
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "The username is too long."

    @staticmethod
    def check_username(username):
        if len(username) > UsernameTooLongException.MAX_LENGTH:
            raise UsernameTooLongException


class PasswordMissingCharacterException(Exception):
    """
    Exception raised when the password is missing a character.
    """
    def __init__(self, missing_chars):
        super().__init__()
        self.missing_chars = missing_chars

    def __str__(self):
        return f"The password is missing the following character(s): {self.missing_chars}"

    @staticmethod
    def checkIfPasswordHasAllCharacter(password):
        """
        Check if password has at least one of all these characters:
        - uppercase letter
        - lowercase letter
        - digit  
        - special character
        """
        missing_chars = ''
        if not any(c.isupper() for c in password):
            missing_chars += 'uppercase letter, '
        if not any(c.islower() for c in password):
            missing_chars += 'lowercase letter, '
        if not any(c.isdigit() for c in password):
            missing_chars += 'digit, '
        if not any(c in string.punctuation for c in password):
            missing_chars += 'special character, '
        
        if missing_chars:
            raise PasswordMissingCharacterException(missing_chars[:-2])  # Remove the extra comma and space
            
class PasswordTooShortException(Exception):
    """
    Exception raised when the password is too short.
    """
    MIN_LENGTH = 8
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "The password is too short."

    @staticmethod
    def checkPassword(password):
        if len(password) < PasswordTooShortException.MIN_LENGTH:
            raise PasswordTooShortException

class PasswordTooLongException(Exception):
    """
    Exception raised when the password is too long.
    """
    MAX_LENGTH = 40
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "The password is too long."

    @staticmethod
    def checkPassword(password):
        if len(password) > PasswordTooLongException.MAX_LENGTH:
            raise PasswordTooLongException

def check_input(username, password): 
    """
    Checks if the input is valid.
    """
    try:
        UsernameContainsIllegalCharacterException.check_username(username)
        UsernameTooShortException.check_username(username)
        UsernameTooLongException.check_username(username)
        PasswordMissingCharacterException.checkIfPasswordHasAllCharacter(password)
        PasswordTooShortException.checkPassword(password)
        PasswordTooLongException.checkPassword(password)
    except (UsernameContainsIllegalCharacterException, UsernameTooShortException, UsernameTooLongException, PasswordMissingCharacterException, PasswordTooShortException, PasswordTooLongException) as e:
        print(e)
    else:
        print("OK")

def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

if __name__ == '__main__':
    main()
import re

class Validator:
    def __init__(self):
        pass

    @staticmethod
    def is_email_valid(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def is_username_valid(username: str) -> bool:
        return 3 <= len(username) <= 20 and username.isalnum()

    @staticmethod
    def is_password_strong(password: str) -> bool:
        return (len(password) >= 8 and 
                any(char.isdigit() for char in password) and 
                any(char.isupper() for char in password) and 
                any(char.islower() for char in password))

    @staticmethod
    def is_phone_number_valid(phone: str) -> bool:
        pattern = r'^\+?[1-9]\d{1,14}$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def is_date_format_valid(date_string: str, format_string: str) -> bool:
        from datetime import datetime
        try:
            datetime.strptime(date_string, format_string)
            return True
        except ValueError:
            return False


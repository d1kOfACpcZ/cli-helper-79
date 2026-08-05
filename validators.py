import re

class InputValidator:
    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r'^\+?[1-9]\d{1,14}$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_username(username: str) -> bool:
        pattern = r'^[a-zA-Z0-9_]{3,15}$'
        return re.match(pattern, username) is not None

    @staticmethod
    def validate_password(password: str) -> bool:
        return (len(password) >= 8 and 
                any(c.isdigit() for c in password) and 
                any(c.isalpha() for c in password))

# Example usage:
if __name__ == '__main__':
    print(InputValidator.validate_email('example@test.com'))
    print(InputValidator.validate_phone('+123456789012'))
    print(InputValidator.validate_username('user_name123'))
    print(InputValidator.validate_password('Passw0rd!'))

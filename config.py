import os

class Config:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.debug = self.environment == 'development'
        self.database_uri = os.getenv('DATABASE_URI', 'sqlite:///default.db')
        self.secret_key = os.getenv('SECRET_KEY', 'mysecret')
        
    def __str__(self):
        return f'Config(environment={self.environment}, debug={self.debug}, database_uri={self.database_uri})'

# Example of configuration loading
if __name__ == '__main__':
    config = Config()
    print(config)
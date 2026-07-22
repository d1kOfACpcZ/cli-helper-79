import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CLIHelper:
    def __init__(self, name):
        self.name = name
        logger.info(f'CLIHelper initialized with name: {self.name}')

    def greet(self):
        greeting = f'Welcome to {self.name}!'
        logger.info(greeting)
        return greeting

    def execute_command(self, command):
        logger.info(f'Executing command: {command}')
        try:
            # Simulating command execution
            result = f'Executed: {command}'
            logger.info(result)
            return result
        except Exception as e:
            logger.error(f'Error executing command: {e}')
            return None

if __name__ == '__main__':
    cli_helper = CLIHelper('My CLI Tool')
    cli_helper.greet()
    cli_helper.execute_command('list all')
    cli_helper.execute_command('exit')
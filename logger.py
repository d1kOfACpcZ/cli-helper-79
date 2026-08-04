import logging

# Configure the logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger('cli_helper')

def log_info(message):
    """Logs an info message."""
    logger.info(message)


def log_warning(message):
    """Logs a warning message."""
    logger.warning(message)


def log_error(message):
    """Logs an error message."""
    logger.error(message)


def log_debug(message):
    """Logs a debug message, useful for debugging."""
    logger.debug(message)


def log_exception(exc):
    """Logs an exception with traceback."""
    logger.exception(exc)

# Example usage
if __name__ == '__main__':
    log_info('Application started.')
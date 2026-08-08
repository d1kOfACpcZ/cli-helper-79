import logging

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# Helper functions for logging

def debug(message):
    """Log a debug message."""
    logger.debug(message)


def info(message):
    """Log an info message."""
    logger.info(message)


def warning(message):
    """Log a warning message."""
    logger.warning(message)


def error(message):
    """Log an error message."""
    logger.error(message)


def critical(message):
    """Log a critical message."""
    logger.critical(message)

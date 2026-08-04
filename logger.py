import logging


def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Sets up a logger that writes to a specified log file and prints to console.

    Args:
        name (str): The name of the logger.
        log_file (str): The path to the log file.
        level (int): The logging level (default is DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.addHandler(logging.StreamHandler())  # also log to console

    return logger


if __name__ == '__main__':
    log = setup_logger('example_logger', 'example.log')
    log.info('This is an info message')
    log.error('This is an error message')
    log.debug('This is a debug message')
import logging


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with the specified name and log level.

    Args:
        name (str): The name of the logger.
        level (int): The logging level (default is logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    # Example usage
    log = setup_logger('example_logger')
    log.info('This is an info message.')
    log.warning('This is a warning message.')
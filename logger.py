import logging
from logging.handlers import RotatingFileHandler

# Logger setup with rotation

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=5):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)
    
    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)
    
    return logger

# Example usage of the logger
if __name__ == '__main__':
    logger = setup_logger()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
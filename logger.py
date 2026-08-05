import logging

# Set up a logger for the application
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(ch)

# Function to log performance metrics

def log_performance_metrics(start_time, end_time, additional_info=''):
    duration = end_time - start_time
    logger.info(f'Performance metric: Duration: {duration} seconds {additional_info}') 

# Example log message
def sample_operation():
    import time
    start_time = time.time()
	# Simulating operation
    time.sleep(1)
    end_time = time.time()
    log_performance_metrics(start_time, end_time, 'for sample_operation')
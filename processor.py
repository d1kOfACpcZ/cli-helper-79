import json
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    pass

def process_data(data):
    if not isinstance(data, dict):
        logger.error('Invalid data type, expected dict')
        raise ProcessingError('Data must be a dictionary')
    
    try:
        result = handle_data(data)
        logger.info('Data processed successfully')
        return result
    except KeyError as e:
        logger.error(f'Missing key in data: {str(e)}')
        raise ProcessingError(f'Missing key: {str(e)}')
    except TypeError as e:
        logger.error(f'Type error occurred: {str(e)}')
        raise ProcessingError('Type error in data processing')

def handle_data(data):
    # Simulate potential errors
    if 'value' not in data:
        raise KeyError('value')
    return data['value'] * 2

if __name__ == '__main__':
    test_data = {'value': 10}
    try:
        print(process_data(test_data))
        print(process_data([]))  # This will raise an error
    except ProcessingError as e:
        logger.error(f'Processing error: {str(e)}')

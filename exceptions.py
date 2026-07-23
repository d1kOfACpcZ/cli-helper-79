class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class InvalidInputError(CustomError):
    """Raised when the input is invalid."""
    def __init__(self, message='Invalid input provided.'): 
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when a required item is not found."""
    def __init__(self, item, message='Not found.'): 
        self.message = f'{item} not found: {message}'
        super().__init__(self.message)

class OperationFailedError(CustomError):
    """Raised when an operation fails."""
    def __init__(self, operation, message='Operation failed.'): 
        self.message = f'Operation "{operation}" failed: {message}'
        super().__init__(self.message)

# Example usage for raising errors

def process_data(data):
    if not isinstance(data, dict):
        raise InvalidInputError('Data should be a dictionary.')
    if 'key' not in data:
        raise NotFoundError('key')
    if data['key'] == 'bad_value':
        raise OperationFailedError('process_data', 'Received bad value.')

    # Processing logic here
    return True
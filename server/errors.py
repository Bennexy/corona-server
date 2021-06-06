import sys
sys.path.append('.')

from server.logger import get_logger

logger = get_logger("error logger")

class APIError(Exception):
    def __init__(self, message, error):
        logger.error(f'error {error}, message {message}')


class UnknownType(APIError):
    def __init__(self, error_type):
        super.__init__("unknown type {error_type}", UnknownType)











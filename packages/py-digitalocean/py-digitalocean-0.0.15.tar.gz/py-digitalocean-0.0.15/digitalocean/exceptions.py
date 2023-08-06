"""Custom Exceptions"""

class NotAuthorized(Exception):
    """Not Authorised Exception"""
    def __init__(self):
        super().__init__('Failed to authenticate with Digital Ocean')

class NotFound(Exception):
    """Not Found Exception"""
    def __init__(self):
        super().__init__("Object not found")

class InternalError(Exception):
    """Internal Error Exception"""
    def __init__(self):
        super().__init__("Internal Error")

class InvalidRequest(Exception):
    """Invalid Request"""
    def __init__(self, msg):
        super().__init__(f"Invalid Request: {msg}")

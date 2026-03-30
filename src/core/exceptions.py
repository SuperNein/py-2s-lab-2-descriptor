class TaskError(Exception):
    """Base exception for Task models"""
    pass

class InvalidPriorityError(TaskError):
    """Raised when an invalid priority is given"""
    pass

class InvalidStatusError(TaskError):
    """Raised when an invalid status is given"""
    pass

class InvalidStatusChangeError(TaskError):
    """Raised when status change is invalid"""
    pass

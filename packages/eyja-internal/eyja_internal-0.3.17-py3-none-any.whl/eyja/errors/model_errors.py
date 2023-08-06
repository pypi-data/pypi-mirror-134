from .base_error import BaseError


class ParseModelNamespaceError(BaseError):
    def __init__(self, message: str = None, *args: object) -> None:
        super().__init__('PARSE_NAMESPACE', message, *args)

class MissedRepresentationError(BaseError):
    def __init__(self, message: str = None, *args: object) -> None:
        super().__init__('MISSED_REPRESENTATION', message, *args)

class ObjectAlreadyExistsError(BaseError):
    def __init__(self, message: str = None, *args: object) -> None:
        super().__init__('OBJECT_ALREADY_EXISTS', message, *args)

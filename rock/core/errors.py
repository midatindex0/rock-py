class RockException(Exception):
    pass

class Rock404(RockException):
    pass

class RockUnknown(RockException):
    pass
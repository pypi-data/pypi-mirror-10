

class JOSEError(Exception):
    pass


class JWSError(JOSEError):
    pass


class JWTError(JOSEError):
    pass


class JWTSignatureError(JWTError):
    pass


class ExpiredSignatureError(JWTError):
    pass



class JOSEError(Exception):
    pass


class JWSError(JOSEError):
    pass


class JWTError(JOSEError):
    pass


class ExpiredSignatureError(JWTError):
    pass

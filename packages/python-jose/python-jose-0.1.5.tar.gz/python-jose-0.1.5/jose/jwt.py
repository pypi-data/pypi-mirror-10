
from calendar import timegm
from datetime import datetime
from datetime import timedelta
from six import string_types

from jose import jws

from .exceptions import JWTError
from .utils import timedelta_total_seconds


def encode(claims, key, algorithm=None):
    """Encodes a claims set and returns a JWT string.

    JWTs are JWS signed objects with a few reserved claims.

    Examples:

        >>> jwt.encode({'a': 'b'}, 'secret', algorithm='HS256')
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhIjoiYiJ9.jiMyrsmD8AoHWeQgmxZ5yq8z0lXS67_QGs52AzC8Ru8'

    Args:
        claims (dict): A claims set to sign
        key (str): The key to use for signing the claim set
        headers (dict, optional): A set of headers that will be added to
            the default headers.  Any headers that are added as additional
            headers will override the default headers.
        algorithm (str, optional): The algorithm to use for signing the
            the claims.  Defaults to HS256.

    Returns:
        str: The string representation of the header, claims, and signature.

    Raises:
        JWTError: If there is an error encoding the claims.

    """

    for time_claim in ['exp', 'iat', 'nbf']:

        # Convert datetime to a intDate value in known time-format claims
        if isinstance(claims.get(time_claim), datetime):
            claims[time_claim] = timegm(claims[time_claim].utctimetuple())

    return jws.sign(claims, key)


def decode(token, key, algorithms=None, options=None, audience=None, issuer=None):
    """Verifies a JWT string's signature and validates reserved claims.

    Examples:

        >>> payload = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhIjoiYiJ9.jiMyrsmD8AoHWeQgmxZ5yq8z0lXS67_QGs52AzC8Ru8'
        >>> jwt.decode(payload, 'secret', algorithms='HS256')

    Args:
        token (str): A signed JWS to be verified.
        key (str): A key to attempt to verify the payload with.
        algorithms (str or list): Valid algorithms that should be used to verify the JWS.
        audience (str): The intended audience of the token.  If the "aud" claim is
            included in the claim set, then the audience must be included and must equal
            the provided claim.
        issuer (str): The issuer of the token.  If the "iss" claim is
            included in the claim set, then the issuer must be included and must equal
            the provided claim.
        options (dict): A dictionary of options for skipping validation steps.

            default = {
                'verify_signature': True,
                'verify_aud': True,
                'verify_iat': True,
                'verify_exp': True,
                'verify_nbf': True,
                'leeway': 0,
            }

    Returns:
        dict: The dict representation of the claims set, assuming the signature is valid
            and all requested data validation passes.

    Raises:
        JWTError: If the signature is invalid in any way.

    """

    defaults = {
        'verify_signature': True,
        'verify_aud': True,
        'verify_iat': True,
        'verify_exp': True,
        'verify_nbf': True,
        'verify_iss': True,
        'leeway': 0,
    }

    if options:
        defaults.update(options)

    # TODO: skip verification for verify_signature == False
    token_info = jws.verify(token, key, algorithms)

    _validate_claims(token_info, audience=audience, issuer=issuer, options=defaults)

    return token_info


def _validate_iat(claims):
    """Validates that the 'iat' claim is valid.

    The "iat" (issued at) claim identifies the time at which the JWT was
    issued.  This claim can be used to determine the age of the JWT.  Its
    value MUST be a number containing a NumericDate value.  Use of this
    claim is OPTIONAL.

    Args:
        claims (dict): The claims dictionary to validate.
    """

    if 'iat' not in claims:
        return

    try:
        int(claims['iat'])
    except ValueError:
        raise JWTError('Issued At claim (iat) must be an integer.')


def _validate_nbf(claims, leeway=0):
    """Validates that the 'nbf' claim is valid.

    The "nbf" (not before) claim identifies the time before which the JWT
    MUST NOT be accepted for processing.  The processing of the "nbf"
    claim requires that the current date/time MUST be after or equal to
    the not-before date/time listed in the "nbf" claim.  Implementers MAY
    provide for some small leeway, usually no more than a few minutes, to
    account for clock skew.  Its value MUST be a number containing a
    NumericDate value.  Use of this claim is OPTIONAL.

    Args:
        claims (dict): The claims dictionary to validate.
        leeway (int): The number of seconds of skew that is allowed.
    """

    if 'nbf' not in claims:
        return

    try:
        nbf = int(claims['nbf'])
    except ValueError:
        raise JWTError('Not Before claim (nbf) must be an integer.')

    now = timegm(datetime.utcnow().utctimetuple())

    if nbf > (now + leeway):
        raise JWTError('The token is not yet valid (nbf)')


def _validate_exp(claims, leeway=0):
    """Validates that the 'exp' claim is valid.

    The "exp" (expiration time) claim identifies the expiration time on
    or after which the JWT MUST NOT be accepted for processing.  The
    processing of the "exp" claim requires that the current date/time
    MUST be before the expiration date/time listed in the "exp" claim.
    Implementers MAY provide for some small leeway, usually no more than
    a few minutes, to account for clock skew.  Its value MUST be a number
    containing a NumericDate value.  Use of this claim is OPTIONAL.

    Args:
        claims (dict): The claims dictionary to validate.
        leeway (int): The number of seconds of skew that is allowed.
    """

    if 'exp' not in claims:
        return

    try:
        exp = int(claims['exp'])
    except ValueError:
        raise JWTError('Expiration Time claim (exp) must be an integer.')

    now = timegm(datetime.utcnow().utctimetuple())

    if exp < (now - leeway):
        raise JWTError('Signature has expired')


def _validate_aud(claims, audience=None):
    """Validates that the 'aud' claim is valid.

    The "aud" (audience) claim identifies the recipients that the JWT is
    intended for.  Each principal intended to process the JWT MUST
    identify itself with a value in the audience claim.  If the principal
    processing the claim does not identify itself with a value in the
    "aud" claim when this claim is present, then the JWT MUST be
    rejected.  In the general case, the "aud" value is an array of case-
    sensitive strings, each containing a StringOrURI value.  In the
    special case when the JWT has one audience, the "aud" value MAY be a
    single case-sensitive string containing a StringOrURI value.  The
    interpretation of audience values is generally application specific.
    Use of this claim is OPTIONAL.

    Args:
        claims (dict): The claims dictionary to validate.
        audience (str): The audience that is verifying the token.
    """

    if 'aud' not in claims:
        # if audience:
        #     raise JWTError('Audience claim expected, but not in claims')
        return

    audience_claims = claims['aud']
    if isinstance(audience_claims, string_types):
        audience_claims = [audience_claims]
    if not isinstance(audience_claims, list):
        raise JWTError('Invalid claim format in token')
    if any(not isinstance(c, string_types) for c in audience_claims):
        raise JWTError('Invalid claim format in token')
    if audience not in audience_claims:
        raise JWTError('Invalid audience')


def _validate_iss(claims, issuer=None):
    """Validates that the 'iss' claim is valid.

    The "iss" (issuer) claim identifies the principal that issued the
    JWT.  The processing of this claim is generally application specific.
    The "iss" value is a case-sensitive string containing a StringOrURI
    value.  Use of this claim is OPTIONAL.

    Args:
        claims (dict): The claims dictionary to validate.
        issuer (str): The issuer that sent the token.
    """

    if issuer is not None:
        if claims.get('iss') != issuer:
            raise JWTError('Invalid issuer')


def _validate_claims(claims, audience=None, issuer=None, options=None):

    leeway = options.get('leeway', 0)

    if isinstance(leeway, timedelta):
        leeway = timedelta_total_seconds(leeway)

    if not isinstance(audience, (string_types, type(None))):
        raise JWTError('audience must be a string or None')

    if options.get('verify_iat'):
        _validate_iat(claims)

    if options.get('verify_nbf'):
        _validate_nbf(claims, leeway=leeway)

    if options.get('verify_exp'):
        _validate_exp(claims, leeway=leeway)

    if options.get('verify_aud'):
        _validate_aud(claims, audience=audience)

    if options.get('verify_iss'):
        _validate_iss(claims, issuer=issuer)

# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                               package.ipt_token.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from flask import current_app, request
from functools import wraps

from typing import Union, Callable, Any, Optional

import jwt
import datetime
# |--------------------------------------------------------------------------------------------------------------------|

class IPToken(object):
# |====================================================================================================================|
# | GENERATE TOKEN DECORATOR |=========================================================================================|
# |====================================================================================================================|
    @staticmethod
    def generate_token(
        status_code: int,
        exp: Optional[int] = 60,
        algorithm: Optional[str] = 'HS256',
        header_arguments: Optional[dict[str, Any]] = {}
        ):
        """Will add a header to the HTTP packet depending on the status code entered. Remember that the route response
        must be set -> tuple[<your response>, int]
        Args:
            status_code (int): Status code that will release the token generation
            exp (Optional[int], optional): Validity time of the token (minutes). Defaults to 60.
            algorithm (Optional[str], optional): Symmetric keyed hashing algorithm. Defaults to 'HS256'.
            header_arguments (Optional[dict[str, Any]], optional): Additional arguments you want to add inside the token
            to be encrypted. Defaults to {}.
        """
        def inner(func: Callable[..., tuple[Any, int]]) -> Callable[..., Union[tuple[Any, int, dict], tuple[Any, int]]]:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Union[tuple[Any, int, dict], tuple[Any, int]]:
                func_value: tuple[str, int] = func(*args, **kwargs)
                if func_value[1] == status_code:
                    
                    # | assemble header |------------------------------------------------------------------------------|
                    encode_header: dict[str, Union[str, datetime.datetime]] = {
                        "ip": request.remote_addr,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=exp)
                    }
                    encode_header.update(header_arguments)
                    # |------------------------------------------------------------------------------------------------|

                    # | token encode |---------------------------------------------------------------------------------|
                    token: str = jwt.encode(payload=encode_header,
                                            key=current_app.config["SECRET_KEY"],
                                            algorithm=algorithm)
                    # |------------------------------------------------------------------------------------------------|

                    return func_value[0], func_value[1], {"IPToken": token}
                return func_value
            return wrapper
        return inner
# |====================================================================================================================|
# | REQUIRED TOKEN DECORATOR |=========================================================================================|
# |====================================================================================================================|
    @staticmethod
    def required_token(algorithm: Optional[list[str]] = ['HS256']):
        """
        Decorator that should be set on routes that require token authentication
        Args:
            algorithm (Optional[list[str]], optional): Symmetric keyed hashing algorithm. Defaults to ['HS256'].
        """
        def inner(func: Callable[..., tuple[Any, int]]) -> Callable[..., tuple[Any, int]]:
            @wraps(func)
            def wrapper(*args, **kwargs) -> tuple[Any, int]:
                # |====================================================================================================|
                # | INTERNAL FUNCTION - TOKEN AUTHENTICATION |=========================================================|
                # |====================================================================================================|
                def token_authentication(token: str, algorithm: list[str]) -> tuple[str, int]:
                    # | Split token string |---------------------------------------------------------------------------|
                    try:
                        try:
                            token: str = token.split()[1]
                        except IndexError:
                            return "BAD REQUEST - TOKEN", 400
                    except AttributeError:
                        return "BAD REQUEST - TOKEN NOT INFORMED", 400
                    # |------------------------------------------------------------------------------------------------|
                    # | Decode token |---------------------------------------------------------------------------------|
                    try:
                        try:
                            decode_token: dict[str, Any] = jwt.decode(
                                token,
                                current_app.config['SECRET_KEY'],
                                algorithms=algorithm
                            )
                        except jwt.exceptions.DecodeError:
                            return "INVALID TOKEN", 400
                    except jwt.exceptions.ExpiredSignatureError:
                        return "EXPIRED TOKEN", 403
                    # |------------------------------------------------------------------------------------------------|
                    if decode_token['ip'] != request.remote_addr:
                        return "IP ADDRESS DOES NOT MATCH", 403
        
                    return "VALID TOKEN", 200
                # Token Authentication |-------------------------------------------------------------------------------|
                token: str = request.headers.get("Authorization")
                token_auth: tuple[str, int] = token_authentication(token, algorithm)
                return token_auth if token_auth[1] != 200 else func(*args, **kwargs)
                # |----------------------------------------------------------------------------------------------------|
            return wrapper
        return inner
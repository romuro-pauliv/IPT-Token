## How the IPT Token works

The IPT Token generates a token based on the `SECRET_KEY` of a Flask application by concatenating the IP address of the HTTP packet sent in the `POST` method into a specific route. The token will be sent in the server's HTTP response packet in the header. For this reason, your route response must follow the parameters set for `@generate_token()` to work correctly.

The `@generate_token()` decorator will not interfere with the structure of your response. Regardless of whether it is an HTML rendering or a json application. The only object that will interfere is the HTTP packet header.

---

#### Structure and Encryption

When starting a Flask application it is necessary to set the `SECRET_KEY` in the internal instance of the application. The IPT Token extension will request in the `current_app.config` instance the base key of the encryption. 

__[1] App config__
```Python
def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="<your .env import our random key string>")

    # ...

    return app
```

After setting the key in the configuration instance, you will be able to use the decorators. You can view the [quickstart]() module to see the application of the decorators at a glance. 

The structure of the decorator follows the parameterization bellow:

__[2] Decorator structure__
```Python
class IPToken(object):
    @staticmethod
    def generate_token(...):
        def inner(func: Callable[..., tuple[Any, int]]) -> Callable[..., Union[tuple[Any, int], tuple[Any, int, dict]]]:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Union[tuple[Any, int], tuple[Any, int, dict]]:
                # |----------------|
                # | Assemble Token |
                # |----------------|
                return func(*args, **kwargs), {"IPToken": token}
            return wrapper
        return inner
```

---

#### HTTP packet IP requirement

When assembling the token, the IP address of the received packet will be requested and concatenated in a dictionary to add to the JWT payload.

**[3] Token encode**
```Python
# assemble header 
encode_header: dict[str, Union[str, datetime.datetime]] = {
    "ip": request.remote_addr,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=exp)
}
encode_header.update(header_arguments)

# token encode
token: str = jwt.encode(payload=encode_header,
                        key=current_app.config["SECRET_KEY"],
                        algorithm=algorithm
)
```

The __[3] Token encode__ code block will be wrapped by the `status_code` argument check function, giving the programmer freedom to structure his route response in any way.

__[4] Check condition__
```Python
def wrapper(*args, **kwargs) -> Union[tuple[Any, int], tuple[Any, int, dict]]:
    func_value: tuple[Any, int] = func(*args, **kwargs)
    if func_value[1] == status_code:
        # |------------------|
        # | [3] Token encode |
        # |------------------|
        return func_value[0], func_value[1], {"IPToken": token}
    return func_value
```

---

#### Function parameters

In the above structures there are parameters not yet defined in the documentation. Each parameter can be modified by the end programmer to best suit their application.

__`@generate_token()`__
| Parameter | Description | Format |
|-----------|-------------|--------|
| __status_code__ | Status code that will release the token generation | `int` |
| __exp__ | Validity time of the token (minutes). Defaults to 60 | Optional: `int` |
| __algorithm__ | Symmetric keyed hashing algorithm. Defaults to `HS256` | Optional: `str` |
| __header_arguments__ | Additional arguments you want to add inside the token to be encrypted. Defaults to {} | Optional: `dict[str, Any]` |

---

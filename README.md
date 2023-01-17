## IPT Token

The IPT Token module is intended to be an extension to your Flask applications. The module will generate a token with a simple `@generate_token()` decorator set in your route depending on the status code you enter. Then you can request this token with a simple `@required_token()` defined in routes that require authentication.

```Python
@bp.route("/login", methods=["POST"])
@generate_token(200)
def sign_in() -> tuple[..., int]:
    return login_funcion(...)


@bp.route("/my-feed", methods=["POST"])
@required_token()
def my_feed() -> tuple[..., int]:
    return return_my_feed()
```
----
### Summary

1. Why use IPT Token

2. How the IPT Token works
2.1. Structure and Encryption
2.2. HTTP packet IP requirement
2.3. Function parameters

3. Applying the IPT Token object in an app
3.1. Route structure for proper operation
3.2. Possible responses from the `@required_token`decorator

4. Quickstart
4.1. Import & Use

5. Requirements and installation

---

## Why use IPT Token

The standard method of user validation using browser caching and session allocation in server RAM may be unusual for some processes that require a high level of security and a high load of requests to the server. On a gigantic request scale, allocating strings containing the Id of the active user on the server may impact other processing, affecting all users on the network. Also, storing the user cache without further validation can open a loophole for Browser Cache Poisoning.

---

## How the IPT Token works

The IPT Token generates a token based on the `SECRET_KEY` of a Flask application by concatenating the IP address of the HTTP packet sent in the `POST` method into a specific route. The token will be sent in the server's HTTP response packet in the header. For this reason, your route response must be in the parameters set for `@generate_token()` to work correctly.

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

The structure of the decorator follows the following parameterization:

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

The __[3] Token encode__ code block will be wrapped by the `status_code` argument check function giving the programmer freedom to structure his route response in any way.

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

In the above structures there are parameters not yet defined in the documentation. Each parameter can be modified by the end programmer to best suit the application created.

__`@generate_token()`__
| Parameter | Description | Format |
|-----------|-------------|--------|
| __status_code__ | Status code that will release the token generation | `int` |
| __exp__ | Validity time of the token (minutes). Defaults to 60 | Optional: `int` |
| __algorithm__ | Symmetric keyed hashing algorithm. Defaults to `HS256` | Optional: `str` |
| __header_arguments__ | Additional arguments you want to add inside the token to be encrypted. Defaults to {} | Optional: `dict[str, Any]` |

---

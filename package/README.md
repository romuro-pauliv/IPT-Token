# IPToken

The code implements a `JWT` (JSON Web Token) token generation and token authentication feature in `Flask` routes. The feature allows routes to be protected with a generated token with information such as the user's **IP address** and the **validity** of the token. Furthermore, the token can be customized with additional arguments. The IPToken class contains two decorators: 
- `@generate_token` is used to generate tokens and add them to the response header of a specific route (which has a certain HTTP status code). 
- `@required_token` is used to protect routes that require token authentication. If a token is provided in the request, its validity is checked by comparing its encoded IP address with the IP address of the current request.

---

### Installation

[Download the package](https://github.com/romuro-pauliv/IPT-Token/raw/package-development/package/dist/iptoken-flask-0.9.1.tar.gz) and run the command bellow to install:

```
pip install iptoken-flask-0.9.C1.tar.gz
```

---

### Import & Use

To use the `IPToken` in your routes, import it as follows:

```Python
from iptoken.module_iptoken import IPToken
```

Then to set `generate_token` on the route that you want the token to be generated:

```Python
@bp.route('/login', methods=["POST"])
@IPToken.generate_token(200)
def login() -> tuple[str, int]:
    return ("Login", 200) if check_credentials() is True else ("username/password is incorrect", 400)
```

The code above is for a ficticious route. The intent is to demonstrate that `generate_token` will only generate the token based on the `status_code` entered in the decorator.

To use the `@required_token` function, do as follows:

```Python
@bp.route("/feed", methods=["GET"])
@required_token()
def login() -> tuple[str, int]:
    return my_feed(), 200
```

The decorator `@required_token` will validate to token automatically and if the token is not valid, the fictitious function `my_feed()` will not be executed.
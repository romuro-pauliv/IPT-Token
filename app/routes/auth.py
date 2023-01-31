# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                             IPToken.routes.auth.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from flask import Blueprint
from iptoken.module_iptoken import IPToken
# |--------------------------------------------------------------------------------------------------------------------|

bp = Blueprint('auth', __name__, url_prefix="/auth")


@bp.route('/login', methods=["GET"])
@IPToken.generate_token(200)
def login() -> tuple[str, int]:
    return "Hello", 200


@bp.route("/feed", methods=["GET"])
@IPToken.required_token()
def feed() -> tuple[str, int]:
    return "World", 200
# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                   tests.iptoken.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import requests
import json
# |--------------------------------------------------------------------------------------------------------------------|

generate_token_route: str = "http://127.0.0.1:5000/auth/login"
required_token_route: str = "http://127.0.0.1:5000/auth/feed"

def test_generated_token() -> None:
    rtn = requests.get(generate_token_route)
    assert rtn.text == "Hello"
    assert rtn.status_code == 200
    assert "IPToken" in [i for i in rtn.headers.keys()]


def test_required_token() -> None:
    rtn_token = requests.get(generate_token_route).headers['IPToken']
    rtn = requests.get(required_token_route, headers={"Authorization": f"Token {rtn_token}"})
    rtn.text == "World"
    rtn.status_code == 200


def test_without_token() -> None:
    rtn = requests.get(required_token_route)
    assert rtn.text == "BAD REQUEST - TOKEN NOT INFORMED"
    assert rtn.status_code == 400
    

def test_wrong_format_token() -> None:
    rtn_token = requests.get(generate_token_route).headers['IPToken']
    rtn = requests.get(required_token_route, headers={"Authorization": f"{rtn_token}"})
    assert rtn.text == "BAD REQUEST - TOKEN"
    assert rtn.status_code == 400


def test_invalid_token() -> None:
    rtn_token = requests.get(generate_token_route).headers['IPToken']
    rtn = requests.get(required_token_route, headers={"Authorization": f"Token 12332test1233221"})
    assert rtn.text == "INVALID TOKEN"
    assert rtn.status_code == 400
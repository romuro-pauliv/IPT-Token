## IPT Token
![](https://img.shields.io/github/repo-size/romuro-pauliv/IPT-Token?style=flat-square) ![](https://img.shields.io/github/last-commit/romuro-pauliv/IPT-Token?style=flat-square) ![](https://img.shields.io/github/license/romuro-pauliv/IPT-Token?style=flat-square)

The IPT Token module is intended to be an extension to your Flask applications. The module will generate a token with a simple `@generate_token()` decorator set in your route depending on the status code you enter. Then request of this token can be done by `@required_token()` defined in routes that require authentication.

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
---

### Summary

- [Quickstart](https://github.com/romuro-pauliv/IPT-Token/tree/main/package#iptoken)
    - [Import & Use](https://github.com/romuro-pauliv/IPT-Token/tree/main/package#installation)
- [How the IPT Token works](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/IPT-Token-works.md#how-the-ipt-token-works)
    - [Generate Token](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/IPT-Token-works.md#generate-token)
    - [Required Token](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/IPT-Token-works.md#required-token)

---


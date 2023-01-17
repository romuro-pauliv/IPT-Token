## IPT Token

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
----
### Summary

- [Why use IPT Token](https://github.com/romuro-pauliv/IPT-Token#why-use-ipt-token)
- Quickstart
    - Import & Use
- [How the IPT Token works](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md)
- [Generate Token]()
    - [Structure and Encryption](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md#structure-and-encryption)
    - [HTTP packet IP requirement](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md#http-packet-ip-requirement)
    - [Function parameters](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md#function-parameters)
- [Required Token](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md#required-token)
    - [Structure and Decryption](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md#structure-and-decryption)
    - [Remote address validation](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md#remote-address-validation)
    - [Function parameters](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/md/IPT-Token-works.md#function-parameters-1)
- Requirements and installation

---


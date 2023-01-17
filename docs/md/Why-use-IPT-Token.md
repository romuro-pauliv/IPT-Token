## Why use IPT Token

The standard method of user validation using browser caching and session allocation in server RAM may be unusual for some processes that require a high level of security and a high load of requests to the server. On a gigantic request scale, allocating strings containing the Id of the active user on the server may impact other processing, affecting all users on the network. Also, storing the user cache without further validation can open a loophole for Browser Cache Poisoning.


![Session Mode](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/img/session_mode.png?raw=true)
> Session Type - fig.(1)

With IPT Token there is no memory allocation in the server to remember the user. At the moment the authentication HTTP package is sent (in this case we can say that it will be the login credentials). The `@generate_token` function will request the user's IP address and if the login is authorized, the IPToken will be concatenated in the server's response header.

The IPT Token will be cached by the user so the next request (like logging into your social network feed) the user's back-end will send the token in the request header.

![Token Mode](https://github.com/romuro-pauliv/IPT-Token/blob/main/docs/img/ipt_token_mode.png?raw=true)
> Token Type - fig.(2)

When the HTTP package is docked at the server, the IPT Token will be required and decrypted. After decryption, the IP address of the HTTP package that arrived in the request will be compared with the IP encrypted in the token, validating the user efficiently. Furthermore the server's memory will not be used in this process, only its processing, which will be momentary and will not affect other vital server processes.

---
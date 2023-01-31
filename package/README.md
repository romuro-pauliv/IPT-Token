# IPToken

The code implements a `JWT` (JSON Web Token) token generation and token authentication feature in `Flask` routes. The feature allows routes to be protected with a generated token with information such as the user's **IP address** and the **validity** of the token. Furthermore, the token can be customized with additional arguments. The IPToken class contains two decorators: 
- `@generate_token` is used to generate tokens and add them to the response header of a specific route (which has a certain HTTP status code). 
- `@required_token` is used to protect routes that require token authentication. If a token is provided in the request, its validity is checked by comparing its encoded IP address with the IP address of the current request.

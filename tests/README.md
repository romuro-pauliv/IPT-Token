# Tests

To run the tests you will need to run the flask application and the run the tests. You will need to install some dependencies. To perform all the steps correctly, follow the steps below:

### Virtual development environment

You need to create a virtual development environment to avoid package conflicts and other errors. You can see how it is create [here](https://docs.python.org/3/library/venv.html). After creating the environment and running the commands `source venv/bin/activate` (Linux), `venv\Script\activate` (Windows), run:

- **Install the requirements**
```
pip install -r requirements.txt
```

- **Run Flask Application**
```
flask --debug run
```

- **Run Pytest**
```
pytest -v tests/test_iptoken.py
```

If everthing is in agreement, pytest will return the following message:

```
collected 5 items                                                                                           
tests/tests_iptoken.py::test_generated_token PASSED                                                   [ 20%]
tests/tests_iptoken.py::test_required_token PASSED                                                    [ 40%]
tests/tests_iptoken.py::test_without_token PASSED                                                     [ 60%]
tests/tests_iptoken.py::test_wrong_format_token PASSED                                                [ 80%]
tests/tests_iptoken.py::test_invalid_token PASSED                                                     [100%]
```
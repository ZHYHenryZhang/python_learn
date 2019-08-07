## python testing using pytest

### Basic

Write test function with named test_*() or *_test() and excute

```
pytest filename
```

Pytest will automatically find and excute the tests.

### Extend:
#### running slow test

Pytest will capture the output and print them all at once, the problem is when the test is slow, we have to wait for the testing finish.
A work-around is using --capture=no

```
pytest --capture=no slow_test_print.py
```

#### running specified test
You can using the namespace :: to specify the function you want to test, without running all tests.

```
pytest -v test_realistic_two_funcs.py::test_2_that_does_not
```

#### fixtures
Think about fixtures as the things you need to set up before tests or clean up after tests, i.e. temp files, temp direcotries, a port.

So when do we need fixtures?
 - module level
 - class level
 - function level
 - method level.

Following functions, if defined, will be run automatically before and after the testing of a module.

```
def setup_module(module):
    ...

def teardown_module(module):
    ...
```

Following functions, if defined, will be run automatically before and after the class being tested.

```
def TestClass:
    
    @classmethod
    def setup_class(cls):
        ...
    
    @classmethod
    def teardown_class(cls):
        ...
```

Fixtures can be chained or function can request multiple fixtures.

Wrapping testing functions/methods using different fixtures into separate modules/classes is a good practice.


### Reference
1. pythontesting.net
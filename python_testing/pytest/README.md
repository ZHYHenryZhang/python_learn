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
pytest --capture=no pytest/slow_test_print.py
```



### Reference
1. pythontesting.net
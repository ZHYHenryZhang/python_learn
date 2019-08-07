## python testing using standard module doctest

It is really nice that when we write a short demo of how to use our function in docstring, python can actually run the demo and compare the output to the expected output in the demo.

### Basic

with a python function like this.
```
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
```
excute
```
python -m pytest -v doctest_simple.py
```

You will see
```
Trying:
    my_function(2, 3)
Expecting:
    6
ok
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    doctest_simple
1 items passed all tests:
   2 tests in doctest_simple.my_function
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

Note that if you don't add -v, you might see nothing if the test pass.

Check reference 1 for more features like handling ambigious output, blankline, whitespace.

reference: 
1. https://pymotw.com/3/doctest/
2. pythontesting.net
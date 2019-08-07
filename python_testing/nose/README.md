## extending unittest to make it easier

### Basic

test code is simple as pytest, without boilerplate.

```
from unnecessary_math import multiply
 
def test_numbers_3_4():
    assert multiply(3,4) == 12 
 
def test_strings_a_3():
    assert multiply('a',3) == 'aaa' 
```

run nosetest

```
nosetests -v test_um_nose.py
```

you will see the output

```
test_um_nose.test_numbers_3_4 ... ok
test_um_nose.test_strings_a_3 ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

reference
1. pythontesting.net 
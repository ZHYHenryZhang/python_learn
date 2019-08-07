## python testing using standard module unittest

### Basics

write the following into test_um_unittest.py

```
import unittest
from unnecessary_math import multiply
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')
 
if __name__ == '__main__':
    unittest.main()
```

excute

```
python test_um_unittest.py -v
```

or

```
python -m unittest test_um_unittest.py -v
```

You will see
```
test_numbers_3_4 (__main__.TestUM) ... ok
test_strings_a_3 (__main__.TestUM) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

run following command for running all tests in a directory

```
python -m unittest discover dir/
```

reference
1. pythontest.net
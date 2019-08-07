"""
use nosetest -s test_um_nose_fixtures.py

> nosetests -s test_um_nose_fixtures.py
....
setup_module before anything in this file
setup_class() before any methods in this class
TestUM:setup() before each test method
test_numbers_5_6()  <============================ actual test code
TestUM:teardown() after each test method
TestUM:setup() before each test method
test_strings_b_2()  <============================ actual test code
TestUM:teardown() after each test method
teardown_class() after any methods in this class
my_setup_function
test_numbers_3_4  <============================ actual test code
my_teardown_function
my_setup_function
test_strings_a_3  <============================ actual test code
my_teardown_function
teardown_module after everything in this file
 
----------------------------------------------------------------------
Ran 4 tests in 0.001s
 
OK
"""


from nose import with_setup # optional
 
from unnecessary_math import multiply
 
def setup_module(module):
    print ("") # this is to get a newline after the dots
    print ("setup_module before anything in this file")
 
def teardown_module(module):
    print ("teardown_module after everything in this file")
 
def my_setup_function():
    print ("my_setup_function")
 
def my_teardown_function():
    print ("my_teardown_function")
 
@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    print 'test_numbers_3_4  <============================ actual test code'
    assert multiply(3,4) == 12
 
@with_setup(my_setup_function, my_teardown_function)
def test_strings_a_3():
    print 'test_strings_a_3  <============================ actual test code'
    assert multiply('a',3) == 'aaa'
 
 
class TestUM:
 
    def setup(self):
        print ("TestUM:setup() before each test method")
 
    def teardown(self):
        print ("TestUM:teardown() after each test method")
 
    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")
 
    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")
 
    def test_numbers_5_6(self):
        print 'test_numbers_5_6()  <============================ actual test code'
        assert multiply(5,6) == 30
 
    def test_strings_b_2(self):
        print 'test_strings_b_2()  <============================ actual test code'
        assert multiply('b',2) == 'bb'
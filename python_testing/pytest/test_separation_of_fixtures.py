'''
separation of fixtures into class or modules provide the convenience that we only load what we need
when we are running part of the tests.
'''

from __future__ import print_function
 
def resource_a_setup():
    print('resources_a_setup()')
 
def resource_a_teardown():
    print('resources_a_teardown()')
 
class TestClass:
 
    @classmethod 
    def setup_class(cls):
        print ('\nsetup_class()')
        resource_a_setup()
 
    @classmethod 
    def teardown_class(cls):
        print ('\nteardown_class()')
        resource_a_teardown()
 
    def test_1_that_needs_resource_a(self):
        print('\ntest_1_that_needs_resource_a()')
 
     
def test_2_that_does_not():
    print('\ntest_2_that_does_not()')
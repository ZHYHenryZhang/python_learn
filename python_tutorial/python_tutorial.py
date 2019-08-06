''' notes on python tutorial 3.7

Author: Henry
Data: July 20, 2019
'''

import math
import sys

state = "going through python tutorial"
section = 0


""" 1
    for appitite
    """
section += 1

""" 2
    interpreter
    """
section += 1
### interpreter

# NOTE: Ctrl + D for quit() or exit()

# what is a tty device

# NOTE: python -c command [arg]
# NOTE: eg. python -c "print(1+1)"    result: 2

# TODO: try this
# python -m module [arg] to invoke module

# NOTE: enter interactive mode after excution
# NOTE: python -i script

import sys
print(sys.argv)

# NOTE: sys.argv[0] can tell how the code is invoked.
# empty string means interactive mode without script and arg
# file name means scripts being run.
# '-' means standard input TODO: what is the difference
# '-m' means module
# '-c' means command

## interactive mode

# python interpreter prompts for the next command with the primary prompt.
# for continues lines it prompts with the secondary prompts, by default three dots (...)
# Encoding:
# -*- coding: encoding -"-
# in the first line except for UNIX "shebang" line
#!/usr/bin/env python3

""" 3
    An Informal Introduction
    """
section+=1
### Using Python as a Calculator

## Numbers

# command in python starts with a hash character.
text = "#this is not a comment"
print(text)
print( 8 / 5) # NOTE: division always returns a floating point number
print( 8 // 5) # floor division
print( 8 % 5) # remainder
print( 5 ** 2) # power
print( 2 ** 2 ** 2 ** 2 ) # NOTE: if you add two more, pay attention to your memory
# NOTE: in interactive mode, _ is the last result.
# TODO: python support Decimal, Fraction, complex numbers.
# TODO: python number limit

### Strings
print('"Isn\'t," they said.')

# NOTE: r for raw string
print(r"raw string \'\"\n\t") # NOTE

# NOTE: string literals will auto concatenate
str232 = 'an ' 'auto ' 'concatenated ' 'string' # NOTE
print(str232)
print('1' '2')

# slides excluded the end
print(str232[:5], " " , str232[5:])
# >>> str232[2:5]
# 'aut'
# >>> str232[5:2]
# ''
# >>> str232[-5:-2]
# 'tri'
# >>> str232[-2:-5]
# ''

# NOTE: index out of range will return error
# NOTE: slice out of range will return till the end (gracefully)
# NOTE: strings are immutable ( cannot be changed)

## 3.1.3 Lists

def list313():
  # list operation returns a shallow copy of list
  list1 = [1, 2, 3, 4]
  list2 = list1[0:3]
  list2[0] = 10
  print(list1[0])

  # NOTE: shallow copy do not support copy the item that are reference, such as a list, an usef-defined object.
  listoflist1 = [[1,2], [3,4]]
  list3 = listoflist1[0:]
  list3[0][0] = 10
  print(listoflist1[0][0])

  # remove part of the list
  print(list1)
  list1[1:] = []
  print(list1)

list313()

### 3.2 first step towards programming

def first_step_toward_programming_3_2():
  # multiple assignment
  a, b = 0, 1
  print(a, b)

  print( bool(1))
  print( bool(-1))
  print( bool(0))
  print( bool(0.1))
  print( bool(0.0))

  # NOTE: any sequence with none zero length is true, empty is false
  print( bool([])) # NOTE
  print( bool([0])) # NOTE
  print( bool("")) # NOTE
  print( bool("0")) # NOTE

  # NOTE: print handles space insertion between arguments
  print("space", "is", "automatically", "inserted")

  # change the end with keyword argument "end"
  print("hello", end='***')
  print("world")


first_step_toward_programming_3_2()

""" 4
    More Control Flow Tools
    """
section += 1

def control_flow():

  def if_statement():
    x = 2 # NOTE: int(input("Please enter an integer: "))
    if x < 0:
      x = 0
      print("negative changed to zero")
    elif x == 0:
      print("Zero")
    elif x == 1:
      print("One")
    else:
      print("More")
    # else part is optional
    # NOTE: if elif elif is a substitute for switch or case statements in other language
  if_statement()

  def for_statement():
    print("for statement")
    # NOTE: if you may modify the sequence you are iterating over, it is recommended that you make a copy.
    words = ['hello', 'world', 'this is so great']
    print(words)

    for w in words[:]:
      if len(w) > 6:
        words.insert(0, w)
    print(words)

    # what is the problem here?
    for w in words:
      if len(w) > 6:
        words.insert(0, w)
      if len(words) > 10:
        break
    print(words)
    # BUG: the list is changing and it will continue going through
    # the same item.
    # NOTE: using slice can be handy for creating a new list here.

  for_statement()

  def range_function():
    print("range function")
    # range behave like a iterable list but it is not
    # print it you will see
    print(range(10))

    # NOTE: range() is an iterable object that will produce successive items until the supply is exhausted. To save space
    # NOTE: iterator like for statement or list() can iterate over it.
    print(list(range(5)))
  
  range_function()

  def else_in_loop():
    # NOTE: for ... else ... pair, else clause excuted when no break happens
    print("else_in_loop")
    for n in range(2, 10):
      for x in range(2, n):
        if n % x == 0:
          print(n, 'equals', x, '*', n/x)
          break
      else:
        print(n, "is a prime number")
  
  else_in_loop()

  def pass_statement():
    # NOTE: pass is useful as a placeholder for thinking of abstraction rather than implement all
    def not_implemented_function():
      pass
    
    class MyEmptyClass:
      pass
  
  pass_statement()

  def functions_definition():
    def plus_one_int(x):
      return x + 1
    
    # NOTE: functions can be renamed
    p = plus_one_int
    print(p(2))
  
  functions_definition()

  def default_arguments():
    print("!!!default will be evaluated once")
    # NOTE: BUG: default arguments are mutable, if you modify them, it will change over time
    def func(a, L=[],P=1):
      P += 1
      L.append(a)
      L.append(P)
      return L
    
    print(func(1))
    print(func(2))
    print(func(3))

    # alternatively, use other data structure to prevent this
    def func_better(a, L=None):
      if L is None:
        L = []
      L.append(a)
      return L
    
    print(func_better(1))
    print(func_better(2))
    print(func_better(3))

  default_arguments()

  def arguments_tuple_and_dict():
    """ function argument *arg receives tuple and **keywords recieves dict """
    # ideas from mother's lovely nick names.
    def piggies_arg(*arguments):
      for arg in arguments:
        print(arg, 'is a piggy')
    
    def piggies_keyword(**keywords):
      for kw in keywords:
        print(kw, ":", keywords[kw])

    # NOTE: *arg for accepting a tuple and **arg for accepting keyword arguments.
    def piggies(*arguments, **keywords): # NOTE
      for arg in arguments:
        print(arg, 'is a piggy')
      for kw in keywords:
        print(kw, ":", keywords[kw])
    
    piggies_arg("Dad", "I", "brother")
    piggies_keyword(piggy1="Dad", piggy2="I", piggy3="brother")
    piggies("Dad", "I", "brother")
    piggies("Dad", "I", "brother", piggy1="Dad", piggy2="I", piggy3="brother")

  arguments_tuple_and_dict()
  
  def unpack_argument_lists():
    print(list(range(3, 6))
    )# NOTE: * can unpack arguments in a list or a tuple.
    args = [3, 6]
    print(list(range(*args)))
    args_2 = (3, 6)
    print(list(range(*args_2)))

  unpack_argument_lists()

  def lambda_expression():
    # NOTE: lambda expressions are small anonymous functions.
    # they are helpful creating simplt functions
    # NOTE: You can return a lambda expression or pass it as an argument.
    def make_incrementor(n):
      return lambda x: x + n
    
    f = make_incrementor(100)
    print(f(0))
    print(f(1))

    pairs = [(1, 'one'), (4, 'four'), (2, 'two'), (3, 'three')]
    print(pairs)
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)
  
  lambda_expression()

  def documentation_strings():
    def my_function():
      """ Do Nothing, but document it.

      No, really, it doesn't do anything
      """
      pass
    
    # NOTE: you can get the documentation string by func_name.__doc__
    print(my_function.__doc__)
  
  documentation_strings()

  def function_annotations():
    # NOTE: function annotations: def dup_list(template_list: list, times: float) -> list:
    def dup_list(template_list: list, times: float) -> list:
      print("input template_list is of type:", type(template_list))
      return template_list * times
    
    # NOTE: function annotations is stored in func.__annotations__
    print(dup_list.__annotations__)
    print(dup_list([1,2,3], 2))
    # NOTE: annotations will not enforce any type check, totally optional.
    print(dup_list((1,2,3), 2))
  
  function_annotations()

  def coding_style():
    # Use 4 space indent rather than tabs.
    # Wrap lines so that they don't exceed 70 characters.
    # Use blank lines to separate funcitons, classes and large blocks of code inside functions.
    # NOTE: When possible, put comments on a line of their own.
    # Use docstrings.
    # Use spaces around operators and after commas, but not directly inside bracketing constructs.
    # UpperCamelCase for classes and lowercase_with_underscores for functions and methods.
    pass

  coding_style()

control_flow()

""" 5. Date Structures
"""
section += 1

def data_structures_5():
  def list_5_1():
    def list_methods():
      num_list = [1, 2, 3]
      print(num_list)
      num_list.extend(range(4, 7))
      print(num_list)
      # NOTE: list.extend(iterable) is equivalent to a[len(a):] = iterable
      num_list[len(num_list):] = range(7, 9)
      print(num_list)

      # NOTE: list.remove(x) will remove item with value x
      num_list.remove(1)
      print(num_list)
      
      # NOTE: list.pop(i) will remove i-th item at position i and return it.
      print(num_list.pop(1))
      print(num_list)

      # NOTE: list.index(x[, start[, end]]) return index of x
      print(num_list.index(6, 2))

      # NOTE: list.count(x) return the number of times x appears.
      print(num_list.count(5))

      # NOTE: list.copy() returns a shallow copy of the list, Equivalent to a[:]

    list_methods()

    def lists_as_stacks_5_1_1():
      # using list as stack is easy, append and pop are fast
      pass
    
    lists_as_stacks_5_1_1()

    def lists_as_queues_5_1_2():
      # NOTE: using lists as queues is possible but not efficient.
      # NOTE: from collections import deque and use append and popleft for quene.
      from collections import deque
      qeque = deque([1,2,3])
      print(qeque)
      qeque.append(4)
      print(qeque)
      qeque.popleft()
      print(qeque)
    
    lists_as_queues_5_1_2()

    def list_comprehensions():
      squares_1 = list(map(lambda x: x**2, range(5)))
      squares_2 = [x**2 for x in range(1,6)]
      print(squares_1)
      print(squares_2)

      # NOTE: A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
      # NOTE: list comprehension would be the same order of the expension.
      same_item_tuple = [(x, y) for x in squares_1 for y in squares_2 if x==y] # NOTE
      print(same_item_tuple)

      list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
      flattened_list = [y for x in list_of_list for y in x]
      print(flattened_list)

      transpose = []
      for rows in list_of_list:
        if len(transpose) == 0:
          for item in rows:
            transpose.append([item])
        else:
          for index, item in enumerate(rows):
            transpose[index].append(item)
      
      print(transpose)
      
      transpose = [[list_of_list[row_id][col_id] for row_id in range(len(list_of_list))] for col_id in range(len(list_of_list[0]))]
      print(transpose)

      # NOTE: nested list comprehension is allowed
      transpose = [[row[i] for row in list_of_list] for i in range(len(list_of_list[0]))] # NOTE
      print(transpose)

      # NOTE: you should prefer built-in functions
      transpose = list(zip(*list_of_list)) # NOTE: transpose matrix
      print(transpose)



    list_comprehensions()


  list_5_1()

  def del_statement_5_2():
    # NOTE: you can use the del statement to remove iten, slice or list.
    a = [x for x in range(8)] # BUG: [range(8)] will not give you a list of numbers, it will contain a single iterable.
    print(a)
    del a[0]
    print(a)
    del a[2:5]
    print(a)
    del a[:]
    print(a)
    del a

    b = 1
    del b
  
  del_statement_5_2()

  def tuples_and_sequences_5_3():
    list_1 = [1, 2, 3]
    list_2 = ['hello', 'world', 'good' 'morning']
    tuple_1 = (list_1, list_2)
    print(tuple_1)
    # NOTE: tuples are immutable, but they can contain mutable objects.
    tuple_1[0][2] = 100 # NOTE think about pointers, address not changed, but the content in the address can be changed.
    print(tuple_1)

    # NOTE: create an empty tuple by () and one-element tuple by adding a comma.
    empty = ()  # NOTE
    singleton = 'single', # NOTE
    print(empty)
    print(singleton)

    # tuple packing and unpacking
    x, y, z = 0, 1, 2
    t = x, y, z
    x2, y2, z2 = t
    print(t, x2, y2, z2)

  tuples_and_sequences_5_3()

  def sets_5_4():
    # NOTE: create a set by {elements} or set(elements), empty set must be created by set().
    basket = {'apple', 'banana', 'orange', 'pear', 'apple', 'peach'}
    print(basket)
    print('bean' in basket)
    basket.add('bean')
    print(basket)
    basket.add('apple')
    print(basket)

    a = set('hello, world')
    b = set('I love you')
    print(a)
    print(b)
    print(a - b)  # in a not in b
    print(a | b)  # in a or in b
    print(a & b)  # in a and in b
    print(a ^ b)  # in a not in b or in b not in a

    c = {x for x in a if x not in b} # NOTE: set comprehension
    print(c)

  sets_5_4()

  def dictionaries_5_5():
    # NOTE: keys of dictionary can be any immutable type, like strings, numbers and tuples that contain only immutable type.
    # NOTE: It is best to think of a dictionary as a set of key.
    tel = {'Police': 110, 'Fire': 119, 'Ambulence': 120}
    print(tel)
    tel['Fire'] = 110
    del tel['Ambulence'] # NOTE: remove a key value pair
    tel['Ambulence'] = 110
    print(tel)
    print(list(tel))
    print(sorted(tel)) # NOTE: directly get sorted keys
    
    dic_comp = {x: x**2 for x in range(6)} # NOTE: dictionary comprehension
    print(dic_comp)
    
    # NOTE: when keys are simple strings, it is easier to create a dictionary using keyword arguments.
    dic_simple = dict(dad=123, mom=456) # NOTE
    print(dic_simple)
  
  dictionaries_5_5()

  def looping_techniques_5_6():
    tel = {'Police': 110, 'Fire': 110, 'Ambulence': 110}
    # NOTE looping throught dictionaries using items() method
    for key, value in tel.items(): # NOTE
      print(key, 'number is:', value)

    seq = [x for x in range(7)]
    # NOTE: using the enumerate function to get index when looping through sequences
    for index, value in enumerate(seq):
      print(index, value)

    seq_2 = [y for y in range(-7, -1)]
    # NOTE: use zip() to loop over two sequences simultaneously, ends when anyone ends.
    for x, y in zip(seq, seq_2):
      print(x, y)
    
    # NOTE: loop over the reversed sequence
    for x in reversed(seq):
      print(x, end=', ')
    print()
    
    for y in sorted(seq_2):
      print(y, end=', ')
    print()

    # NOTE: It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN')]
    filtered_data = [value for value in raw_data if not math.isnan(value)]
    print(filtered_data)
  
  looping_techniques_5_6()

  def more_on_conditions_5_7():
    a, b, c, d = 1, 2, 3, 4
    if a < b <= c <= d: # NOTE: condiition can be chained
      print('chained')
    # NOTE: 'not' has a higher priority than 'and', 'or' has the lowest priority.
    print(c > d or not a > b and b < c) # NOTE: (c > d) or ((not a > b) and b < c)

    # NOTE: The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined.

    # NOTE: Assignment cannot occur inside expressions, it avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.
       

  more_on_conditions_5_7()

  def comparing_sequences_and_others_5_8():
    # NOTE: Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering, recursively from left to right.
    pass
  
  comparing_sequences_and_others_5_8()

data_structures_5()

""" 6.Modules
"""
section += 1

def modules_6():
  def more_on_modules_6_1():
    # A module is a file containing definitions and statements.
    # within a module, the modules's name is available as the value of the global variable __name__
    # NOTE: print '__main__' running this script and print 'python_tutorial' if imported as a module.
    print(__name__) # NOTE
    # modules are only imported once per interpreter session for efficiency.
    # NOTE: if __name__ == "__main__": will make the following code run only when this files is excuted
    # NOTE: as script, not as imported module. which provides a convenient user interface to a module.
    # NOTE: module search path: built-in first, then sys.path
    # NOTE:   directory containing the input script
    # NOTE:   PYTHONPATH
    # NOTE:   installation-dependent default 
    # NOTE: __pycache__ stores compiled version of each module with name module.version.pyc
  more_on_modules_6_1()

  def standard_modules_6_2():
    pass
  
  standard_modules_6_2()

  def the_dir_function_6_3():
    # NOTE: the built-in function dir() is used to find out which names a module defines.
    # NOTE: without arguments, dir() lists the names you have defined in this scope currently.
    only_one_in_this_scope = "nothing"
    print(dir())
  the_dir_function_6_3()
  
  print(dir())
  
  def packages_6_4():
    # NOTE: Packages are a way of structuring Python's module namespace by using 'dotted module names'.
    # NOTE: __init__py files re required to make python treat directories containing the file as packages.
    # NOTE: __init__py can be empty file, it can also execute initialization code for the package or set __all__ variable.
    # NOTE: from module import function will make the function available, but module is also loaded, but not available.
    from mydataproc.create import rand_int_positive
    size = [2, 2]
    # randint = mydataproc.create.rand_int_neutral(size) # BUG: name not defined
    # print(randint)
    # NOTE: __all__ = ['module1',...] defines the behavior of from package import * 
    # NOTE: Intra-package reference, absolute import package.submodule.subsubmodule
    # NOTE: or you can relative import: from . import module in current directory, or .. for parent.
    # NOTE: from ..subpackage import module refers import module from a subpackage in the parent directory.
    # NOTE: __path__ is a list containing the name of the directory holding the packages's __init__.py
    import mydataproc
    print(mydataproc.__path__)
  packages_6_4()

modules_6()

''' 7. Input and output
'''
section += 1

def input_and_output_7():
  def fancier_output_formatting_7_1():
    def formatted_string_literals_7_1_1():
      
      # NOTE: f-string use f before string and brackets for variables
      # print(f'the value of pi is approximately {math.pi:.3f}.') # NOTE: supported from 3.6
      # NOTE: passing an integer after the ':' will cause that field to be a minimum number of characters wide.
      food = dict(tomato=1, rice=2, sausage=3, egg=4)
      # for ingredient, num in food.items():
      #   print(f'{ingredient:10}==>{num:10}') 
      # NOTE: Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
      # print(f'{animals!r}) # NOTE

    formatted_string_literals_7_1_1()

    def the_string_format_method_7_1_2():
      # NOTE: A number in the brackets can be used to refer to the position of the object passed into the str.format() method
      print('{1} and {0}'.format('first','second')) # NOTE: will print 'second and first'
      # NOTE: keyword argument can be used in format() method
      print('{food} and {study}, {0}'.format('zero', food='first', study='second')) # NOTE
      # NOTE: pass a dictionary as argument of format() method
      table = {'Sjoerd':4127, 'Jack':4098, 'Dcab': 8637}
      print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
      print('Jack: {Jack:d}; Sjeord: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

    the_string_format_method_7_1_2()

    def manual_string_formatting_7_1_3():
      # NOTE: you can use rjust, zfill to format your string
      for i in range(10):
        print(repr(i).rjust(2), repr(i*i).rjust(3), repr(i**3).rjust(4)) # NOTE
      minute = 9
      second = 1
      print('time is', repr(minute).zfill(2)+':'+repr(second).zfill(2)) # NOTE
    
    manual_string_formatting_7_1_3()

    def old_string_formatting_7_1_4():
      # NOTE: % operator format the string like sprintf-stype() string
      print('The value of pi is approximately %5.3f.' % math.pi)
    
    old_string_formatting_7_1_4()

  fancier_output_formatting_7_1()

  def reading_and_writing_files_7_2():
    # NOTE: it is a good practice to use the with keyword when dealing with file objects. It will be closed properly.
    with open('data.txt','r') as f: # NOTE
      data = f.readlines()
      for line in data:
        print(line.split())
    print(f.closed)

    def methods_of_file_objects_7_2_1():
      # NOTE: For reading lines from a file, you can loop over the file object. This is memory efficient, fast and simple.
      with open('data.txt','r') as f:
        for line in f: # NOTE
          print(line, end='') # NOTE: lines will include the '\n', so we set print() ends with nothing
      print()
      # NOTE: you can also use list(f) or f.readlines()

      # NOTE: f.write(str) write a string, f.tell() returns the position, f.seek changes the position
      with open('data.txt','r+') as f:
        print(f.tell())
        print(f.seek(0, 2)) # NOTE: offset=0, from_what = 2 as end of the file, 0 as beginning, 1 as current position.
        print(f.write('hi 2'))
    
    methods_of_file_objects_7_2_1()

    def saving_structured_data_with_json_7_2_2():
      # NOTE: The standard module called json can take python data hierachies, and convert them to string representations.
      import json
      data = [1, 'simple', 'list']
      print(json.dumps(data)) # NOTE
      with open('object.json', 'w+') as f:
        json.dump(data, f) # NOTE: directly write into text file
      with open('object.json', 'r') as f:
        data_loaded = json.load(f) # NOTE: write into file
        print(data_loaded)
      # NOTE: pickle allow you to write arbitrarily complex python objects, whick make it dangerous and only python specific

    saving_structured_data_with_json_7_2_2()
  
  reading_and_writing_files_7_2()

input_and_output_7()

''' 8. Errors and Exceptions
'''
section += 1

def errors_and_exceptions_8():
  def syntax_errors_8_1():
    # NOTE: syntax error is also known as parsing error, is caused by the token preceding the arrow
    pass

  syntax_errors_8_1()

  def exceptions_8_2():
    # NOTE: exception types are printed as part of the messsage
    pass
  
  exceptions_8_2()

  def handling_exceptions_8_3():
    # NOTE: the code between try and except is excuted, if no error, except is skipped.
    # NOTE: if error occurs, see if except matches the exception, if yes, go excute that, if not look for outer try.
    # NOTE: a try statement can have multiple except statement in multiple line or a tuple.
    while True:
      try:
        x = int(input("Please enter a number: "))
        break
      except ValueError:
        print("Oops! That was not a valid number. Try again ... ")
      except KeyboardInterrupt:
        print('get key board interupt')
        break
    
    class B(Exception):
      pass

    class C(B):
      pass

    class D(C):
      pass

    for cls in [B, C, D]:
      try:
        raise cls()
      except D:
        print("D")
      except C:
        print("C")
      except B:
        print("B")
    
    for cls in [B, C, D]:
      try:
        raise cls()
      except B:
        print("B")
      except C:
        print("C")
      except D:
        print("D")
    # NOTE: exception will be handled by the first match

    try:
      f = open('data.txt')
      s = f.readline()
      i = int(s.strip())
    except OSError as err: # NOTE: The except clause may spepcify a variable after the exception name, which is bounded to an exception instance.
      print("OS error: {0}".format(err)) # NOTE: for convenience, the exception instance defines __str__() so they can be printed directly
    except ValueError:
      print("Could not convert data to an integer.")
    except: # NOTE: last except can omit errortype, which is dangerous.
      print("Unexpected error:", sys.exc_info()[0]) # NOTE: print error info
      raise

    # NOTE: try ... except statement has an optional else clause, which is useful for code that must be excuted if the try clause does not raise an exception.
    # NOTE: it is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn't raised by the code that needs to be protected.

    filename = 'data1.txt'
    try:
      f = open(filename, 'r')
    except OSError:
      print('cannot open', filename)
    else:
      print(filename, 'has', len(f.readlines()), 'lines') # NOTE: get number of lines
      f.close()
    # NOTE: If an exception has arguments, they are printed as the last part (‘detail’) of the message for unhandled exceptions.
    # NOTE: Exception handlers don't just handle exceptions if they occur immediately in the try clause, but also if they occer inside functions that are called (even indirectly) in the try clause.

    def this_fails():
      x = 1/0
      print("will not print")
    
    try:
      this_fails()
    except ZeroDivisionError as err:
      print("Handling err {} here".format(err))

  handling_exceptions_8_3()

  def raising_exceptions_8_4():
    # NOTE: raise statement allows the programmer to force a specfied exception to occer.
    # NOTE: the exception to be raised can be an exception instance or an exception class (a class derives from Exception)
    try:
      try:
        raise NameError('HiThere')
      except NameError:
        print('an exception flew by!')
        raise # NOTE: use this to raise the error again
    except NameError:
      pass

  raising_exceptions_8_4()

  def user_defined_exceptions_8_5():
    # NOTE: User-defined exceptions should typically be derived from the Exception class, either directly or indirectly.
    try:
      try:
        raise KeyboardInterrupt
      finally:
        print("good bye")
    except KeyboardInterrupt:
      pass
    

  
  user_defined_exceptions_8_5()

  def defining_clean_up_actions_8_6():
    # NOTE: The try statement has another optinal clause finally which is intended to define clean-up actions that must ve executed under all circumstances.
        def divide(x, y):
      try:
        result = x / y
      except ZeroDivisionError:
        print('division by zero!')
      else:
        print('result is', result)
      finally:
        print('excuting finally')
    
    
    divide(2, 1)
    try:
      divide(2, 0)
    except KeyboardInterrupt:
      pass
    try:
      divide('2', '1')
    except:
      pass
  
  defining_clean_up_actions_8_6()

  def predefined_clean_up_actions_8_7():
    # with statement
    pass
  
  predefined_clean_up_actions_8_7()

errors_and_exceptions_8()

''' 9. Classes
'''
section += 1

def classes_9():
  def a_word_about_names_and_objects_9_1():
    pass
  
  a_word_about_names_and_objects_9_1()

  def python_scopes_and_namespaces_9_2():
    pass
  
  python_scopes_and_namespaces_9_2()

  def a_first_look_at_classes_9_3():
    pass

  a_first_look_at_classes_9_3()

  def random_remarks_9_4():
    pass
  
  random_remarks_9_4()

  def inheritance_9_5():
    pass
  
  inheritance_9_5()

  def private_variables_9_6():
    pass
  
  private_variables_9_6()

  def odds_and_ends_9_7():
    pass
  
  odds_and_ends_9_7()

  def iterators_9_8():
    pass
  
  iterators_9_8()

  def generators_9_9():
    pass
  
  generators_9_9()

  def generator_expressions_9_10():
    pass
  
  generator_expressions_9_10()

classes_9()

print(state, "current section is", str(section))
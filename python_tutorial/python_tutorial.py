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
    # NOTE: To rebind variables found outside of the innermost scope, the nonlocal statement can be used; if not declared nonlocal, those variables are read-only (an attempt to write to such a variable will simply create a new local variable in the innermost scope, leaving the identically named outer variable unchanged).
    # NOTE: If no global statement is in effect – assignments to names always go into the innermost scope.
    # NOTE: Assignments do not copy data — they just bind names to objects. 
    def scope_test():
      def do_local():
        spam = "local spam"

      def do_nonlocal():
        nonlocal spam # NOTE: nonlocal will make it go to outter level
        spam = "nonlocal spam"

      def do_global():
        global spam # NOTE: global will go to the outermost level.
        spam = "global spam"

      spam = "test spam"
      do_local()
      print("After local assignment:", spam)
      do_nonlocal()
      print("After nonlocal assignment:", spam)
      do_global()
      print("After global assignment:", spam)

    scope_test()
    
  
  python_scopes_and_namespaces_9_2()

  def a_first_look_at_classes_9_3():
    # NOTE: you can define a class with only statements
    class FirstClass: # NOTE
      print("FirstClass defined") # NOTE
    
    # NOTE: When a class definition is entered, a new namespace is created,
    # NOTE: When a class definition is left normally (via the end), a class object is created.
    # NOTE: The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class object is bound here to the class name given in the class definition header (ClassName in the example).
    # NOTE: Class objects support two kinds of operations: attribute references and instantiation.
    # NOTE: A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well.)
    # NOTE: previously, I think you have to have all members in __init__, it might not be true.
    # NOTE: immutable object are not shared but mutable object are shared by all instance
    class InitClass:
      attr = 1 # NOTE: not shared across instances (different id)
      class_list = [] # NOTE: shared across instances (same id)
      def __init__(self, arg):
        self.num = arg
      
      def plus(self, number):
        self.num += number
        return self.num
      
      def list_append(self, item):
        self.class_list.append(item)
    
    obj1 = InitClass(1)
    obj2 = InitClass(2)
    obj1.attr = 3
    obj1.list_append("only obj1")
    print(obj2.attr)
    print(obj2.class_list)
    # NOTE: In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.
    print(InitClass.plus(obj1, 1)) # NOTE
    print(obj1.plus(1)) # NOTE
    pass

  a_first_look_at_classes_9_3()

  def random_remarks_9_4():
    # NOTE: Data attributes override method attributes with the same name
    # NOTE: Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok.
    def outside_method(self, x, y):
      return min(x, y)
    
    class Foo:
      f_min = outside_method

      def g(self):
        return "hello, world"
      h = g
    
    # Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.
    print(math.__class__)
    print(print.__class__)
    print(Foo().__class__)
    pass
  
  random_remarks_9_4()

  def inheritance_9_5():
    class Bar:
      def g(self):
        return "hello, world"
    
    class Foo(Bar):
      f = 1
    
    print(Foo.__class__)
    print(Foo.g.__class__)
    # NOTE: Derived classes may override methods of their base classes.
    # NOTE: There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments).
    # NOTE: isinstance() to check an instance's type, use issubclass() to check class inheritance.
    print(issubclass(bool, int)) # NOTE: True since bool is derived from int.
  
    # NOTE: For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.
  
  
  inheritance_9_5()

  def private_variables_9_6():
    # NOTE: member variable with preceeding underscore are considered private by convention, but not restricted from being accessed.
    pass
  
  private_variables_9_6()

  def odds_and_ends_9_7():
    # NOTE: an empty class will be useful to bundling together a few named data items.
    class Student:
      pass
    
    john = Student()
    john.id = 1
    john.name = "John"
    print(john)

    
    # NOTE: Instance method objects have attributes, too: m.__self__ is the instance object with the method m(), and m.__func__ is the function object corresponding to the method.
    pass
  
  odds_and_ends_9_7()

  def iterators_9_8():
    # NOTE: The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object. 
    # NOTE: The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. 
    # NOTE: When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate.
    
    s = 'abs'
    it = iter(s)
    print(it)
    while True:
      try:
        print(next(it))
      except StopIteration as err:
        print("caught StopIteration error", err)
        break
    
    # This is Okay, but ugly
    class Group:

      class MemberIterator:
        def __init__(self, members):
          self.idx = -1
          self.members = members
        
        def __next__(self):
          self.idx += 1
          if self.idx >= len(self.members):
            raise StopIteration
          else:
            return self.members[self.idx]

      def __init__(self, mem):
        self.members = []
        for member in mem:
          self.members.append(member)
      
      def __iter__(self):
        itr = self.MemberIterator(self.members)
        return itr

    team = Group(["Henry", "David", "John"])
    
    itr = iter(team)
    print(next(itr))

    for member in team:
      print(member)
    
    ### NOTE: elegant inplementation of reverse iterator
    class Reverse:
      """ Iterator for looping over a sequence backwards."""
      def __init__(self, seq):
        self.seq = seq
        self.index = 0
      
      def __iter__(self):
        self.index = len(self.seq)
        return self
      
      def __next__(self):
        if self.index == 0:
          raise StopIteration
        else:
          self.index -= 1
          return self.seq[self.index]
    
    ###

    nums = [1, 2, 3, 4]
    for num in Reverse(nums):
      print(num)
    
    nums = []
    for num in Reverse(nums):
      print(num)

      
  
  iterators_9_8()

  def generators_9_9():
    # NOTE: Generators are a simple and powerful tool for creating iterators. 
    # NOTE: They are written like regular functions but use the yield statement whenever they want to return data. 
    # NOTE: Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). 

    def reverse(data):
      for index in range(len(data)-1, -1, -1):
        yield data[index]
    
    nums = [1, 2, 3, 4]
    for num in reverse(nums):
      print(num)
    
    nums = []
    for num in reverse(nums):
      print(num)
    pass
  
  generators_9_9()

  def generator_expressions_9_10():
    # NOTE: Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets.
    # NOTE: Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

    sine_table = {x: math.sin(x * math.pi / 180) for x in range(0, 91)} # NOTE

    # NOTE: unique_words = set(word for line in page for word in line.split())

    # NOTE: valensictorian = max((student.gpa, student.name) for student in graduates)


    pass
  
  generator_expressions_9_10()

classes_9()

def brief_tour_of_the_standard_library_10():
  def operating_system_interface_10_1():
    # NOTE: The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:
    import os
    dir(os)
    pass

  operating_system_interface_10_1()

  def file_wildcards_10_2():
    # NOTE: The glob module provides a function for making file lists from directory wildcard searches
    import glob
    print(glob.glob('*.py')) # NOTE
    pass
  
  file_wildcards_10_2()

  def command_line_arguments_10_3():
    print(sys.argv)
    # NOTE: The argparse module provides a mechanism to process command line arguments. It should always be preferred over directly processing sys.argv manually.
    import argparse
    from getpass import getuser
    parser = argparse.ArgumentParser(description='An argparse example')
    parser.add_argument('name', nargs='?', default=getuser(), help='The name of user')
    parser.add_argument('--verbose', '-v', action='count')
    args = parser.parse_args()
    if not args.verbose:
      print('Try run this again with multiple "-v" flages!')
    else:
      greetings = ['Hi', 'Hello', 'Nice to meet you'][args.verbose % 3]
      print('{} {}'.format(greetings, args.name))
    

  
  command_line_arguments_10_3()

  def error_output_redirection_and_program_termination_10_4():
    # NOTE: The stderr is useful for emitting warnings and error messages to make them visible even when stdout has been redirected
    sys.stderr.write('Warning, trying to write a warning!\n')
    pass

  error_output_redirection_and_program_termination_10_4()

  def string_pattern_matching_10_5():
    import re
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
    print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
    
    # NOTE: When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:
    print('tea for too'.replace('too', 'two'))
  
  string_pattern_matching_10_5()

  def mathematics_10_6():
    import random
    print(random.choice(['apple', 'pear', 'banana'])) # NOTE
    print(random.sample(range(100), 10)) # NOTE
    print(random.random()) # NOTE: random float
    print(random.randrange(6)) # NOTE: random integer
    
    data = [1, 1.1, 1, 1.05, 0.99, 0.9]
    import statistics
    print(statistics.mean(data)) # NOTE
    print(statistics.median(data)) # NOTE
    print(statistics.variance(data)) # NOTE
    print(statistics.mode(data))

  mathematics_10_6()

  def internet_access_10_7():
    from urllib.request import urlopen
    with urlopen('http://www.google.com') as response:
      for line in response:
        line = line.decode('utf-8', errors="replace")
        if 'EST' in line or 'EDT' in line:
          print(line)
        else:
          print(line)
  
  internet_access_10_7()

  def dates_and_times_10_8():
    from datetime import date
    now = date.today()
    print(now)
    # NOTE: 08-11-19. 11 Aug 2019 is a Sunday on the 11 day of August.
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")) # NOTE
    
    birthday = date(1064, 7, 31)
    age = now - birthday
    print(age.days)
    
  dates_and_times_10_8()

  def data_compression_10_9():
    import zlib
    s = b'which which has which witches wrist watch'
    print(len(s))
    t = zlib.compress(s)
    print(len(t))
    print(zlib.decompress(t))
    print(zlib.crc32(s))
  
  data_compression_10_9()

  def performance_measurement_10_10():
    # NOTE: In contrast to timeit’s fine level of granularity, the profile and pstats modules provide tools for identifying time critical sections in larger blocks of code.
    from timeit import Timer
    print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
    print(Timer('a,b = b,a', 'a=1; b=2').timeit())


  
  performance_measurement_10_10()

  def quality_control_10_11():
    # unittest and doctest is memtioned.
    pass
  
  quality_control_10_11()

  def batteries_included_10_12():
    pass
  
  batteries_included_10_12()

brief_tour_of_the_standard_library_10()

def brief_tour_of_the_standard_library_11():
  def multi_threading_11_4():
    ### NOTE: multi threading template
    import threading, zipfile
    class AsyncZip(threading.Thread):
      def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
      
      def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)
    
    background = AsyncZip('data.txt', 'data_archive.zip')
    background.start()
    print('This line should go first, main program is still running.')

    background.join() # Wait for the background task to finish
    print('Main program waited until background was done')
    ###

    # NOTE: The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. To that end, the threading module provides a number of synchronization primitives including locks, events, condition variables, and semaphores.
    # NOTE: While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. So, the preferred approach to task coordination is to concentrate all access to a resource in a single thread and then use the queue module to feed that thread with requests from other threads. Applications using Queue objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.

  multi_threading_11_4()

  def logging_11_5():
    import logging
    logging.debug('Debugging information')
    logging.info('Informational message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error -- shutting down')
    # NOTE: By default, informational and debugging messages are suppressed and the output is sent to standard error.
  logging_11_5()

  def tools_for_working_with_lists_11_7():
    # NOTE: The array module provides an array() object that is like a list that stores only homogeneous data and stores it more compactly.
    from array import array # NOTE
    a = array("H", [400, 10, 700, 2222]) # NOTE

    # NOTE: The collections module provides a deque() object that is like a list with faster appends and pops from the left side but slower lookups in the middle. These objects are well suited for implementing queues and breadth first tree searches
    from collections import deque # NOTE
    d = deque(["task1", "task2", "task3"]) # NOTE
    d.append("task4")
    print("Handling", d.popleft) # NOTE

    # NOTE: The heapq module provides functions for implementing heaps based on regular lists. The lowest valued entry is always kept at position zero. This is useful for applications which repeatedly access the smallest element but do not want to run a full list sort
    pass

brief_tour_of_the_standard_library_11()

def virtual_environments_and_packages_12():
  # NOTE: You can also install a specific version of a package by giving the package name followed by == and the version number.
  # NOTE: pip install requests==2.6.0
  # NOTE: pip list will display all of the packages installed in the virtual environment:
  # NOTE: pip freeze will produce a similar list of the installed packages, but the output uses the format that pip install expects. A common convention is to put this list in a requirements.txt file
  # NOTE: The requirements.txt can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with install -r.
  pass

virtual_environments_and_packages_12()

print("In global scope:", spam)
print(state, "current section is", str(section))
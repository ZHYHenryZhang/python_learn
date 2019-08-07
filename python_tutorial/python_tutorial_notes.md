# NOTE: Ctrl + D for quit() or exit()
# NOTE: python -c command [arg]
# NOTE: eg. python -c "print(1+1)"    result: 2
# NOTE: enter interactive mode after excution
# NOTE: python -i script
# NOTE: sys.argv[0] can tell how the code is invoked.
print( 8 / 5) # NOTE: division always returns a floating point number
print( 2 ** 2 ** 2 ** 2 ) # NOTE: if you add two more, pay attention to your memory
# NOTE: in interactive mode, _ is the last result.
# NOTE: r for raw string
print(r"raw string \'\"\n\t") # NOTE
# NOTE: string literals will auto concatenate
str232 = 'an ' 'auto ' 'concatenated ' 'string' # NOTE
# NOTE: index out of range will return error
# NOTE: slice out of range will return till the end (gracefully)
# NOTE: strings are immutable ( cannot be changed)
# NOTE: shallow copy do not support copy the item that are reference, such as a list, an usef-defined object.
# NOTE: any sequence with none zero length is true, empty is false
print( bool([])) # NOTE
print( bool([0])) # NOTE
print( bool("")) # NOTE
print( bool("0")) # NOTE
# NOTE: print handles space insertion between arguments
x = 2 # NOTE: int(input("Please enter an integer: "))
# NOTE: if elif elif is a substitute for switch or case statements in other language
# NOTE: if you may modify the sequence you are iterating over, it is recommended that you make a copy.
# BUG: the list is changing and it will continue going through
# NOTE: using slice can be handy for creating a new list here.
# NOTE: range() is an iterable object that will produce successive items until the supply is exhausted. To save space
# NOTE: iterator like for statement or list() can iterate over it.
# NOTE: for ... else ... pair, else clause excuted when no break happens
# NOTE: pass is useful as a placeholder for thinking of abstraction rather than implement all
# NOTE: functions can be renamed
# NOTE: BUG: default arguments are mutable, if you modify them, it will change over time
# NOTE: *arg for accepting a tuple and **arg for accepting keyword arguments.
def piggies(*arguments, **keywords): # NOTE
)# NOTE: * can unpack arguments in a list or a tuple.
# NOTE: lambda expressions are small anonymous functions.
# NOTE: You can return a lambda expression or pass it as an argument.
# NOTE: you can get the documentation string by func_name.__doc__
# NOTE: function annotations: def dup_list(template_list: list, times: float) -> list:
# NOTE: function annotations is stored in func.__annotations__
# NOTE: annotations will not enforce any type check, totally optional.
# NOTE: When possible, put comments on a line of their own.
# NOTE: list.extend(iterable) is equivalent to a[len(a):] = iterable
# NOTE: list.remove(x) will remove item with value x
# NOTE: list.pop(i) will remove i-th item at position i and return it.
# NOTE: list.index(x[, start[, end]]) return index of x
# NOTE: list.count(x) return the number of times x appears.
# NOTE: list.copy() returns a shallow copy of the list, Equivalent to a[:]
# NOTE: using lists as queues is possible but not efficient.
# NOTE: from collections import deque and use append and popleft for quene.
# NOTE: A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# NOTE: list comprehension would be the same order of the expension.
same_item_tuple = [(x, y) for x in squares_1 for y in squares_2 if x==y] # NOTE
# NOTE: nested list comprehension is allowed
transpose = [[row[i] for row in list_of_list] for i in range(len(list_of_list[0]))] # NOTE
# NOTE: you should prefer built-in functions
transpose = list(zip(*list_of_list)) # NOTE: transpose matrix
# NOTE: you can use the del statement to remove iten, slice or list.
a = [x for x in range(8)] # BUG: [range(8)] will not give you a list of numbers, it will contain a single iterable.
# NOTE: tuples are immutable, but they can contain mutable objects.
tuple_1[0][2] = 100 # NOTE think about pointers, address not changed, but the content in the address can be changed.
# NOTE: create an empty tuple by () and one-element tuple by adding a comma.
empty = ()  # NOTE
singleton = 'single', # NOTE
# NOTE: create a set by {elements} or set(elements), empty set must be created by set().
c = {x for x in a if x not in b} # NOTE: set comprehension
# NOTE: keys of dictionary can be any immutable type, like strings, numbers and tuples that contain only immutable type.
# NOTE: It is best to think of a dictionary as a set of key.
del tel['Ambulence'] # NOTE: remove a key value pair
print(sorted(tel)) # NOTE: directly get sorted keys
dic_comp = {x: x**2 for x in range(6)} # NOTE: dictionary comprehension
# NOTE: when keys are simple strings, it is easier to create a dictionary using keyword arguments.
dic_simple = dict(dad=123, mom=456) # NOTE
# NOTE looping throught dictionaries using items() method
for key, value in tel.items(): # NOTE
# NOTE: using the enumerate function to get index when looping through sequences
# NOTE: use zip() to loop over two sequences simultaneously, ends when anyone ends.
# NOTE: loop over the reversed sequence
# NOTE: It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
if a < b <= c <= d: # NOTE: condiition can be chained
# NOTE: 'not' has a higher priority than 'and', 'or' has the lowest priority.
print(c > d or not a > b and b < c) # NOTE: (c > d) or ((not a > b) and b < c)
# NOTE: The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined.
# NOTE: Assignment cannot occur inside expressions, it avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.
# NOTE: Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering, recursively from left to right.
# NOTE: print '__main__' running this script and print 'python_tutorial' if imported as a module.
print(__name__) # NOTE
# NOTE: if __name__ == "__main__": will make the following code run only when this files is excuted
# NOTE: as script, not as imported module. which provides a convenient user interface to a module.
# NOTE: module search path: built-in first, then sys.path
# NOTE:   directory containing the input script
# NOTE:   PYTHONPATH
# NOTE:   installation-dependent default 
# NOTE: __pycache__ stores compiled version of each module with name module.version.pyc
# NOTE: the built-in function dir() is used to find out which names a module defines.
# NOTE: without arguments, dir() lists the names you have defined in this scope currently.
# NOTE: Packages are a way of structuring Python's module namespace by using 'dotted module names'.
# NOTE: __init__py files re required to make python treat directories containing the file as packages.
# NOTE: __init__py can be empty file, it can also execute initialization code for the package or set __all__ variable.
# NOTE: from module import function will make the function available, but module is also loaded, but not available.
# randint = mydataproc.create.rand_int_neutral(size) # BUG: name not defined
# NOTE: __all__ = ['module1',...] defines the behavior of from package import * 
# NOTE: Intra-package reference, absolute import package.submodule.subsubmodule
# NOTE: or you can relative import: from . import module in current directory, or .. for parent.
# NOTE: from ..subpackage import module refers import module from a subpackage in the parent directory.
# NOTE: __path__ is a list containing the name of the directory holding the packages's __init__.py
# NOTE: f-string use f before string and brackets for variables
# print(f'the value of pi is approximately {math.pi:.3f}.') # NOTE: supported from 3.6
# NOTE: passing an integer after the ':' will cause that field to be a minimum number of characters wide.
# NOTE: Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
# print(f'{animals!r}) # NOTE
# NOTE: A number in the brackets can be used to refer to the position of the object passed into the str.format() method
print('{1} and {0}'.format('first','second')) # NOTE: will print 'second and first'
# NOTE: keyword argument can be used in format() method
print('{food} and {study}, {0}'.format('zero', food='first', study='second')) # NOTE
# NOTE: pass a dictionary as argument of format() method
# NOTE: you can use rjust, zfill to format your string
print(repr(i).rjust(2), repr(i*i).rjust(3), repr(i**3).rjust(4)) # NOTE
print('time is', repr(minute).zfill(2)+':'+repr(second).zfill(2)) # NOTE
# NOTE: % operator format the string like sprintf-stype() string
# NOTE: it is a good practice to use the with keyword when dealing with file objects. It will be closed properly.
with open('data.txt','r') as f: # NOTE
# NOTE: For reading lines from a file, you can loop over the file object. This is memory efficient, fast and simple.
for line in f: # NOTE
print(line, end='') # NOTE: lines will include the '\n', so we set print() ends with nothing
# NOTE: you can also use list(f) or f.readlines()
# NOTE: f.write(str) write a string, f.tell() returns the position, f.seek changes the position
print(f.seek(0, 2)) # NOTE: offset=0, from_what = 2 as end of the file, 0 as beginning, 1 as current position.
# NOTE: The standard module called json can take python data hierachies, and convert them to string representations.
print(json.dumps(data)) # NOTE
json.dump(data, f) # NOTE: directly write into text file
data_loaded = json.load(f) # NOTE: write into file
# NOTE: pickle allow you to write arbitrarily complex python objects, whick make it dangerous and only python specific
# NOTE: syntax error is also known as parsing error, is caused by the token preceding the arrow
# NOTE: exception types are printed as part of the messsage
# NOTE: the code between try and except is excuted, if no error, except is skipped.
# NOTE: if error occurs, see if except matches the exception, if yes, go excute that, if not look for outer try.
# NOTE: a try statement can have multiple except statement in multiple line or a tuple.
# NOTE: exception will be handled by the first match
except OSError as err: # NOTE: The except clause may spepcify a variable after the exception name, which is bounded to an exception instance.
print("OS error: {0}".format(err)) # NOTE: for convenience, the exception instance defines __str__() so they can be printed directly
except: # NOTE: last except can omit errortype, which is dangerous.
print("Unexpected error:", sys.exc_info()[0]) # NOTE: print error info
# NOTE: try ... except statement has an optional else clause, which is useful for code that must be excuted if the try clause does not raise an exception.
# NOTE: it is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn't raised by the code that needs to be protected.
print(filename, 'has', len(f.readlines()), 'lines') # NOTE: get number of lines
# NOTE: If an exception has arguments, they are printed as the last part (‘detail’) of the message for unhandled exceptions.
# NOTE: Exception handlers don't just handle exceptions if they occur immediately in the try clause, but also if they occer inside functions that are called (even indirectly) in the try clause.
# NOTE: raise statement allows the programmer to force a specfied exception to occer.
# NOTE: the exception to be raised can be an exception instance or an exception class (a class derives from Exception)
raise # NOTE: use this to raise the error again
# NOTE: User-defined exceptions should typically be derived from the Exception class, either directly or indirectly.
# NOTE: The try statement has another optinal clause finally which is intended to define clean-up actions that must ve executed under all circumstances.

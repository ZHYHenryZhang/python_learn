## Walking through python tutorial in official documentation

to generate useful tips, run
```
grep -e "NOTE" -e "BUG" python_tutorial.py
```

If you have never check the python official documentation, or an well-organized class. You will benefit a lot from it.

Actually, there are definitely a few points worth mentioning.

 - import, module and packages
 - exception handling orders
 - list comprehension
 - repr method and formatting
 - a definition of a class is an object


Patterns
 - compare
 ```
 if a < b < c:
     print("we can compare like this")
 ```
 - file
 ```
 with open(filename, 'r') as f:
     for line in f:
         print("iterate over files, with 'with'")
 ```
 - list comprehension
 ```
 square = [x**2 for x in range(10)]
 ```
 - exception
 ```
 try:
     do_something()
 except ExceptionType as err:
     print(err)
 finally:
     clean_up()
 ```
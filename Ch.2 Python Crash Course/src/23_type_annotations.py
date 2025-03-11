#23a) Python is "dynamically typed" --> varibale type declarations are irrelevant as long as they are used correctly

def add(a,b):
    return a + b

assert add(10, 5) == 15,                "+ is valid for numbers"
assert add([1,2], [3]) == [1, 2, 3],    "+ is valid for lists"
assert add("hi ", "there") ==           "hi there", "+ is valid for strings"

try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")


#-------------------------------------------------------------------------------------
#23b) In other languages (a "statically typed" one), out fxn & obj would have specific types
def add(a: int, b: int) -> int:
    return a + b

assert add(10, 5) == 15,                    "you'd be okay like this"
assert add('hi', 'there') == 'hithere',     "and you'd catch this error here"


#-------------------------------------------------------------------------------------
#23c) Why to use type annotations
        ## 1) Important form of documentation (especially when it comes to mathematical concepts)
        ## for example, compare the following two stubs

def dot_product(x, y):

# I haven't defined "Vector" yet, but image if I did tho...
def dot_product(x: Vector, y: Vector) -> float:
    pass  
    
        ## 2) using the "mypy" tool to check for type errors
        ## ex: using mypy on the previous add("hi", "there") it would give the following

demo = """error: Argument 1 to "add" has incompatible type "str"; expected "int" """
            # Similar to assert testing


        ## 3) it can force me to design cleaner functions and interfaces
from typing import Union

def secretly_ugly_function(value, operation): ...

def ugly_function(value: int,
                  operation: Union[str, int, float, bool]) --> int: ...

        ## 4) allows for helping with autocomplete in VsCode

def f(xs: List[int]) -> None:
 #ex   xs.append
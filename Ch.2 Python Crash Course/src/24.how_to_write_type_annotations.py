#24a) Using type annotations with lists 
def total(xs: list) -> float:
    return sum(total)
            ## Not specific enough --> need it to be clear we want a list of floats somehow


#-------------------------------------------------------------------------------------
#24b) Using the "typing" module to find some extra parameterized types
from typing import List # Note the capital L

def total(xs: List[float]) -> float:
    return sum(total)


#-------------------------------------------------------------------------------------
#24c) Using type annotations on regular old varibales

# this is how to type-annotate variables when you define them
# But this is unnecessary; its 'obvious' x is an int
x: int = 5


        ## sometimes its not so obvious though
values = []                             # what type is this?
best_so_far = None                      # what type is this?


#-------------------------------------------------------------------------------------
#24d) Fixing this by using inline type hints
from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None     # allowed to be either a floaT or None


#-------------------------------------------------------------------------------------
#24e) All potential options from the typing module
from typing import Dict, Iterable, Tuple

# keys of type str and values of type int
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)


#-------------------------------------------------------------------------------------
#24f) Representing functions intelligently
from typing import Callable
# the type hint says that repeater is a function that takes
# two arguments, a string and an int, and returns a string

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"


        ## Type annotations are just OBJECTS
        ## Can assign to variables to make tbem easier to refer to

Number = int
Numbers = list[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)
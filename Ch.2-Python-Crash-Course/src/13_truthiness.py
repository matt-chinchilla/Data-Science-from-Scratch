#13a) Dealing with Boolean operations
        # *** they are CAPITALIZED in python

one_is_less_than_2 = 1 < 2          # equals True
true_equals_false = True == False   # equals False


# 13b) Python's version of "null" is "None"
x = None
assert x == None, "this is not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"


#13c) All of the values that are considered "falsy"
    # False
    # None
    # [] (an empty list)
    # {} (an empty dict)
    # ""
    # set() (an empty set)
    # 0
    # 0.0

    ## This basically means everything else is true & allows for "if statements" to check for empty

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

    ## This ^^^ is a longer way of doing the following
first_char = s and s[o]
        ### The reason why this works is because the "and" operator returns the 2nd val when the
        ### first is True, and the 1st val when it is False


#13d) Truthiness if x is either a number or possible "None"
safe_x = x or 0
    ## is definitely a number. The following may be more readable though
safe_x = x if x is not None else 0


#13e) The "all" function & the "any" function
    ## "all" Returns "True" only when EVERY element is truthy
    ## "any" returns truthy when at least 1 element is truthy

all([True, 1, {3}])     # True, all are truthy
all([True, 1, {}])      # False, {} is falsy
any([True, 1, {}])      # True
print(all([]))          # True, empty list is truthy
any([])                 # False, empty list is falsy
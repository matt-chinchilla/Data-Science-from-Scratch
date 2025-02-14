#3a) Functions are a rule for:
    # Taking 0 or more inputs and returning a corresponding output
    # Ex:
def double(x):
    """ This is where you put an optional docstring that explains what the
        function does. For example, the function multiplies its imput by 2
    """
    return x * 2


#3b) Fxn are "first-class" meaning that a variable can have a value of a function
def apply_to_one(f):
    """ Calls the function f with 1 as its argument"""
    return f(1)

my_double = double                          # refers to the previously defined function
x = apply_to_one(my_double)                 # x == return 1 * 2 == 2


#3c) Lambda fxn are short anonymous functions (meaning they don't have a name)
y = apply_to_one(lambda x: x + 4)           # == 5


#3d) You can assign lambda fxn to a variable // Most people recommend using def instead
another_double = lambda x: 2 * x            # Don't do this

def another_double(x):
    """ Do this instead """
    return 2 * x


#3e) Default args for fxn
def my_print(message = "my default message"):
    print(message)

my_print("hello")                           # prints 'hello'
my_print()                                  # prints 'my default message'


#3f) Specifying arugments by name
def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

full_name("Joel", "Grus")                   # == "Joel Grus"
full_name("Joel")                           # == "Joel Something"
full_name(last = "Grus")                    # == "What's-his-name Grus"
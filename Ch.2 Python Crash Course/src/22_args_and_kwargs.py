#22a) Ex: Creating a higher-order function that takes "f" as an input & returns a new function that is "f*2"
def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return f(x) * 2
    
    # and return that new function
    return g

            ## This works in some cases
def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8, "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

            ## This does not work in cases with functions that take in more than one argument
def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")


#-------------------------------------------------------------------------------------
#22b) Specifying functions that take arbitrary arguments. Done w/ unpacking & a wee bit o-magic
def magic(*args, **kwargs):
    print("unnamed args", args)
    print("keyword args", kwargs)

magic(1, 2, key="word", key2="word2")

# prints
#   unnamed args (1, 2)
#   keyword args {'key': 'word', 'key2': 'word2'}

            ## Here, args is a tuple of unnamed arguments & kwargs is a dictionary of keyword arguments


#-------------------------------------------------------------------------------------
#22c) Supplying arguments to a function
def other_way_magic (x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should equal 6"


#-------------------------------------------------------------------------------------
#22d) We will only use this trick to produce higher-order functions that can accept arbitrary arguments
def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g i supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"

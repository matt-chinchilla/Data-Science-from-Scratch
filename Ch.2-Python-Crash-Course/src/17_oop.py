#17a) "Classes" --> a way to encapsulate data & functions that operate on them
        ## This example will be a "counting clicker" like the one at Costco
        ## Defined using "class" keyword & a PascalCase name:

class CountingClicker:
    """A class can/should have a docstring, just like a function"""


#---------------------------------------------------------------------------------------------------
#17b) "member functions" --> fxn that allows the data w/in a class to be operated upon
        ## Normally, a class has constructor "__init__" that takes 
        ## in whatever parameters are needed to construct an instance

def __init__(self, count = 0):
    self.count = count


#---------------------------------------------------------------------------------------------------
#17c) Using the class name to construct an instance of the class
clicker1 = CountingClicker()                        # Init to 0
clicker2 = CountingClicker(100)                     # starts with count = 100
clicker3 = CountingClicker(count=100)               # More explicit way of doing the same


            ### "dunder methods" --> "double underscore methods" have "special behaviors"
            ### and are generally considered "private"


#---------------------------------------------------------------------------------------------------
#17d) "repr" method is another dunder which makes a string representation of a class instance
def __repr__(self):
    return f"CountingClicker(count={self.count})"


# --------------------------------------------------------------------------------------------------
#17e) implementing the "public API" of the class
        ## "public API" --> the fxns that are meant to be used by the user
        ## "private API" --> the fxns that are meant to be used by the class itself

def click(self, num_times = 1):
    """Click the clicker some number of times."""
    self.count += num_times

def read(self):
    return self.count

def reset(self):
    self.count = 0

#---------------------------------------------------------------------------------------------------
#17f) Writing test cases for the clicker
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with a count of 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after 2 clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should have count 0"


#--------------------------------------------------------------------------------------------------
#17g) Making subclasses that inherit from the parent class
        ## Ex: a new clicker that cannot be reset

#a subclass inherits all the behavior of its parent class
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that now DOES NOTHING
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"
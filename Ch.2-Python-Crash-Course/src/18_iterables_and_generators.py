#18a) "Generators" will be used in order to retrieve specific elements by indicies & not waste
#     compute resources. I will often be iterating over it w/ "for" & "in" statements

        ## "Generators" --> Something that can be iterated over like lists, but generates values
        ##  lazily on demand


#-----------------------------------------------------------------------------------------------------
#18b) Making Generators using the "yield" operator
def generate_range(n):
    i = 0
    while i < n:
        yield i             # Every call to yield produces a value of the generator
        i += 1


#-----------------------------------------------------------------------------------------------------
#18c) Making a loop to consume "yielded" values one at a time until none are left
for i in generate_range(10):
    print(f"i: {i}")

        ## It is worth notin that rnage itself is lazy, so there's no point in doing this


#-----------------------------------------------------------------------------------------------------
#18d) using a generator to create an infinite sequence
def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
        ## ^^ probably smart to include "break" logic

        ## Note: You can only iterate over a generator once
        ##       either re-create it every time, or just use a list


#-----------------------------------------------------------------------------------------------------
#18e) Another way is by using "for" comprehensions wrapped in parentheses
evens_below_20 = (i for i in range(20) if i % 2 == 0)
        ## None of these generator comprehensions do any work until they are iterated
        ## ^^ can be used to build data-processing pipelines

# none of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# and so on...


#-----------------------------------------------------------------------------------------------------
#18f) Using the "enumerate" function to get not only values. but also their indices
        ## Returns values in pairs (index, value)

names = ["Alice", "Bob", "Claire", "Debbie"]

#not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {names[i]}")
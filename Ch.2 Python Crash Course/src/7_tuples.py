#7a) Tuples: --> An immutable variation of a list
my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3, 4
my_list[1] = 3                                      # my_list == [1, 3]

try:
    my_tuple[1] = 3                                 # This will raise a TypeError b/c NOT mutable
except TypeError:
    print("cannot modify a tuple")


#7b) Tuples are a convenient way to return multiple values from functions
def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2,3)                           # == (5, 6)
s, p = sum_and_product(5, 10)                       # s == 15, p == 50


#7c) Multiple assignment (unpacking) with tuples
x, y = 1, 2                                         # now x == 1, y == 2
x, y = y, x                                         # Pythonic way to swap variables; now x == 2, y == 1
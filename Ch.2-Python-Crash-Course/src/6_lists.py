#6a) Most fundamental data structure in python --> is an ARRAY in other programming languages ++ OTHER programming functionality
integer_list = [1, 2, 3]
heterogeneous_list = ["String", 0.1, True]                  # Lists can contain different types
list_of_lists = [integer_list, heterogeneous_list, []]      # Lists can contain other lists

list_length = len(integer_list)                             # == 3
list_sum = sum(integer_list)                                # == 6


#6b) Can get or set the nth element of a list with square brackets
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0]                                                 # == 0, lists are 0-indexed
one = x[1]                                                  # == 1
nine = x[-1]                                                # == 9,  'Pythonic' for last element of the list
eight = x[-2]                                               # == 8,  'Pythonic' for next-to-last element of the list
x[0] = -1                                                   # now x == [-1, 1, 2, 3, ..., 9]


#6c) Use square brackets to SLICE lists
        # The "slice i:j" means ALL ELEMENTS from i (inclusive) to j (not inclusive)
        # Leaving off the beginning (ex: [:3]) means start at the beginning
        # Leaving off the end (ex: [3:]) means go all the way to the end

first_three = x[:3]                                         # == [-1, 1, 2]
three_to_end = x[3:]                                        # == [3, 4, ..., 9]
one_to_four = x[1:5]                                        # == [1, 2, 3, 4]
last_three = x[-3:]                                         # == [7, 8, 9]
without_first_and_last = x[1:-1]                            # == [1, 2, ..., 8]
copy_of_x = x[:]                                            # == [-1, 1, 2, ..., 9]

        # Can also take in a "stride" ([start:stop:stride]) to know how much to jump by
every_third = x[::3]                                        # == [-1, 3, 6, 9]
five_to_three = x[5:2:-1]                                   # == [5, 4, 3]


#6d) Use "in" to check for list membership
1 in [1, 2, 3]                                              # == True
0 in [1, 2, 3]                                              # == False
        # This check involves examining the elements of the list one at a time
        # So you probably shouldn't use it unless you know your list is pretty small

#6e) adding/concat lists together using the "extend" method
x = [1, 2, 3]
x.extend([4, 5, 6])                                         # x is now [1, 2, 3, 4, 5, 6]

        # If you don't want to modify x you can use "list addition"
x = [1, 2, 3]
y = x + [4, 5, 6]                                           # y is [1, 2, 3, 4, 5, 6]
        # This doesn't modify x, so you can use this when you want to keep x around


#6f) append to lists one item at a time
x = [1, 2, 3]
x.append(0)                                                 # x is now [1, 2, 3, 0]
y = x[-1]                                                   # == 0
z = len(x)                                                  # == 4


#6g) Unpacking lists (I know how many elements they contain)
x, y = [1, 2]                                               # now x == 1, y == 2
        # Causes a ValueError if both sides are not the sa,me
        # use an underscore for a value you are going to throw away
_, y = [1, 2]                                               # now y == 2
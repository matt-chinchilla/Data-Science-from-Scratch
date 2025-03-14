#21a) "zip" function --> transforms  multiple iterables into a single iterable of tuples of corresponding fxns
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy so I have to do something like the following:
[pair for pair in zip(list1, list2)]            # is [('a', 1), ('b', 2), ('c', 3)]
        ## ** if the lists are diff lengths, "zip" stops as soon as the first list ends **

#---------------------------------------------------------------------------------------------------
#21b) "unziping" using a little trick
pair = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pair)

        ## The asterisk (*) preforms "argument unpacking"
        ## uses elements of pairs as individual arguments to zip
        ## Same as doing the following

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))


#---------------------------------------------------------------------------------------------------
#21c) Using argument unpacking with any function
def add(a, b): return a + b

add(1, 2)         # returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
add(* [1,2])      # returns 3
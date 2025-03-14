#15a) "List Comprehensions" --> A Pythonic way to transform a list into another list 
                                # (but only chooses certain elements)

even_numbers = [x for x in range(5) if x % 2 == 0]        # is now [0, 2, 4]
squares = [x * x in range(5)]                             # is now [0, 1, 4, 9, 16]  
even_squares = [x * x for x in even_numbers]              # is now [0, 4, 16]  


#15b) Can also use it to turn lists into "Dictionaires" | "Sets"
square_dict = {x: x * x for x in range (5)}               # is now {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set = {x * x for x in [1, -1]}                     # is now {1} (set of unique values)


#15c) Using underscores is a common way for if you will not need the variable being used
        # For anything other than the calculation
zeros = [0 for _ in even_numbers]                         # same length as even numbers


#15d) Nesting for loops in a list comprehension
pairs = [(x,y)
         for x in range(10)
         for y in range(10)]                              # pairs becomes [(0,0), (0,1), ..., (9,9)]


#15e) Using list comprehensions with math in the results
increasing_pairs = [(x,y)                                 # Only pairs where x < y
                    for x in range(10)                    # range(lo, hi) equals
                    for y in range(x+1, 10)]              # [lo, lo + 1, ..., hi - 1]
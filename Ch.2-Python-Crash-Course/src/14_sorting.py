#14a) The "sort" method sorts lists in place
        ## The "sorted" function returns a new sorted list (prevents modification)

x = [4, 1, 2, 3]
y = sorted(x)           # y is now [1, 2, 3, 4]
x.sort()                # x is now [1, 2, 3, 4]

        ## Sorts natively by smallest to largest


#12b) Reverse sorting
        ## Done using a "reverse=True" parameter
        ## Can compare the results of a fxn that you specify with a key

# sort the list by absolute values from largest to smallest
x = sorted([-4, 1, -2, 3], key = abs, reverse = True)           # is now [4, -3, -2, 1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
            key = lambda word_and_count: word_and_count[1],
            reverse = True)

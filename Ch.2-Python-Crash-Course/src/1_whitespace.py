#1a) Whitespace formatting
for i in [1,2,3,4,5]:       
    print(i)                # First line in "for i" block
    for j in [1,2,3,4,5]:
        print(j)            # First line in "for j" block
        print(i + j)        # Last line in "for j" block
    print(i)                # Last line in "for i" block
print("done looping")

#1b) Long lines
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12
                           + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

#1c) making code easier to read
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

easier_to_read_list_of_lists = [[1,2,3],
                                [4,5,6],
                                [7,8,9]]

#1d) using a backslash to continue a statement onto the next line
two_plus_three = 2 + \
                 3
print(two_plus_three)

#------------------------------------------------------------------------------------------------
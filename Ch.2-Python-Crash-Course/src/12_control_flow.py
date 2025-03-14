#12a) The "if" keyword is for conditional arguments
if 1 > 2:
    message = "if only 1 were greater than 2..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"


#12b) Ternary "if-then-else" on one line
parity = "even" if x % 2 == 0 else "odd"


#12c) "while" loops
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1


#12d) Not gonna lie, definitely going to use "for" and "in" a lot more
        # The "range" keyword indicates the following:
        # ex: range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(10):
    print(f"{x} is less than 10")


#12e) We can use "continue" and "break" for more complex operations
for x in range(10):
    if x == 3:
        continue    # this will SKIP this one entirely & go to the next iteration
    if x == 5:
        break       # Quits the loop ASAP
    print(x)

    #prints 0, 1, 2, 4
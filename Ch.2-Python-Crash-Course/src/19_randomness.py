#19a) using the "random" module frequently for random numbers in data science
import random
random.seed(10)             # ** Seeds of specific number reproduce the same results every time **

four_uniform_randoms = [random.random() for _ in range(4)]
#[0.5714025946899135,       # random.random() produces numbers
# 0.4288890546751146,       # uniformly between 0 and 1.
# 0.5780913011344704,       
# 0.20609823213950174]

        ## This is all "pseudorandom" because results a reprducible w/ random.seed()


#------------------------------------------------------------------------------------
#19b) using "random.rnadrange" to take in 1 or 2 args & choosing an element randomly from the range
random.randrange(10)        # choose randomly from range(10) = [0, 1, 2, ..., 9]
random.randrange(3, 6)      # choose randomly from range(3, 6) = [3, 4, 5]


#------------------------------------------------------------------------------------
#19c) using random.shuffle to randomly reorder elements of a list
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# I got [4, 5, 6, 7, 2, 9, 10, 8, 1, 3]


#------------------------------------------------------------------------------------
#19d) using random.choice to randomly select an element from a list
my_best_friend = random.choice(["Alice", "Bob", "Claire", "Debbie"])
print(my_best_friend) 
# I got Bob


#------------------------------------------------------------------------------------
#19e) using random.sample to choose a sample of elements without replacement (ex: no replacements)
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)
#I got [38, 22, 24, 26, 18, 52]


#------------------------------------------------------------------------------------
#19f) using random.choice to take a sample of elements with replacement (ex: allowing duplicates)
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)
# I got [4, 7, 2, 4]
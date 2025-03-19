#1) ** Explicitly reading and writing TO FILES directly in my code **
        # The basics, "working with text files" --> obtain a "file" object using OPEN

# 'r' means read-only, it's assumed if you leave it out
file_for_reading = open('reading_file.txt', 'r')
file_for_reading2 = open('reading_file.txt')

# 'w' is write -- will destroy the file if it already exists!
file_for_writing = open('writing_file.txt', 'w')

# 'a' is append -- for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')

    ## ** close all your files when you are done **
file_for_writing.close()

    ## TIP: use a WITH BLOCK when altering files --> Closes them automatically
with open(filename) as f:
    data = function_that_gets_data_from(f)

# at this point f has already been close, so don't try to use it
process(data)

#-----------------------------------------------------------------------------------------------
#2) Iterating over a whole text file with "for"
import re
starts_with_hash = 0

with open('input.txt') as f:
    for line in f:                      # look at each line in the file
        if re.match("^#", line):        # use a regex to see if it starts with '#'
            starts_with_hash += 1       # if it does, add 1 to the count


#-------------------------------------------------------------------------------------------------
#3) "strip" to remove whitespace before alterations
    # ex: FIle w/ emails adds // 1-per-line // need to gen a histogram of domains
     ## Possible solution (not for all) --> seperate them by the "@" symbol

def get_domain(email_address: str) -> str:
    """Split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]         # -1 = last item in list

# a couple of tests
assert get_domain("joelgrus@gmail.com") == "gmail.com"
assert get_domain("joel@m.datasciencester.com") == "m.datasciencester.com"

from collections import Counter

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip()
                                       for line in f
                                       if '@' in line))
#1) the sys.stdin and sys.stdout modules
        # "stdin" -> standard input / data stream for inputting data
        # "stdout" -> standard output / data stream for outputting data

    # Ex: a program that reads lines of text & spits out the ones that match regular expressions
#egrep.py
import sys, re

# sys.argv is the list of CLI args
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]

# for every line parsed into the script
for line in sys.stdin:
    # if it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)

    # Next ex: counts the lines it receives then writes the count
#line_count.py
import sys

count = 0
for line in sys.stdin:
    count += 1

# print goes to sys.stdout
print(count)


#-----------------------------------------------------------------------------------------------
#2) Script that coutns the words in its input and writes out the most common ones

# most_common_words.py
import sys
from collections import Counter

# pass in number of words as first argument
try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py num_words")
    sys.exit(1)

counter = Counter(word.lower()                          # all lowercase
                  for line in sys.stdin
                  for word in line.strip().split()      # Split on spaces
                  if word)                              # Skip empty words

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))                        # Write the count
    sys.stdout.write("\t")                              # Tab
    sys.stdout.write(word)                              # Write the word
    sys.stdout.write("\n")                              # New line

    # Example output
    ## "type the_bible.txt | python most_common_words.py 5"
      ### 36397    the
      ### 30031    and
      ### 20163    of
      ### 7154     to
      ### 6484     in
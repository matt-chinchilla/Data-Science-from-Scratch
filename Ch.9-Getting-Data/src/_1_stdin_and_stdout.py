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
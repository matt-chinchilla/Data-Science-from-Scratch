#20a) the "re" module provides a way of searching text || very useful & complex
import re

re_examples = [                                 # All of these are True because
    not re.match("a", "cat"),                       # 'cat' does not start with 'a'
    re.search("a", "cat"),                          # 'cat' contains 'a'
    not re.search("c", "dog"),                      # 'dog' does not contain 'c'
    3 == len(re.split("[ab]", "carbs")),            # Split on a or b to ['c', 'r', 's']
    "R-D-" == re.sub("[0-9]", "-", "R2D2")          # Replace all digits with '-'
]

assert all(re_examples), "All regex examples should be True"
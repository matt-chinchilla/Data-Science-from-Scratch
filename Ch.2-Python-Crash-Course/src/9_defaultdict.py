#9a) Ex: Trying to count the # of instances of a word in a document
        # --> Create a dictionary w/ keys as words || values as counts (# of times each word appears)
        # Add to dict if not in there already || increment the count if it is

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


#9b) Using exception handling to when looking up missing keys instead
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1


#9c) Option 3: Using the "get" method --> Super graceful for missing keys
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0) # 0 if not there
    word_counts[word] = previous_count + 1


#9d) Using "defaultdict" from the "collections" module
            # Adds a first value for a key if it's not already in the dictionary
from collections import defaultdict

word_counts = defaultdict(int)                          # int() produces 0
for word in document:
    word_counts[word] += 1


#9e) Using "default dict" w/ list or dict or my own function
dd_list = defaultdict(list)                             # list() produces an empty list
dd_list[2].append(1)                                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)                             # dict() produces an empty dict
dd_dict = ["Fred"]["City"] = "Seattle"                  # {Fred: {City: Seattle}}

dd_pair = default_dict(lambda: [0, 0])
dd_pair[2][1] = 1                                       # now dd_pair contains {2: [0, 1]}

### Will be useful when using dictionaries to "collect" results
### by some key BUT we don't want to have to check every time to
### See if it exists yet
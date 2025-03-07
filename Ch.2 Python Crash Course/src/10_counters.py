#10a) "Counter" --> turns a sequence of values into a defaultdict(int)-like
                    # object mapping keys to counts

from collections import Counter
c = Counter[[0, 1, 2, 0]]                           # c is basically {0: 2, 1: 1, 2: 1}


#10b) Makes a really easy way to solve word-counting problems
        # Recall document == a list of words
word_counts = Counter(document)


#10c) "most_common" method:
    # print the top 10 most common words and their counts
for wird, count in word_counts.most_common(10):
    print(word, count)
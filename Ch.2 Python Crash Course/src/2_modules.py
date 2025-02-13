#2a) What they are
    # Features (either by python itself, or 3rd party libraries)
    # Can be included using the "import" statement
import re
my_regex = re.compile("[0-9]+", re.I)

#2b) Aliasing assuming there was already a differebt "re" in the code
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

#2c) Aliasing to condense the size of the code needed to be typed
import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,6]) # Plots 1-3 on x axis // plots 4-6 on y axis
plt.show()

#2d) Explicit imports && w/o qualification
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()
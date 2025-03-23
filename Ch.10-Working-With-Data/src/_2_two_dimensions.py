#2) Plotting 2 data points against each other (ex): Daily minutes on my site AND #years experience as a data scientist
    # consider the following fake dataset
import random
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2] # 2 layers deep
probability_src = project_root / "Ch.6-Probability" / "src" # Construct the path
sys.path.append(str(probability_src))

from B2_continuous_distributions import inverse_normal_cdf

def random_normal() -> float:
    """Returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]
    # Historgrams for ys1 and ys2 would look similar, but a JOINT DISTRIBUTION with xs
    # gives a MUCH different look

import matplotlib.pyplot as plt
plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Very Different Joint Distributions")
plt.show()

        # Also looks very different if we look at the correlations
statistics_src = project_root / "Ch.5-Statistics" / "src"
sys.path.append(str(statistics_src))
from D_correlation import correlation

print(correlation(xs, ys1)) # about .9
print(correlation(xs, ys2)) # about -.9 
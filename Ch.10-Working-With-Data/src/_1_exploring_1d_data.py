#1) Creating a Histogram where data is grouped into discrete buckets
from typing import List, Dict
from collections import Counter
import math

import matplotlib.pyplot as plt

def bucketsize(point: float, bucket_size: float) -> float:
    """Floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size) # floor = round down

def make_histogram(points: List[float], bucket_size: float) -> Dict[float, int]:
    """Buckets the points and counts how many in each bucket"""
    return Counter(bucketsize(point, bucket_size) for point in points)

def plot_histogram(points: List[float], bucket_size: float, title: str =""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)

# Making random data to plot
import random
import matplotlib.pyplot as plt

import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2] # 2 layers deep
probability_src = project_root / "Ch.6-Probability" / "src" # Construct the path
sys.path.append(str(probability_src))
from B2_continuous_distributions import inverse_normal_cdf

random.seed(0)

# uniform between -100 and 100
uniform = [200 * random.random() - 100 for _ in range(10000)]

# normal distribution with mean 0, standard deviation of 57
normal = [57 * inverse_normal_cdf(random.random())for _ in range(10000)]

        ## Both uniform & normal have means close to 0 & Standard Dev CLOSE to 58
        ## BUT ** very different distributions **
plot_histogram(uniform, 10, "Uniform Histogram")
plt.show()
plt.gca().clear()  # Clear the current figure
plt.close()        # Close the current figure window

plot_histogram(normal, 10, "Normal Histogram")
plt.show()
plt.gca().clear()
plt.close()

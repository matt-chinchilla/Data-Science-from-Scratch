#3a) "Dispersion" -> How spread out our data is
        ## "range" already means something in Python, so we'll use a different name
        ## "Range" -> the difference between the smallest and largest values
from typing import List
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

assert data_range(num_friends) == 99

        ## Not always the most reliable as the range doesn't rely on the whole dataset
        ## Ex: Range of [0,0,0,0,0,0,100,100] is the same as [0, 50, 50, 50, 100]
        ##     even though the dispersions are different, so we use...


#-----------------------------------------------------------------------------------
#3b) Using the "variance" -> the average of the squared differences from the mean
from B_central_tendencies import mean

import sys
sys.path.append(r"C:\Users\chiri\Programming Projects\Data-Science-from-Scratch\Ch.4 Linear Algebra\src")
from A_vectors import sum_of_squares

def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
        """Almost the average squared deviation from the mean"""
        assert len(xs) >= 2, "variance requires at least two elements"

        n = len(xs)
        deviations = de_mean(xs)
        return sum_of_squares(deviations) / (n - 1)

assert 81.54 < variance(num_friends) < 81.55


#-----------------------------------------------------------------------------------
#3c) Using the "standard deviation" -> the square root of the variance
import math
def standard_deviation(xs: List[float]) -> float:
        """The standard deviation is the square root of the variance"""
        return math.sqrt(variance(xs))

assert 9.02 < standard_deviation(num_friends) < 9.04
                ## Still suffers from the issue that outliers can mess with the data


#-----------------------------------------------------------------------------------
#3d) Using the "interquartile range" -> the difference between the 75th percentile and the 25th percentile
from B_central_tendencies import quantile # sorts list, returns result at p-index

def interquartile_range(xs: List[float]) -> float:
        return quantile(xs, 0.75) - quantile(xs, 0.25)

assert interquartile_range(num_friends) == 6
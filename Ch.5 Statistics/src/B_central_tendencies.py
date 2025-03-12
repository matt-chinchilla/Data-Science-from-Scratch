#2a) We will want to know where our data is "centered" --> a common method is the "mean"
from typing import List

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def mean(xs: List[float]) ->float:
         return sum(xs) / len(xs)

mean(num_friends)       #7.333333


#-----------------------------------------------------------------------------------
#2b) Using the median for even and odd cases & combining them
# the underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library (they also appear as maroon).

def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]     # return the sorted list 

def _median_even(xs: List[float]) -> float:
       """If len(xs) is even, the median is the average of the middle two elements"""
       sorted_xs = sorted(xs)
       mid_right = len(xs) // 2
       mid_left = mid_right - 1
       return (sorted_xs[mid_left] + sorted_xs[mid_right]) / 2

def median(v: List[float]) -> float:
       """Finds the 'middle-most' value of v"""
       return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

        ## Now we can decipher the median number of friends in num_friends
print(median(num_friends))    #6

        ## The median can change with a single newly-added value AND also
        ## Has to be sorted in order to calculate, therefore making it more complex than mean


#-----------------------------------------------------------------------------------
#2c) Using the "quantile" --> a value below which a certain percentile of the data falls
        ## Ex: The median is the value at the 50th percentile

def quantile(xs: List[float], p: float) -> float:
       """Returns the pth-percentile value in x"""
       p_index = int(p * len(xs))
       return sorted(xs)[p_index] # ** Returns sorted list at position p_index

assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13


#-----------------------------------------------------------------------------------
#2d) Using the "mode" --> the most common value(s) in a list
from collections import Counter

def mode(x: List[float]) -> List[float]:
       """Returns a list, since there might be more than one mode"""
       counts = Counter(x)
       max_count = max(counts.values())
       return [x_i for x_i, count in counts.items()
               if count == max_count]

assert set(mode(num_friends)) == {1, 6}
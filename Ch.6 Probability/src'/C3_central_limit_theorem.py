#3a) "Central Limit Theorem" --> states that a random variable defined as 
#       "the average of a large number of independent && randomly distributed variables"
#       will approximately be normally distributed.


#----------------------------------------------------------------------------------------
#3b) "Binomial Random Variables" -> Have the following:
#                   1) 2 parameters: n (number of trials) && p (probability of success)

        ## A Binomial(n,p) random variable == sum of "n" independent Bernoulli(p) random variables
        ## 2 possible outcomes: Success (1) && Failure (0)
import random

def bernoulli_trial(p: float) -> int:
    """Returns 1 with probability p and 0 with probability 1-p"""
    return 1 if random.random() < p else 0

def binomial(n: int, p: float) -> int:
    """Returns the sum of n bernoulli(p) trials"""
    return sum(bernoulli_trial(p) for _ in range(n))



#-------------------------------------------------------------------------------------------------------
#3c) Using the Central Limit Theorem to show how the Binomial distribution approaches a
#    Normal distribution as n increases

from B2_continuous_distributions import normal_cdf
from collections import Counter
from matplotlib import pyplot as plt
import math

def binomial_histogram(p: float, n: int, num_points: int) -> None:
    """Picks points from a Binomial(n, p) and plots their histogram"""
    data = [binomial(n, p) for _ in range(num_points)]

    # use a bar chart to show the actual binomial samples
    histogram = Counter(data) # count the number of occurrences of each value
    plt.bar([x - 0.4 for x in histogram.keys()],                #
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')
    
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs Normal Approximation")
    plt.show()
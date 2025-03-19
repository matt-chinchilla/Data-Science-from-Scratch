#1a) Using the "Flipping a coin example", we will test if a coin is fair
        # Testing that p = 0.5
        #          vs.
        # Testing that p != 0.5
    # "n" == # of coin flips
    # "X" == counter of # of heads
        ## X is a Binomial(n.p) random variable

# ** Approximating the Normal Distribution **
    ## Import needed materials from other chapters
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2] # 2 layers deep
probability_src = project_root / "Ch.6-Probability" / "src" # Construct the path
sys.path.append(str(probability_src)) # Now Line 31 works


from typing import Tuple
import math

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Returns mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1-p) * n)
    return mu, sigma

            ## When a random variable follows a "normal distribution" (bell curve)
            ## we can figure out the probability that its "realized value" is w/in or outside 
            ## of a particular interval

from B2_continuous_distributions import normal_cdf, inverse_normal_cdf

# The normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf

#It's above the threshold if it's not below the threshold
def normal_probability_above(lo: float,         # LITERALLY jus
                             mu: float = 0,
                             sigma: float = 1) -> float:
    """The prob. that a N(mu, sigma) is > lo"""
    return 1 - normal_cdf(lo, mu, sigma)

# It's less than hi, more than lo
def normal_probability_between(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """The probability that a N(mu, sigma) is between lo and hi."""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# It's outside if it's not between
def normal_probability_outside(lo: float,
                                 hi: float,
                                 mu: float = 0,
                                    sigma: float = 1) -> float:
    """The probability that a N(mu, sigma) is not between lo and hi. """
    return 1 - normal_probability_between(lo, hi, mu, sigma)


#--------------------------------------------------------------------------------
#1b) Doing the "reverse" || aka finding the liklihood of being OUTSIDE a range
        # ex: an interval centered at mean // has 60% probability // Find lower 20%
        #     and the upper 20% of the probability (leaves 60%)

def normal_upper_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    """
    Returns the symmetric (about the mean) bounds
    that contain the specified probability
    """
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print("mu_0, sigma_0", mu_0, sigma_0)


#-----------------------------------------------------------------------------------------------
#1c) "Significance" -> How willing we are to make a "tpye 1 error" (false positive)
        ## a.k.a we Reject Ho (null hypothesis || p = 0.5 || default hypothesis)
        ## **** we choose either 1% or 5% for some reason nobody knows anymore ****

    # A 5 % example over 1000 flips where H0 gets rejects falling outside the bounds of:
    # (469, 531)
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)


#---------------------------------------------------------------------
#1d) "Power of a test" -> How willing we are to make a "type 2 error" (false negative)
        ##Ex: flipping a coin is NOT p = 0.5


    #95% bounds based on assumption that p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

    # Actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

    # a type 2 error means we fail to reject the null hypothesis
    # which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability      # 0.887


#----------------------------------------------------------------------------------------
#1e) "one-sided test" -> rejected when X is MUCH larger than 500, but not when smaller than 500
hi = normal_upper_bound(0.95, mu_0, sigma_0) 
# is 526 (< 531, since we need more probability in the upper tail)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability # 0.936
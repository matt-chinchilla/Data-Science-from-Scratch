# The parameters:
        # 990/1000 viewers click on Ad "A" when shown
        # 10/1000 viewers click on Ad "B" when shown

        #N_a == # of viewers of ad A
        #n_a == # of viewers who clicked on ad A
        #N_b == # of viewers of ad B
        #n_b == # of viewers who clicked on ad B
from typing import Tuple
import math

def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n / N             # p == mean && probability someone clicks the ad
    sigma = math.sqrt(p * (1-p) / N)
    return p, sigma

#---------------------------------------------------------------------------------
#2) Testing our "null hypothesis" that p_a and p_b are equal

def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    """returns p_a - p_b divided by standard deviation of their differences"""
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    p_diff = p_A - p_B
    return p_diff / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


#---------------------------------------------------------------------------------
#3) Tesing our statistic on "A" w/ 200 and "b" w/ 180
z = a_b_test_statistic(1000, 200, 1000, 180)    #-1.14

from B2_p_values import two_sided_p_value
        # The probability of getting a value at least as extreme as z
p_value = two_sided_p_value(z) # 0.2546

# If b had 150 instead
z = a_b_test_statistic(1000, 200, 1000, 150)    
p_value = two_sided_p_value(z) # 0.003

# ***  Only a 0.003 probability that we would see such a difference if the ads were equally effective**
#2a) "p-values" Assuming our initial hypothesis is correct, what is the probability of
                # Getting the actual result that we got?
from A1_flipping_a_coin import normal_probability_above, normal_probability_below, mu_0, sigma_0


def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    How likely are we to see a value at least as extreme as x (in either
    direction) if our values are from a N(mu, sigma)?
    """
    if x >= mu:
        # x is greater than the mean, so the tail is everything greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x is less than the mean so the tail is everything less than x
        return 2 * normal_probability_below(x, mu, sigma)
    
# Example: If we got 530 Heads/ 470 tails:
print(two_sided_p_value(529.5, mu_0, sigma_0) * 100) # odds are about 6.2077%

        #Running a simulation
import random

extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0    # Count # of heads
                    for _ in range(1000))                # in 1000 flips,
    if num_heads >= 530 or num_heads <= 470:             # and count how often
        extreme_value_count += 1                         # the # is 'extreme'

# the found p-value was 0.062 => ~62 extreme values out of 1000
assert 59 < extreme_value_count < 65, f"{extreme_value_count}" # Above the 5% significance!!!

# MATTHEW, MAKE SURE YOUR DATA IS ROUGHLY DISTRIBUTED NORMALLY BEFORE DOING TESTS
# THIS COULD DO SOMETHING LIKE MESS WITH THE LIKLIHOOD OF AI RESPONSES
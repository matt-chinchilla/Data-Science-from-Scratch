# 1) "Bayseian Inference" --> Starting with unknown parameters // treat them as random variables
        # Then we use observed Data and Bayes's theorem to get a updated "posterior distribution"
    # for the parameters

# Ex: unknown parameter is a probability "P", we use a "Beta Distribution" to model it
#     # Beta Distribution is a probability distribution over the interval [0, 1]
#     # Beta distribution is parameterized by two parameters: alpha and beta
#     # alpha == # of successes
#     # beta == # of failures

import math
# alpha = success + 1 |||| beta = failure + 1
# Ex: alpha = 10, beta = 10 => uniform distribution
def B(alpha: float, beta: float) -> float:
    """A normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1:          # no weight outside of [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)
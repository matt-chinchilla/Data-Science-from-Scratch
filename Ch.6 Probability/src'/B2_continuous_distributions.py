#2a) Making a Probability Density Function (PDF) for a continous random variable
        ## P(val) == Integral(Density(val)) from x = -inf to x = inf

#The density function of a uniform distribution is:
def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0
        ## Ex: Probability of seeing a value beteen .2 and .3 is 1/10


#------------------------------------------------------------------------------------
#2b) "Cumulative Distribution Function (CDF)" -> The probability that a random variable
#   #                                            is <= a certain value

def uniform_cdf(x: float) -> float:
    if x < 0:   return 0            # uniform random is never less than 0
    elif x < 1: return x            # ex: P(X <= 0.4) = 0.4
    else:       return 1            # uniform random is never greater than 1               

import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-1.0, 2.0, 300)
    # Compute y-values from the uniform CDF function
y_values = [uniform_cdf(x) for x in x_values]

# Make a da plot
plt.figure(figsize=(8,6))
plt.plot(x_values, y_values, label='The Uniform CDF', color='blue')

# Ticks of 0.5 for both axes
plt.xticks(np.arange(-1.0, 2.0, 0.5))
plt.yticks(np.arange(-0.5, 1.5, 0.5))

# limits
plt.xlim(-1.0, 2.0)
plt.ylim(-0.5, 1.5)

# Axis lavels, title, legend, and grid
plt.xlabel('x')
plt.ylabel('F(X)')
plt.title('The Uniform CDF')
plt.legend()
plt.grid(True)

# Display
plt.show()
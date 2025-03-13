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
# plt.figure(figsize=(8,6))
# plt.plot(x_values, y_values, label='The Uniform CDF', color='blue')

# # Ticks of 0.5 for both axes
# plt.xticks(np.arange(-1.0, 2.0, 0.5))
# plt.yticks(np.arange(-0.5, 1.5, 0.5))

# # limits
# plt.xlim(-1.0, 2.0)
# plt.ylim(-0.5, 1.5)

# # Axis lavels, title, legend, and grid
# plt.xlabel('x')
# plt.ylabel('F(X)')
# plt.title('The Uniform CDF')
# plt.legend()
# plt.grid(True)

# Display
# plt.show()


#--------------------------------------------------------------------------------------------------
#2c) "Probability Density Function (PDF)" -> The probability that a random variable "X" falls
#   #                                        between 'x' and 'x+h'
# 
#   #   P(x <= X <= x+h) = Integral(Density(x)) from x to x+h
 
 
#--------------------------------------------------------------------------------------------------
# #2d) "Normal Distribution" -> The Bell curve || Determined by its mean (mu) and standard dev (sigma)
import math
SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

# Lets plot them now
import matplotlib.pyplot as plt
xs = [x / 10.0 for x in range(-50, 50)] # # x values from -5 to 5

plt.plot(xs, [normal_pdf(x,sigma=1) for x in xs], '-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1)   for x in xs],'-.',label='mu=-1,sigma=1')

plt.legend()
plt.title("Various Normal pdfs")
#plt.show()

plt.gca().clear()  # Clear the current figure
plt.close()        # Close the current figure window
plt.clf()          # Clear the current figure to free up memory

#----------------------------------------------------------------------------------------------
#2e) making the Comulative Distribution Function (CDF) for a normal distribution
def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return(1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

        ## Plotting a few CDFs
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')

plt.xlabel("x (Value)")
plt.ylabel("Cumulative Probability")
plt.legend(loc=4) # bottom right
plt.title("Various Normal cdfs")
#plt.show()

plt.close()
plt.gca().clear()
plt.clf()


#----------------------------------------------------------------------------------------------
#2f) Inversing the CDF to fin a value corresponding to a probability this time
        # If normal_cdf is continuous and increasing, we can use a binary_search

def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """Find approximate inverse using binary search."""

    # if not standard, compute standard and rescale             
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0   # normal_cdf(-10) is (very close to) 0
    hi_z =   10.0     # normal_cdf(10) is (very close to) 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2          # consider the midpoint
        mid_p = normal_cdf(mid_z)           # and the CDF's value there
        if mid_p < p:
            low_z = mid_z                   # Midpoint too low, search above it
        else:
            hi_z = mid_z                    # Midpoint too high, search below it 

# Repeatedly bisects intervals until it narrows in on a Z (the desired standard normal variable)
# that is close enough (within the tolerance range) to the desired probability "p"
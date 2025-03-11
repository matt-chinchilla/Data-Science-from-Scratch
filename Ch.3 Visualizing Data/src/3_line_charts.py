#3a) We can make line charts using plt.plot --> **good for showing "trends"**

from matplotlib import pyplot as plt
from typing import List, Optional

variance: List[int] = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared: List[int] = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error: List[int] = [x + y for x, y in zip(variance, bias_squared)]
xs: List[int] = [i for i, _ in enumerate(variance)]         # Counter for each point on the x-axis

# we can make multiple calls to plt.plot
# to show multiple series on the same chart

plt.plot(xs, variance,     'g-', label='variance')              # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')               # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error')            # blue dotted line

# because we've assigned labels to each series
# we can get a legend for free
plt.legend(loc=9)                                            # loc=9 means "top center" 
plt.xlabel('model complexity')
plt.xticks([])                                               # no x-axis labels
plt.title('The Bias-Variance Tradeoff')
plt.show()
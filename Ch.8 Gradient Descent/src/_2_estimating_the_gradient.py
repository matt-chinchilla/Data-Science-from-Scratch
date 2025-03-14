#1) "f" is a function of one variable / derivative at point "x" measures how f(x) changes
        # when a small change is made to x
        # "Derivative" = limit of the quotient differences

from typing import Callable
# takes a float and returns a float
def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    """Computes the difference quotient of f at x with step(difference) h"""
    return (f(x + h) - f(x)) / h


#---------------------------------------------------------------------------------------------
#2) Calculating easy derivatives:
def square(x: float) -> float:
    return x * x

    #Its derivative
def derivative(x: float) -> float:
    return 2 * x


#Ex: estimating derivatives by evaluating the difference quatient for a very small "e"
xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h = 0.01) for x in xs]

# plot to show that they are basically the same
import matplotlib.pyplot as plt
plt.title('Actual Derivatives vs. estimates')
plt.plot(xs, actuals, 'rx', label='Actual')         # red x
plt.plot(xs, estimates, 'b+', label='Estimate')     # blue +
plt.legend(loc=9)
plt.xlabel("Inputted value")
plt.ylabel("Derivative value")
plt.show()


#---------------------------------------------------------------------------------------------
#3) Estimating the gradient of a function with multiple variables --> Therefore multiple
                                                                #    partial derivatives

        # How we do this: calculate the "i-th" partial derivative by treating it as 
        # a function of JUST its "i-th" variable and keeping the other variables constant
from A_vectors import Vector

def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: int,
                                h: float) -> float:
    w = [v_j + (h if j == i else 0)     # Add h to the i-th element of v
         for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_gradient(f: Callable[[Vector], float],
                      v: Vector,
                      h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]
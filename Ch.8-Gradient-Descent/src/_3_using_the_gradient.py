# using the gradient
    # Picking a random starting point and then taking tiny steps in the opposite direction
    # until we reach a point where teh gradient is very small

import random
from linear_algebra import Vector, distance, add, scalar_multiply

def gradient_step (v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves 'step_size in the 'gradient' direction from 'v' """
    assert len(v) == len(gradient), "Vectors must be the same length"
    step = scalar_multiply(step_size, gradient) # multiply each element of gradient by step_size
    return add(v, step) # add the step to the current vector v

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

# pick a random starting point
v = [random.uniform(-10, 10) for i in range(3)]

# epoch == one step
for epoch in range(100):
    gradient = sum_of_squares_gradient(v)
    v = gradient_step(v, gradient, -0.01)                       # Compute the gradient at v
    print(epoch, v)                                             # take a negative gradient step

assert distance(v, [0, 0, 0]) < 0.01                            # v should be close to 0


#--------------------------------------------------------------------------------------------
#2) Using the gradient to try and find model-parameters that minimize "loss" aka the error

    # x ranges from -50 to 49, y is always 20 * x + 5
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]


        # Using G.D. to find the slope & intercept that minimized avg(err ** 2)

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept    # prediction of the model
    error = (predicted - y)              # error is (predicted - actual)
    squared_error = error ** 2           # We'll minimize squared error
    grad = [2 * error * x, 2 * error]    # using its gradient.
    return grad


#--------------------------------------------------------------------------------------------
#3) "Mean Squared Error" --> Mean of the individual gradients
    # Steps:
            ## 1) Start w/ random val for Θ 
            ## 2) Compute µ (mean) of the gradients
            ## 3) Adjust Θ in that direction
            ## 4) Repeat until convergence

from linear_algebra import vector_mean

# Starting with random vals for slope
         #Θ_0                   Θ_1
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

for epoch in range(5000):
    # Compute mean of the gradients
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
    # Take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)

slope, intercept = theta
assert 19.9 < slope < 20.1,      "slope should be about 20"
assert 4.9 < intercept < 5.1,    "intercept should be about 5"


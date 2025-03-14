#1) "minibatch gradient descent" --> computing gradient from a "minibatch" sampled from the larger set

from typing import TypeVar, List, Iterator
from linear_algebra import vector_mean
from _3_using_the_gradient import gradient_step, inputs, linear_gradient, learning_rate
import random

T = TypeVar('T')     # Allows for the typing of 'generic' fxns

def minibatches(dataset: List[T],
                batch_size: int,
                shuffle: bool = True) -> Iterator[List[T]]: # Produces an iterator of minibatches
    """Generates `batch_size`-sized minibatches from the dataset"""
    # Start indexes 0, batch_size, 2 * batch_size, ...
    batch_starts = [start for start in range(0, len(dataset), batch_size)]

    if shuffle: random.shuffle(batch_starts)  # shuffle the batches

    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]  # yield the batch from start to end


#------------------------------------------------------------------------------
#2) Solving our problem once again using minibatches
  # Minibatch gradient descent example
    
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    
    for epoch in range(1000):
        for batch in minibatches(inputs, batch_size=20):
            grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
            theta = gradient_step(theta, grad, -learning_rate)
        print(epoch, theta)
    
    slope, intercept = theta
    assert 19.9 < slope < 20.1,   "slope should be about 20"
    assert 4.9 < intercept < 5.1, "intercept should be about 5"


#--------------------------------------------------------------------------------------------
#3) "stochastic gradient descent" --> computing gradient from a single randomly sampled example
   
    # Stochastic gradient descent example
    
    theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
    
    for epoch in range(100):
        for x, y in inputs:
            grad = linear_gradient(x, y, theta)
            theta = gradient_step(theta, grad, -learning_rate)
        print(epoch, theta)
    
    slope, intercept = theta
    assert 19.9 < slope < 20.1,   "slope should be about 20"
    assert 4.9 < intercept < 5.1, "intercept should be about 5"
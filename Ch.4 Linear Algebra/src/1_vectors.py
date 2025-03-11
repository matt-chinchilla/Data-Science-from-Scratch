#1a) "Vector" --> objects that can be added together to form new vectors
                # and can be multiplied by "scalars" (i.e. numbers) to form new vectors

    # Vectors are points in finite-dimensional space
        ## Very useful way to represent numeric data

    # simplest from-scratch approach is to represent vectors as lists of numbers
        ## Ex: [1, 2, 3] is a vector in 3-dimensional space

    # ** We accomplish this with a type alias that says a "Vector" is a list of floats **

from typing import List

Vector = List[float]

height_weight_age = [70,    #inches
                     170,   #pounds
                     40]    #years

grades = [95,   #exam 1
          80,   #exam 2
          75,   #exam 3
          62]   #exam 4


#----------------------------------------------------------------------------------
# 1b) "Vector addition" --> adding two vectors together to form a new vector
#       ## Ex: [1, 2, 3] + [4, 5, 6] = [5, 7, 9]
# 
# Can be easily implemented by "ziping" the vectors together
#       ## And using a list comprehension to add the corresponding elements together

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]       


#----------------------------------------------------------------------------------
# 1c) "Vector subtraction" --> subtracting two vectors to form a new vector

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


#----------------------------------------------------------------------------------
# 1d) "Vector componentwise sum} --> adding together all the components of a vector to form
#                                    1 Dimension of a new vector

def vector_sum(vectors: List[Vector]) -> Vector:     # Takes a list of lists (vector of vectors)
                                                     # and expects a single vector output
    """Sums all corresponding elements"""
    # Check the vectors are all the same size
    assert vectors, "no vectors provided!"

    # Check equal length of vectors
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors) # Make sure lengths are equal for each vector in Vectors

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


#--------------------------------------------------------------------------------------
#1e) "Vector scalar multiplication" --> multiplying a vector by a scalar to form a new vector

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


#--------------------------------------------------------------------------------------
#1f) "Vector componentwise means" --> taking the average of EACH component of a vector
#                                       to form a new vector (same-sized)

def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
    ## ^^ returns (# number of vectors, value of average)

print(vector_mean([[1, 12], [3, 4], [5, 6]]))


#--------------------------------------------------------------------------------------
#1g) "Dot Product" --> Multiplying v[i] * w[i], v[j] * w[j], etc... and Summing them
def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be the same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32 # 1*4 + 2*5 + 3*6 = 32


#--------------------------------------------------------------------------------------
#1h) "Vector magnitude" --> Length of a vector (distance from origin to point)
        ## Beginning with a "sum of squares" calculation

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

        ## using this function to make a "magnitude" function

import math

def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5       # Pythagorean Theorem


#--------------------------------------------------------------------------------------
#1i) "Distance Between 2 Vectors Formula

def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))

        ## Will probably look cleaner if it is written as this equivalence
def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))
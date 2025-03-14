# Ex: Function "f" / input of ' vector of real numbers' / output of 'single real number'
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2] # 2 layers deep
probability_src = project_root / "Ch.4 Linear Algebra" / "src" # Construct the path
sys.path.append(str(probability_src)) # Now Line 31 works

from A_vectors import Vector, dot

def sum_of_squares(v: Vector) -> float:
    """Computers the sum of squared elements in Vector, v"""
    return dot(v, v) 

        # Why we will use Gradient descent: Need to MAXIMIZE or MINIMIZE these types of functions
        # a.k.a -> find the input "v" that gives the largest (or smallest) value

#-----------------------------------------------------------------------------------------------
#2) "Gradient" == a vector of partial derivatives || "slopes" of the function at a given point
        ## It gives the input direction in which the function most quickly increases

# How to maximize a function (one method):
    ## 1) Pick a random starting point
    ## 2) Compute the gradient at that point
    ## 3) Move a small amount in the direction of the gradient (the direction 
         # that causes the most amount of increase)
    ## 4) Repeat with the new point

#2a) "Matrix" --> a 2-dimensional collection of numbers
        ## It will be a "list of lists" to me
        ## Matrices are represented by Capital Letters

# Another type alias
from typing import List

Matrix = List[List[float]]

A: Matrix = [[1, 2, 3],     # A has 2 rows and 3 columns
     [4, 5, 6]]

B: Matrix = [[1,2],         # B has 3 rows and 2 columns
             [3,4],
             [5,6]]

#----------------------------------------------------------------------------------
#2b) "shape" of a matrix --> len(A) rows, and len(A[0]) columns
from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows A, # of columns A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0            # num of elements in the first row
    return num_rows, num_cols

assert shape([1,2,3], [4,5,6]) == (2,3)         # 2 rows, 3 columns



#----------------------------------------------------------------------------------
#2c) "nested list comprehension" --> method for creating a matrix given its shape
#                                    and a function for generating its elements
from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols Matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)                 # given i, create a list
             for j in range(num_cols)]      # [entry_fn(i,0), ...]
             for i in range(num_rows)]      # create one list for each i


#----------------------------------------------------------------------------------
#2d) Making an "identity matrix" (1's across the diagonal) with the new function
def identity_matrix(n: int) -> Matrix:
    """Returns the nxn identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)       # When column & row are same, 1
                                                                    # else it is 0 as defined in the 
                                                                    # Lambda function
assert identity_matrix(5) == [[1,0,0,0,0],
                              [0,1,0,0,0],
                              [0,0,1,0,0],
                              [0,0,0,1,0],
                              [0,0,0,0,1]]


#-----------------------------------------------------------------------------------
#2e) Why we would use a Matrix
        ## First, it can represent a dataset with multiple vectors
        ## Ex: We have the heights, weights, and ages of 1,000 people

data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19],
         [None, None, None]]

        ## Second, they can be used in an "n x k" matrix to represent a linear function
        ## that maps "k-directional" vectors to "n-dimensional" vectors

        ## Third, the can be used to represent "binary relationships"
            ### ex: Making a Matrix A such that A[I][J] is 1 if nodes
            ### i & j are connected, otherwise it is 0


#------------------------------------------------------------------------------------
#2f) An example where we use a matrix to represent a binary pairing
friendships = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
               (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

        # Can also be represented as the following Matrix
#              user 0  1  2  3  4  5  6  7  8  9
#
friend_matrix =   [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],   # user 0
                   [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],   # user 1  
                   [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],   # user 2
                   [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],   # user 3
                   [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],   # user 4
                   [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],   # user 5
                   [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],   # user 6
                   [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],   # user 7
                   [0, 0, 0, 0, 0, 1, 1, 1, 0, 1],   # user 8
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]   # user 9

#------------------------------------------------------------------------------------
#2g) "Matrix Lookup" is much simpler for finding the connection that parsing through every edge
assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"


#------------------------------------------------------------------------------------
#2h) Inspecting node connections by only looking at a column (or row) that it corresponds to

# only need to look at one row
friends_of_five = [i
                   for i, is_friend in enumerate(friend_matrix[5])
                   if is_friend]